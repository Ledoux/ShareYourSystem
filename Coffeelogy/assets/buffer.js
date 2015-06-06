(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){


//console
console.log("ready for main")

//require some
//Reacter=require('./Reacter/src')
//Coffeer=require('./Coffeer/src')
Coder=require('./Coder/src')

},{"./Coder/src":30}],2:[function(require,module,exports){

},{}],3:[function(require,module,exports){
/*!
 * The buffer module from node.js, for the browser.
 *
 * @author   Feross Aboukhadijeh <feross@feross.org> <http://feross.org>
 * @license  MIT
 */

var base64 = require('base64-js')
var ieee754 = require('ieee754')
var isArray = require('is-array')

exports.Buffer = Buffer
exports.SlowBuffer = SlowBuffer
exports.INSPECT_MAX_BYTES = 50
Buffer.poolSize = 8192 // not used by this implementation

var kMaxLength = 0x3fffffff
var rootParent = {}

/**
 * If `Buffer.TYPED_ARRAY_SUPPORT`:
 *   === true    Use Uint8Array implementation (fastest)
 *   === false   Use Object implementation (most compatible, even IE6)
 *
 * Browsers that support typed arrays are IE 10+, Firefox 4+, Chrome 7+, Safari 5.1+,
 * Opera 11.6+, iOS 4.2+.
 *
 * Note:
 *
 * - Implementation must support adding new properties to `Uint8Array` instances.
 *   Firefox 4-29 lacked support, fixed in Firefox 30+.
 *   See: https://bugzilla.mozilla.org/show_bug.cgi?id=695438.
 *
 *  - Chrome 9-10 is missing the `TypedArray.prototype.subarray` function.
 *
 *  - IE10 has a broken `TypedArray.prototype.subarray` function which returns arrays of
 *    incorrect length in some situations.
 *
 * We detect these buggy browsers and set `Buffer.TYPED_ARRAY_SUPPORT` to `false` so they will
 * get the Object implementation, which is slower but will work correctly.
 */
Buffer.TYPED_ARRAY_SUPPORT = (function () {
  try {
    var buf = new ArrayBuffer(0)
    var arr = new Uint8Array(buf)
    arr.foo = function () { return 42 }
    return arr.foo() === 42 && // typed array instances can be augmented
        typeof arr.subarray === 'function' && // chrome 9-10 lack `subarray`
        new Uint8Array(1).subarray(1, 1).byteLength === 0 // ie10 has broken `subarray`
  } catch (e) {
    return false
  }
})()

/**
 * Class: Buffer
 * =============
 *
 * The Buffer constructor returns instances of `Uint8Array` that are augmented
 * with function properties for all the node `Buffer` API functions. We use
 * `Uint8Array` so that square bracket notation works as expected -- it returns
 * a single octet.
 *
 * By augmenting the instances, we can avoid modifying the `Uint8Array`
 * prototype.
 */
function Buffer (arg) {
  if (!(this instanceof Buffer)) {
    // Avoid going through an ArgumentsAdaptorTrampoline in the common case.
    if (arguments.length > 1) return new Buffer(arg, arguments[1])
    return new Buffer(arg)
  }

  this.length = 0
  this.parent = undefined

  // Common case.
  if (typeof arg === 'number') {
    return fromNumber(this, arg)
  }

  // Slightly less common case.
  if (typeof arg === 'string') {
    return fromString(this, arg, arguments.length > 1 ? arguments[1] : 'utf8')
  }

  // Unusual.
  return fromObject(this, arg)
}

function fromNumber (that, length) {
  that = allocate(that, length < 0 ? 0 : checked(length) | 0)
  if (!Buffer.TYPED_ARRAY_SUPPORT) {
    for (var i = 0; i < length; i++) {
      that[i] = 0
    }
  }
  return that
}

function fromString (that, string, encoding) {
  if (typeof encoding !== 'string' || encoding === '') encoding = 'utf8'

  // Assumption: byteLength() return value is always < kMaxLength.
  var length = byteLength(string, encoding) | 0
  that = allocate(that, length)

  that.write(string, encoding)
  return that
}

function fromObject (that, object) {
  if (Buffer.isBuffer(object)) return fromBuffer(that, object)

  if (isArray(object)) return fromArray(that, object)

  if (object == null) {
    throw new TypeError('must start with number, buffer, array or string')
  }

  if (typeof ArrayBuffer !== 'undefined' && object.buffer instanceof ArrayBuffer) {
    return fromTypedArray(that, object)
  }

  if (object.length) return fromArrayLike(that, object)

  return fromJsonObject(that, object)
}

function fromBuffer (that, buffer) {
  var length = checked(buffer.length) | 0
  that = allocate(that, length)
  buffer.copy(that, 0, 0, length)
  return that
}

function fromArray (that, array) {
  var length = checked(array.length) | 0
  that = allocate(that, length)
  for (var i = 0; i < length; i += 1) {
    that[i] = array[i] & 255
  }
  return that
}

// Duplicate of fromArray() to keep fromArray() monomorphic.
function fromTypedArray (that, array) {
  var length = checked(array.length) | 0
  that = allocate(that, length)
  // Truncating the elements is probably not what people expect from typed
  // arrays with BYTES_PER_ELEMENT > 1 but it's compatible with the behavior
  // of the old Buffer constructor.
  for (var i = 0; i < length; i += 1) {
    that[i] = array[i] & 255
  }
  return that
}

function fromArrayLike (that, array) {
  var length = checked(array.length) | 0
  that = allocate(that, length)
  for (var i = 0; i < length; i += 1) {
    that[i] = array[i] & 255
  }
  return that
}

// Deserialize { type: 'Buffer', data: [1,2,3,...] } into a Buffer object.
// Returns a zero-length buffer for inputs that don't conform to the spec.
function fromJsonObject (that, object) {
  var array
  var length = 0

  if (object.type === 'Buffer' && isArray(object.data)) {
    array = object.data
    length = checked(array.length) | 0
  }
  that = allocate(that, length)

  for (var i = 0; i < length; i += 1) {
    that[i] = array[i] & 255
  }
  return that
}

function allocate (that, length) {
  if (Buffer.TYPED_ARRAY_SUPPORT) {
    // Return an augmented `Uint8Array` instance, for best performance
    that = Buffer._augment(new Uint8Array(length))
  } else {
    // Fallback: Return an object instance of the Buffer class
    that.length = length
    that._isBuffer = true
  }

  var fromPool = length !== 0 && length <= Buffer.poolSize >>> 1
  if (fromPool) that.parent = rootParent

  return that
}

function checked (length) {
  // Note: cannot use `length < kMaxLength` here because that fails when
  // length is NaN (which is otherwise coerced to zero.)
  if (length >= kMaxLength) {
    throw new RangeError('Attempt to allocate Buffer larger than maximum ' +
                         'size: 0x' + kMaxLength.toString(16) + ' bytes')
  }
  return length | 0
}

function SlowBuffer (subject, encoding) {
  if (!(this instanceof SlowBuffer)) return new SlowBuffer(subject, encoding)

  var buf = new Buffer(subject, encoding)
  delete buf.parent
  return buf
}

Buffer.isBuffer = function isBuffer (b) {
  return !!(b != null && b._isBuffer)
}

Buffer.compare = function compare (a, b) {
  if (!Buffer.isBuffer(a) || !Buffer.isBuffer(b)) {
    throw new TypeError('Arguments must be Buffers')
  }

  if (a === b) return 0

  var x = a.length
  var y = b.length

  var i = 0
  var len = Math.min(x, y)
  while (i < len) {
    if (a[i] !== b[i]) break

    ++i
  }

  if (i !== len) {
    x = a[i]
    y = b[i]
  }

  if (x < y) return -1
  if (y < x) return 1
  return 0
}

Buffer.isEncoding = function isEncoding (encoding) {
  switch (String(encoding).toLowerCase()) {
    case 'hex':
    case 'utf8':
    case 'utf-8':
    case 'ascii':
    case 'binary':
    case 'base64':
    case 'raw':
    case 'ucs2':
    case 'ucs-2':
    case 'utf16le':
    case 'utf-16le':
      return true
    default:
      return false
  }
}

Buffer.concat = function concat (list, length) {
  if (!isArray(list)) throw new TypeError('list argument must be an Array of Buffers.')

  if (list.length === 0) {
    return new Buffer(0)
  } else if (list.length === 1) {
    return list[0]
  }

  var i
  if (length === undefined) {
    length = 0
    for (i = 0; i < list.length; i++) {
      length += list[i].length
    }
  }

  var buf = new Buffer(length)
  var pos = 0
  for (i = 0; i < list.length; i++) {
    var item = list[i]
    item.copy(buf, pos)
    pos += item.length
  }
  return buf
}

function byteLength (string, encoding) {
  if (typeof string !== 'string') string = String(string)

  if (string.length === 0) return 0

  switch (encoding || 'utf8') {
    case 'ascii':
    case 'binary':
    case 'raw':
      return string.length
    case 'ucs2':
    case 'ucs-2':
    case 'utf16le':
    case 'utf-16le':
      return string.length * 2
    case 'hex':
      return string.length >>> 1
    case 'utf8':
    case 'utf-8':
      return utf8ToBytes(string).length
    case 'base64':
      return base64ToBytes(string).length
    default:
      return string.length
  }
}
Buffer.byteLength = byteLength

// pre-set for values that may exist in the future
Buffer.prototype.length = undefined
Buffer.prototype.parent = undefined

// toString(encoding, start=0, end=buffer.length)
Buffer.prototype.toString = function toString (encoding, start, end) {
  var loweredCase = false

  start = start | 0
  end = end === undefined || end === Infinity ? this.length : end | 0

  if (!encoding) encoding = 'utf8'
  if (start < 0) start = 0
  if (end > this.length) end = this.length
  if (end <= start) return ''

  while (true) {
    switch (encoding) {
      case 'hex':
        return hexSlice(this, start, end)

      case 'utf8':
      case 'utf-8':
        return utf8Slice(this, start, end)

      case 'ascii':
        return asciiSlice(this, start, end)

      case 'binary':
        return binarySlice(this, start, end)

      case 'base64':
        return base64Slice(this, start, end)

      case 'ucs2':
      case 'ucs-2':
      case 'utf16le':
      case 'utf-16le':
        return utf16leSlice(this, start, end)

      default:
        if (loweredCase) throw new TypeError('Unknown encoding: ' + encoding)
        encoding = (encoding + '').toLowerCase()
        loweredCase = true
    }
  }
}

Buffer.prototype.equals = function equals (b) {
  if (!Buffer.isBuffer(b)) throw new TypeError('Argument must be a Buffer')
  if (this === b) return true
  return Buffer.compare(this, b) === 0
}

Buffer.prototype.inspect = function inspect () {
  var str = ''
  var max = exports.INSPECT_MAX_BYTES
  if (this.length > 0) {
    str = this.toString('hex', 0, max).match(/.{2}/g).join(' ')
    if (this.length > max) str += ' ... '
  }
  return '<Buffer ' + str + '>'
}

Buffer.prototype.compare = function compare (b) {
  if (!Buffer.isBuffer(b)) throw new TypeError('Argument must be a Buffer')
  if (this === b) return 0
  return Buffer.compare(this, b)
}

Buffer.prototype.indexOf = function indexOf (val, byteOffset) {
  if (byteOffset > 0x7fffffff) byteOffset = 0x7fffffff
  else if (byteOffset < -0x80000000) byteOffset = -0x80000000
  byteOffset >>= 0

  if (this.length === 0) return -1
  if (byteOffset >= this.length) return -1

  // Negative offsets start from the end of the buffer
  if (byteOffset < 0) byteOffset = Math.max(this.length + byteOffset, 0)

  if (typeof val === 'string') {
    if (val.length === 0) return -1 // special case: looking for empty string always fails
    return String.prototype.indexOf.call(this, val, byteOffset)
  }
  if (Buffer.isBuffer(val)) {
    return arrayIndexOf(this, val, byteOffset)
  }
  if (typeof val === 'number') {
    if (Buffer.TYPED_ARRAY_SUPPORT && Uint8Array.prototype.indexOf === 'function') {
      return Uint8Array.prototype.indexOf.call(this, val, byteOffset)
    }
    return arrayIndexOf(this, [ val ], byteOffset)
  }

  function arrayIndexOf (arr, val, byteOffset) {
    var foundIndex = -1
    for (var i = 0; byteOffset + i < arr.length; i++) {
      if (arr[byteOffset + i] === val[foundIndex === -1 ? 0 : i - foundIndex]) {
        if (foundIndex === -1) foundIndex = i
        if (i - foundIndex + 1 === val.length) return byteOffset + foundIndex
      } else {
        foundIndex = -1
      }
    }
    return -1
  }

  throw new TypeError('val must be string, number or Buffer')
}

// `get` will be removed in Node 0.13+
Buffer.prototype.get = function get (offset) {
  console.log('.get() is deprecated. Access using array indexes instead.')
  return this.readUInt8(offset)
}

// `set` will be removed in Node 0.13+
Buffer.prototype.set = function set (v, offset) {
  console.log('.set() is deprecated. Access using array indexes instead.')
  return this.writeUInt8(v, offset)
}

function hexWrite (buf, string, offset, length) {
  offset = Number(offset) || 0
  var remaining = buf.length - offset
  if (!length) {
    length = remaining
  } else {
    length = Number(length)
    if (length > remaining) {
      length = remaining
    }
  }

  // must be an even number of digits
  var strLen = string.length
  if (strLen % 2 !== 0) throw new Error('Invalid hex string')

  if (length > strLen / 2) {
    length = strLen / 2
  }
  for (var i = 0; i < length; i++) {
    var parsed = parseInt(string.substr(i * 2, 2), 16)
    if (isNaN(parsed)) throw new Error('Invalid hex string')
    buf[offset + i] = parsed
  }
  return i
}

function utf8Write (buf, string, offset, length) {
  return blitBuffer(utf8ToBytes(string, buf.length - offset), buf, offset, length)
}

function asciiWrite (buf, string, offset, length) {
  return blitBuffer(asciiToBytes(string), buf, offset, length)
}

function binaryWrite (buf, string, offset, length) {
  return asciiWrite(buf, string, offset, length)
}

function base64Write (buf, string, offset, length) {
  return blitBuffer(base64ToBytes(string), buf, offset, length)
}

function ucs2Write (buf, string, offset, length) {
  return blitBuffer(utf16leToBytes(string, buf.length - offset), buf, offset, length)
}

Buffer.prototype.write = function write (string, offset, length, encoding) {
  // Buffer#write(string)
  if (offset === undefined) {
    encoding = 'utf8'
    length = this.length
    offset = 0
  // Buffer#write(string, encoding)
  } else if (length === undefined && typeof offset === 'string') {
    encoding = offset
    length = this.length
    offset = 0
  // Buffer#write(string, offset[, length][, encoding])
  } else if (isFinite(offset)) {
    offset = offset | 0
    if (isFinite(length)) {
      length = length | 0
      if (encoding === undefined) encoding = 'utf8'
    } else {
      encoding = length
      length = undefined
    }
  // legacy write(string, encoding, offset, length) - remove in v0.13
  } else {
    var swap = encoding
    encoding = offset
    offset = length | 0
    length = swap
  }

  var remaining = this.length - offset
  if (length === undefined || length > remaining) length = remaining

  if ((string.length > 0 && (length < 0 || offset < 0)) || offset > this.length) {
    throw new RangeError('attempt to write outside buffer bounds')
  }

  if (!encoding) encoding = 'utf8'

  var loweredCase = false
  for (;;) {
    switch (encoding) {
      case 'hex':
        return hexWrite(this, string, offset, length)

      case 'utf8':
      case 'utf-8':
        return utf8Write(this, string, offset, length)

      case 'ascii':
        return asciiWrite(this, string, offset, length)

      case 'binary':
        return binaryWrite(this, string, offset, length)

      case 'base64':
        // Warning: maxLength not taken into account in base64Write
        return base64Write(this, string, offset, length)

      case 'ucs2':
      case 'ucs-2':
      case 'utf16le':
      case 'utf-16le':
        return ucs2Write(this, string, offset, length)

      default:
        if (loweredCase) throw new TypeError('Unknown encoding: ' + encoding)
        encoding = ('' + encoding).toLowerCase()
        loweredCase = true
    }
  }
}

Buffer.prototype.toJSON = function toJSON () {
  return {
    type: 'Buffer',
    data: Array.prototype.slice.call(this._arr || this, 0)
  }
}

function base64Slice (buf, start, end) {
  if (start === 0 && end === buf.length) {
    return base64.fromByteArray(buf)
  } else {
    return base64.fromByteArray(buf.slice(start, end))
  }
}

function utf8Slice (buf, start, end) {
  var res = ''
  var tmp = ''
  end = Math.min(buf.length, end)

  for (var i = start; i < end; i++) {
    if (buf[i] <= 0x7F) {
      res += decodeUtf8Char(tmp) + String.fromCharCode(buf[i])
      tmp = ''
    } else {
      tmp += '%' + buf[i].toString(16)
    }
  }

  return res + decodeUtf8Char(tmp)
}

function asciiSlice (buf, start, end) {
  var ret = ''
  end = Math.min(buf.length, end)

  for (var i = start; i < end; i++) {
    ret += String.fromCharCode(buf[i] & 0x7F)
  }
  return ret
}

function binarySlice (buf, start, end) {
  var ret = ''
  end = Math.min(buf.length, end)

  for (var i = start; i < end; i++) {
    ret += String.fromCharCode(buf[i])
  }
  return ret
}

function hexSlice (buf, start, end) {
  var len = buf.length

  if (!start || start < 0) start = 0
  if (!end || end < 0 || end > len) end = len

  var out = ''
  for (var i = start; i < end; i++) {
    out += toHex(buf[i])
  }
  return out
}

function utf16leSlice (buf, start, end) {
  var bytes = buf.slice(start, end)
  var res = ''
  for (var i = 0; i < bytes.length; i += 2) {
    res += String.fromCharCode(bytes[i] + bytes[i + 1] * 256)
  }
  return res
}

Buffer.prototype.slice = function slice (start, end) {
  var len = this.length
  start = ~~start
  end = end === undefined ? len : ~~end

  if (start < 0) {
    start += len
    if (start < 0) start = 0
  } else if (start > len) {
    start = len
  }

  if (end < 0) {
    end += len
    if (end < 0) end = 0
  } else if (end > len) {
    end = len
  }

  if (end < start) end = start

  var newBuf
  if (Buffer.TYPED_ARRAY_SUPPORT) {
    newBuf = Buffer._augment(this.subarray(start, end))
  } else {
    var sliceLen = end - start
    newBuf = new Buffer(sliceLen, undefined)
    for (var i = 0; i < sliceLen; i++) {
      newBuf[i] = this[i + start]
    }
  }

  if (newBuf.length) newBuf.parent = this.parent || this

  return newBuf
}

/*
 * Need to make sure that buffer isn't trying to write out of bounds.
 */
function checkOffset (offset, ext, length) {
  if ((offset % 1) !== 0 || offset < 0) throw new RangeError('offset is not uint')
  if (offset + ext > length) throw new RangeError('Trying to access beyond buffer length')
}

Buffer.prototype.readUIntLE = function readUIntLE (offset, byteLength, noAssert) {
  offset = offset | 0
  byteLength = byteLength | 0
  if (!noAssert) checkOffset(offset, byteLength, this.length)

  var val = this[offset]
  var mul = 1
  var i = 0
  while (++i < byteLength && (mul *= 0x100)) {
    val += this[offset + i] * mul
  }

  return val
}

Buffer.prototype.readUIntBE = function readUIntBE (offset, byteLength, noAssert) {
  offset = offset | 0
  byteLength = byteLength | 0
  if (!noAssert) {
    checkOffset(offset, byteLength, this.length)
  }

  var val = this[offset + --byteLength]
  var mul = 1
  while (byteLength > 0 && (mul *= 0x100)) {
    val += this[offset + --byteLength] * mul
  }

  return val
}

Buffer.prototype.readUInt8 = function readUInt8 (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 1, this.length)
  return this[offset]
}

Buffer.prototype.readUInt16LE = function readUInt16LE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 2, this.length)
  return this[offset] | (this[offset + 1] << 8)
}

Buffer.prototype.readUInt16BE = function readUInt16BE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 2, this.length)
  return (this[offset] << 8) | this[offset + 1]
}

Buffer.prototype.readUInt32LE = function readUInt32LE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 4, this.length)

  return ((this[offset]) |
      (this[offset + 1] << 8) |
      (this[offset + 2] << 16)) +
      (this[offset + 3] * 0x1000000)
}

Buffer.prototype.readUInt32BE = function readUInt32BE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 4, this.length)

  return (this[offset] * 0x1000000) +
    ((this[offset + 1] << 16) |
    (this[offset + 2] << 8) |
    this[offset + 3])
}

Buffer.prototype.readIntLE = function readIntLE (offset, byteLength, noAssert) {
  offset = offset | 0
  byteLength = byteLength | 0
  if (!noAssert) checkOffset(offset, byteLength, this.length)

  var val = this[offset]
  var mul = 1
  var i = 0
  while (++i < byteLength && (mul *= 0x100)) {
    val += this[offset + i] * mul
  }
  mul *= 0x80

  if (val >= mul) val -= Math.pow(2, 8 * byteLength)

  return val
}

Buffer.prototype.readIntBE = function readIntBE (offset, byteLength, noAssert) {
  offset = offset | 0
  byteLength = byteLength | 0
  if (!noAssert) checkOffset(offset, byteLength, this.length)

  var i = byteLength
  var mul = 1
  var val = this[offset + --i]
  while (i > 0 && (mul *= 0x100)) {
    val += this[offset + --i] * mul
  }
  mul *= 0x80

  if (val >= mul) val -= Math.pow(2, 8 * byteLength)

  return val
}

Buffer.prototype.readInt8 = function readInt8 (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 1, this.length)
  if (!(this[offset] & 0x80)) return (this[offset])
  return ((0xff - this[offset] + 1) * -1)
}

Buffer.prototype.readInt16LE = function readInt16LE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 2, this.length)
  var val = this[offset] | (this[offset + 1] << 8)
  return (val & 0x8000) ? val | 0xFFFF0000 : val
}

Buffer.prototype.readInt16BE = function readInt16BE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 2, this.length)
  var val = this[offset + 1] | (this[offset] << 8)
  return (val & 0x8000) ? val | 0xFFFF0000 : val
}

Buffer.prototype.readInt32LE = function readInt32LE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 4, this.length)

  return (this[offset]) |
    (this[offset + 1] << 8) |
    (this[offset + 2] << 16) |
    (this[offset + 3] << 24)
}

Buffer.prototype.readInt32BE = function readInt32BE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 4, this.length)

  return (this[offset] << 24) |
    (this[offset + 1] << 16) |
    (this[offset + 2] << 8) |
    (this[offset + 3])
}

Buffer.prototype.readFloatLE = function readFloatLE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 4, this.length)
  return ieee754.read(this, offset, true, 23, 4)
}

Buffer.prototype.readFloatBE = function readFloatBE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 4, this.length)
  return ieee754.read(this, offset, false, 23, 4)
}

Buffer.prototype.readDoubleLE = function readDoubleLE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 8, this.length)
  return ieee754.read(this, offset, true, 52, 8)
}

Buffer.prototype.readDoubleBE = function readDoubleBE (offset, noAssert) {
  if (!noAssert) checkOffset(offset, 8, this.length)
  return ieee754.read(this, offset, false, 52, 8)
}

function checkInt (buf, value, offset, ext, max, min) {
  if (!Buffer.isBuffer(buf)) throw new TypeError('buffer must be a Buffer instance')
  if (value > max || value < min) throw new RangeError('value is out of bounds')
  if (offset + ext > buf.length) throw new RangeError('index out of range')
}

Buffer.prototype.writeUIntLE = function writeUIntLE (value, offset, byteLength, noAssert) {
  value = +value
  offset = offset | 0
  byteLength = byteLength | 0
  if (!noAssert) checkInt(this, value, offset, byteLength, Math.pow(2, 8 * byteLength), 0)

  var mul = 1
  var i = 0
  this[offset] = value & 0xFF
  while (++i < byteLength && (mul *= 0x100)) {
    this[offset + i] = (value / mul) & 0xFF
  }

  return offset + byteLength
}

Buffer.prototype.writeUIntBE = function writeUIntBE (value, offset, byteLength, noAssert) {
  value = +value
  offset = offset | 0
  byteLength = byteLength | 0
  if (!noAssert) checkInt(this, value, offset, byteLength, Math.pow(2, 8 * byteLength), 0)

  var i = byteLength - 1
  var mul = 1
  this[offset + i] = value & 0xFF
  while (--i >= 0 && (mul *= 0x100)) {
    this[offset + i] = (value / mul) & 0xFF
  }

  return offset + byteLength
}

Buffer.prototype.writeUInt8 = function writeUInt8 (value, offset, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) checkInt(this, value, offset, 1, 0xff, 0)
  if (!Buffer.TYPED_ARRAY_SUPPORT) value = Math.floor(value)
  this[offset] = value
  return offset + 1
}

function objectWriteUInt16 (buf, value, offset, littleEndian) {
  if (value < 0) value = 0xffff + value + 1
  for (var i = 0, j = Math.min(buf.length - offset, 2); i < j; i++) {
    buf[offset + i] = (value & (0xff << (8 * (littleEndian ? i : 1 - i)))) >>>
      (littleEndian ? i : 1 - i) * 8
  }
}

Buffer.prototype.writeUInt16LE = function writeUInt16LE (value, offset, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) checkInt(this, value, offset, 2, 0xffff, 0)
  if (Buffer.TYPED_ARRAY_SUPPORT) {
    this[offset] = value
    this[offset + 1] = (value >>> 8)
  } else {
    objectWriteUInt16(this, value, offset, true)
  }
  return offset + 2
}

Buffer.prototype.writeUInt16BE = function writeUInt16BE (value, offset, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) checkInt(this, value, offset, 2, 0xffff, 0)
  if (Buffer.TYPED_ARRAY_SUPPORT) {
    this[offset] = (value >>> 8)
    this[offset + 1] = value
  } else {
    objectWriteUInt16(this, value, offset, false)
  }
  return offset + 2
}

function objectWriteUInt32 (buf, value, offset, littleEndian) {
  if (value < 0) value = 0xffffffff + value + 1
  for (var i = 0, j = Math.min(buf.length - offset, 4); i < j; i++) {
    buf[offset + i] = (value >>> (littleEndian ? i : 3 - i) * 8) & 0xff
  }
}

Buffer.prototype.writeUInt32LE = function writeUInt32LE (value, offset, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) checkInt(this, value, offset, 4, 0xffffffff, 0)
  if (Buffer.TYPED_ARRAY_SUPPORT) {
    this[offset + 3] = (value >>> 24)
    this[offset + 2] = (value >>> 16)
    this[offset + 1] = (value >>> 8)
    this[offset] = value
  } else {
    objectWriteUInt32(this, value, offset, true)
  }
  return offset + 4
}

Buffer.prototype.writeUInt32BE = function writeUInt32BE (value, offset, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) checkInt(this, value, offset, 4, 0xffffffff, 0)
  if (Buffer.TYPED_ARRAY_SUPPORT) {
    this[offset] = (value >>> 24)
    this[offset + 1] = (value >>> 16)
    this[offset + 2] = (value >>> 8)
    this[offset + 3] = value
  } else {
    objectWriteUInt32(this, value, offset, false)
  }
  return offset + 4
}

Buffer.prototype.writeIntLE = function writeIntLE (value, offset, byteLength, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) {
    var limit = Math.pow(2, 8 * byteLength - 1)

    checkInt(this, value, offset, byteLength, limit - 1, -limit)
  }

  var i = 0
  var mul = 1
  var sub = value < 0 ? 1 : 0
  this[offset] = value & 0xFF
  while (++i < byteLength && (mul *= 0x100)) {
    this[offset + i] = ((value / mul) >> 0) - sub & 0xFF
  }

  return offset + byteLength
}

Buffer.prototype.writeIntBE = function writeIntBE (value, offset, byteLength, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) {
    var limit = Math.pow(2, 8 * byteLength - 1)

    checkInt(this, value, offset, byteLength, limit - 1, -limit)
  }

  var i = byteLength - 1
  var mul = 1
  var sub = value < 0 ? 1 : 0
  this[offset + i] = value & 0xFF
  while (--i >= 0 && (mul *= 0x100)) {
    this[offset + i] = ((value / mul) >> 0) - sub & 0xFF
  }

  return offset + byteLength
}

Buffer.prototype.writeInt8 = function writeInt8 (value, offset, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) checkInt(this, value, offset, 1, 0x7f, -0x80)
  if (!Buffer.TYPED_ARRAY_SUPPORT) value = Math.floor(value)
  if (value < 0) value = 0xff + value + 1
  this[offset] = value
  return offset + 1
}

Buffer.prototype.writeInt16LE = function writeInt16LE (value, offset, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) checkInt(this, value, offset, 2, 0x7fff, -0x8000)
  if (Buffer.TYPED_ARRAY_SUPPORT) {
    this[offset] = value
    this[offset + 1] = (value >>> 8)
  } else {
    objectWriteUInt16(this, value, offset, true)
  }
  return offset + 2
}

Buffer.prototype.writeInt16BE = function writeInt16BE (value, offset, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) checkInt(this, value, offset, 2, 0x7fff, -0x8000)
  if (Buffer.TYPED_ARRAY_SUPPORT) {
    this[offset] = (value >>> 8)
    this[offset + 1] = value
  } else {
    objectWriteUInt16(this, value, offset, false)
  }
  return offset + 2
}

Buffer.prototype.writeInt32LE = function writeInt32LE (value, offset, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) checkInt(this, value, offset, 4, 0x7fffffff, -0x80000000)
  if (Buffer.TYPED_ARRAY_SUPPORT) {
    this[offset] = value
    this[offset + 1] = (value >>> 8)
    this[offset + 2] = (value >>> 16)
    this[offset + 3] = (value >>> 24)
  } else {
    objectWriteUInt32(this, value, offset, true)
  }
  return offset + 4
}

Buffer.prototype.writeInt32BE = function writeInt32BE (value, offset, noAssert) {
  value = +value
  offset = offset | 0
  if (!noAssert) checkInt(this, value, offset, 4, 0x7fffffff, -0x80000000)
  if (value < 0) value = 0xffffffff + value + 1
  if (Buffer.TYPED_ARRAY_SUPPORT) {
    this[offset] = (value >>> 24)
    this[offset + 1] = (value >>> 16)
    this[offset + 2] = (value >>> 8)
    this[offset + 3] = value
  } else {
    objectWriteUInt32(this, value, offset, false)
  }
  return offset + 4
}

function checkIEEE754 (buf, value, offset, ext, max, min) {
  if (value > max || value < min) throw new RangeError('value is out of bounds')
  if (offset + ext > buf.length) throw new RangeError('index out of range')
  if (offset < 0) throw new RangeError('index out of range')
}

function writeFloat (buf, value, offset, littleEndian, noAssert) {
  if (!noAssert) {
    checkIEEE754(buf, value, offset, 4, 3.4028234663852886e+38, -3.4028234663852886e+38)
  }
  ieee754.write(buf, value, offset, littleEndian, 23, 4)
  return offset + 4
}

Buffer.prototype.writeFloatLE = function writeFloatLE (value, offset, noAssert) {
  return writeFloat(this, value, offset, true, noAssert)
}

Buffer.prototype.writeFloatBE = function writeFloatBE (value, offset, noAssert) {
  return writeFloat(this, value, offset, false, noAssert)
}

function writeDouble (buf, value, offset, littleEndian, noAssert) {
  if (!noAssert) {
    checkIEEE754(buf, value, offset, 8, 1.7976931348623157E+308, -1.7976931348623157E+308)
  }
  ieee754.write(buf, value, offset, littleEndian, 52, 8)
  return offset + 8
}

Buffer.prototype.writeDoubleLE = function writeDoubleLE (value, offset, noAssert) {
  return writeDouble(this, value, offset, true, noAssert)
}

Buffer.prototype.writeDoubleBE = function writeDoubleBE (value, offset, noAssert) {
  return writeDouble(this, value, offset, false, noAssert)
}

// copy(targetBuffer, targetStart=0, sourceStart=0, sourceEnd=buffer.length)
Buffer.prototype.copy = function copy (target, targetStart, start, end) {
  if (!start) start = 0
  if (!end && end !== 0) end = this.length
  if (targetStart >= target.length) targetStart = target.length
  if (!targetStart) targetStart = 0
  if (end > 0 && end < start) end = start

  // Copy 0 bytes; we're done
  if (end === start) return 0
  if (target.length === 0 || this.length === 0) return 0

  // Fatal error conditions
  if (targetStart < 0) {
    throw new RangeError('targetStart out of bounds')
  }
  if (start < 0 || start >= this.length) throw new RangeError('sourceStart out of bounds')
  if (end < 0) throw new RangeError('sourceEnd out of bounds')

  // Are we oob?
  if (end > this.length) end = this.length
  if (target.length - targetStart < end - start) {
    end = target.length - targetStart + start
  }

  var len = end - start

  if (len < 1000 || !Buffer.TYPED_ARRAY_SUPPORT) {
    for (var i = 0; i < len; i++) {
      target[i + targetStart] = this[i + start]
    }
  } else {
    target._set(this.subarray(start, start + len), targetStart)
  }

  return len
}

// fill(value, start=0, end=buffer.length)
Buffer.prototype.fill = function fill (value, start, end) {
  if (!value) value = 0
  if (!start) start = 0
  if (!end) end = this.length

  if (end < start) throw new RangeError('end < start')

  // Fill 0 bytes; we're done
  if (end === start) return
  if (this.length === 0) return

  if (start < 0 || start >= this.length) throw new RangeError('start out of bounds')
  if (end < 0 || end > this.length) throw new RangeError('end out of bounds')

  var i
  if (typeof value === 'number') {
    for (i = start; i < end; i++) {
      this[i] = value
    }
  } else {
    var bytes = utf8ToBytes(value.toString())
    var len = bytes.length
    for (i = start; i < end; i++) {
      this[i] = bytes[i % len]
    }
  }

  return this
}

/**
 * Creates a new `ArrayBuffer` with the *copied* memory of the buffer instance.
 * Added in Node 0.12. Only available in browsers that support ArrayBuffer.
 */
Buffer.prototype.toArrayBuffer = function toArrayBuffer () {
  if (typeof Uint8Array !== 'undefined') {
    if (Buffer.TYPED_ARRAY_SUPPORT) {
      return (new Buffer(this)).buffer
    } else {
      var buf = new Uint8Array(this.length)
      for (var i = 0, len = buf.length; i < len; i += 1) {
        buf[i] = this[i]
      }
      return buf.buffer
    }
  } else {
    throw new TypeError('Buffer.toArrayBuffer not supported in this browser')
  }
}

// HELPER FUNCTIONS
// ================

var BP = Buffer.prototype

/**
 * Augment a Uint8Array *instance* (not the Uint8Array class!) with Buffer methods
 */
Buffer._augment = function _augment (arr) {
  arr.constructor = Buffer
  arr._isBuffer = true

  // save reference to original Uint8Array set method before overwriting
  arr._set = arr.set

  // deprecated, will be removed in node 0.13+
  arr.get = BP.get
  arr.set = BP.set

  arr.write = BP.write
  arr.toString = BP.toString
  arr.toLocaleString = BP.toString
  arr.toJSON = BP.toJSON
  arr.equals = BP.equals
  arr.compare = BP.compare
  arr.indexOf = BP.indexOf
  arr.copy = BP.copy
  arr.slice = BP.slice
  arr.readUIntLE = BP.readUIntLE
  arr.readUIntBE = BP.readUIntBE
  arr.readUInt8 = BP.readUInt8
  arr.readUInt16LE = BP.readUInt16LE
  arr.readUInt16BE = BP.readUInt16BE
  arr.readUInt32LE = BP.readUInt32LE
  arr.readUInt32BE = BP.readUInt32BE
  arr.readIntLE = BP.readIntLE
  arr.readIntBE = BP.readIntBE
  arr.readInt8 = BP.readInt8
  arr.readInt16LE = BP.readInt16LE
  arr.readInt16BE = BP.readInt16BE
  arr.readInt32LE = BP.readInt32LE
  arr.readInt32BE = BP.readInt32BE
  arr.readFloatLE = BP.readFloatLE
  arr.readFloatBE = BP.readFloatBE
  arr.readDoubleLE = BP.readDoubleLE
  arr.readDoubleBE = BP.readDoubleBE
  arr.writeUInt8 = BP.writeUInt8
  arr.writeUIntLE = BP.writeUIntLE
  arr.writeUIntBE = BP.writeUIntBE
  arr.writeUInt16LE = BP.writeUInt16LE
  arr.writeUInt16BE = BP.writeUInt16BE
  arr.writeUInt32LE = BP.writeUInt32LE
  arr.writeUInt32BE = BP.writeUInt32BE
  arr.writeIntLE = BP.writeIntLE
  arr.writeIntBE = BP.writeIntBE
  arr.writeInt8 = BP.writeInt8
  arr.writeInt16LE = BP.writeInt16LE
  arr.writeInt16BE = BP.writeInt16BE
  arr.writeInt32LE = BP.writeInt32LE
  arr.writeInt32BE = BP.writeInt32BE
  arr.writeFloatLE = BP.writeFloatLE
  arr.writeFloatBE = BP.writeFloatBE
  arr.writeDoubleLE = BP.writeDoubleLE
  arr.writeDoubleBE = BP.writeDoubleBE
  arr.fill = BP.fill
  arr.inspect = BP.inspect
  arr.toArrayBuffer = BP.toArrayBuffer

  return arr
}

var INVALID_BASE64_RE = /[^+\/0-9A-z\-]/g

function base64clean (str) {
  // Node strips out invalid characters like \n and \t from the string, base64-js does not
  str = stringtrim(str).replace(INVALID_BASE64_RE, '')
  // Node converts strings with length < 2 to ''
  if (str.length < 2) return ''
  // Node allows for non-padded base64 strings (missing trailing ===), base64-js does not
  while (str.length % 4 !== 0) {
    str = str + '='
  }
  return str
}

function stringtrim (str) {
  if (str.trim) return str.trim()
  return str.replace(/^\s+|\s+$/g, '')
}

function toHex (n) {
  if (n < 16) return '0' + n.toString(16)
  return n.toString(16)
}

function utf8ToBytes (string, units) {
  units = units || Infinity
  var codePoint
  var length = string.length
  var leadSurrogate = null
  var bytes = []
  var i = 0

  for (; i < length; i++) {
    codePoint = string.charCodeAt(i)

    // is surrogate component
    if (codePoint > 0xD7FF && codePoint < 0xE000) {
      // last char was a lead
      if (leadSurrogate) {
        // 2 leads in a row
        if (codePoint < 0xDC00) {
          if ((units -= 3) > -1) bytes.push(0xEF, 0xBF, 0xBD)
          leadSurrogate = codePoint
          continue
        } else {
          // valid surrogate pair
          codePoint = leadSurrogate - 0xD800 << 10 | codePoint - 0xDC00 | 0x10000
          leadSurrogate = null
        }
      } else {
        // no lead yet

        if (codePoint > 0xDBFF) {
          // unexpected trail
          if ((units -= 3) > -1) bytes.push(0xEF, 0xBF, 0xBD)
          continue
        } else if (i + 1 === length) {
          // unpaired lead
          if ((units -= 3) > -1) bytes.push(0xEF, 0xBF, 0xBD)
          continue
        } else {
          // valid lead
          leadSurrogate = codePoint
          continue
        }
      }
    } else if (leadSurrogate) {
      // valid bmp char, but last char was a lead
      if ((units -= 3) > -1) bytes.push(0xEF, 0xBF, 0xBD)
      leadSurrogate = null
    }

    // encode utf8
    if (codePoint < 0x80) {
      if ((units -= 1) < 0) break
      bytes.push(codePoint)
    } else if (codePoint < 0x800) {
      if ((units -= 2) < 0) break
      bytes.push(
        codePoint >> 0x6 | 0xC0,
        codePoint & 0x3F | 0x80
      )
    } else if (codePoint < 0x10000) {
      if ((units -= 3) < 0) break
      bytes.push(
        codePoint >> 0xC | 0xE0,
        codePoint >> 0x6 & 0x3F | 0x80,
        codePoint & 0x3F | 0x80
      )
    } else if (codePoint < 0x200000) {
      if ((units -= 4) < 0) break
      bytes.push(
        codePoint >> 0x12 | 0xF0,
        codePoint >> 0xC & 0x3F | 0x80,
        codePoint >> 0x6 & 0x3F | 0x80,
        codePoint & 0x3F | 0x80
      )
    } else {
      throw new Error('Invalid code point')
    }
  }

  return bytes
}

function asciiToBytes (str) {
  var byteArray = []
  for (var i = 0; i < str.length; i++) {
    // Node's code seems to be doing this and not & 0x7F..
    byteArray.push(str.charCodeAt(i) & 0xFF)
  }
  return byteArray
}

function utf16leToBytes (str, units) {
  var c, hi, lo
  var byteArray = []
  for (var i = 0; i < str.length; i++) {
    if ((units -= 2) < 0) break

    c = str.charCodeAt(i)
    hi = c >> 8
    lo = c % 256
    byteArray.push(lo)
    byteArray.push(hi)
  }

  return byteArray
}

function base64ToBytes (str) {
  return base64.toByteArray(base64clean(str))
}

function blitBuffer (src, dst, offset, length) {
  for (var i = 0; i < length; i++) {
    if ((i + offset >= dst.length) || (i >= src.length)) break
    dst[i + offset] = src[i]
  }
  return i
}

function decodeUtf8Char (str) {
  try {
    return decodeURIComponent(str)
  } catch (err) {
    return String.fromCharCode(0xFFFD) // UTF 8 invalid char
  }
}

},{"base64-js":4,"ieee754":5,"is-array":6}],4:[function(require,module,exports){
var lookup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';

;(function (exports) {
	'use strict';

  var Arr = (typeof Uint8Array !== 'undefined')
    ? Uint8Array
    : Array

	var PLUS   = '+'.charCodeAt(0)
	var SLASH  = '/'.charCodeAt(0)
	var NUMBER = '0'.charCodeAt(0)
	var LOWER  = 'a'.charCodeAt(0)
	var UPPER  = 'A'.charCodeAt(0)
	var PLUS_URL_SAFE = '-'.charCodeAt(0)
	var SLASH_URL_SAFE = '_'.charCodeAt(0)

	function decode (elt) {
		var code = elt.charCodeAt(0)
		if (code === PLUS ||
		    code === PLUS_URL_SAFE)
			return 62 // '+'
		if (code === SLASH ||
		    code === SLASH_URL_SAFE)
			return 63 // '/'
		if (code < NUMBER)
			return -1 //no match
		if (code < NUMBER + 10)
			return code - NUMBER + 26 + 26
		if (code < UPPER + 26)
			return code - UPPER
		if (code < LOWER + 26)
			return code - LOWER + 26
	}

	function b64ToByteArray (b64) {
		var i, j, l, tmp, placeHolders, arr

		if (b64.length % 4 > 0) {
			throw new Error('Invalid string. Length must be a multiple of 4')
		}

		// the number of equal signs (place holders)
		// if there are two placeholders, than the two characters before it
		// represent one byte
		// if there is only one, then the three characters before it represent 2 bytes
		// this is just a cheap hack to not do indexOf twice
		var len = b64.length
		placeHolders = '=' === b64.charAt(len - 2) ? 2 : '=' === b64.charAt(len - 1) ? 1 : 0

		// base64 is 4/3 + up to two characters of the original data
		arr = new Arr(b64.length * 3 / 4 - placeHolders)

		// if there are placeholders, only get up to the last complete 4 chars
		l = placeHolders > 0 ? b64.length - 4 : b64.length

		var L = 0

		function push (v) {
			arr[L++] = v
		}

		for (i = 0, j = 0; i < l; i += 4, j += 3) {
			tmp = (decode(b64.charAt(i)) << 18) | (decode(b64.charAt(i + 1)) << 12) | (decode(b64.charAt(i + 2)) << 6) | decode(b64.charAt(i + 3))
			push((tmp & 0xFF0000) >> 16)
			push((tmp & 0xFF00) >> 8)
			push(tmp & 0xFF)
		}

		if (placeHolders === 2) {
			tmp = (decode(b64.charAt(i)) << 2) | (decode(b64.charAt(i + 1)) >> 4)
			push(tmp & 0xFF)
		} else if (placeHolders === 1) {
			tmp = (decode(b64.charAt(i)) << 10) | (decode(b64.charAt(i + 1)) << 4) | (decode(b64.charAt(i + 2)) >> 2)
			push((tmp >> 8) & 0xFF)
			push(tmp & 0xFF)
		}

		return arr
	}

	function uint8ToBase64 (uint8) {
		var i,
			extraBytes = uint8.length % 3, // if we have 1 byte left, pad 2 bytes
			output = "",
			temp, length

		function encode (num) {
			return lookup.charAt(num)
		}

		function tripletToBase64 (num) {
			return encode(num >> 18 & 0x3F) + encode(num >> 12 & 0x3F) + encode(num >> 6 & 0x3F) + encode(num & 0x3F)
		}

		// go through the array every three bytes, we'll deal with trailing stuff later
		for (i = 0, length = uint8.length - extraBytes; i < length; i += 3) {
			temp = (uint8[i] << 16) + (uint8[i + 1] << 8) + (uint8[i + 2])
			output += tripletToBase64(temp)
		}

		// pad the end with zeros, but make sure to not forget the extra bytes
		switch (extraBytes) {
			case 1:
				temp = uint8[uint8.length - 1]
				output += encode(temp >> 2)
				output += encode((temp << 4) & 0x3F)
				output += '=='
				break
			case 2:
				temp = (uint8[uint8.length - 2] << 8) + (uint8[uint8.length - 1])
				output += encode(temp >> 10)
				output += encode((temp >> 4) & 0x3F)
				output += encode((temp << 2) & 0x3F)
				output += '='
				break
		}

		return output
	}

	exports.toByteArray = b64ToByteArray
	exports.fromByteArray = uint8ToBase64
}(typeof exports === 'undefined' ? (this.base64js = {}) : exports))

},{}],5:[function(require,module,exports){
exports.read = function (buffer, offset, isLE, mLen, nBytes) {
  var e, m,
      eLen = nBytes * 8 - mLen - 1,
      eMax = (1 << eLen) - 1,
      eBias = eMax >> 1,
      nBits = -7,
      i = isLE ? (nBytes - 1) : 0,
      d = isLE ? -1 : 1,
      s = buffer[offset + i]

  i += d

  e = s & ((1 << (-nBits)) - 1)
  s >>= (-nBits)
  nBits += eLen
  for (; nBits > 0; e = e * 256 + buffer[offset + i], i += d, nBits -= 8) {}

  m = e & ((1 << (-nBits)) - 1)
  e >>= (-nBits)
  nBits += mLen
  for (; nBits > 0; m = m * 256 + buffer[offset + i], i += d, nBits -= 8) {}

  if (e === 0) {
    e = 1 - eBias
  } else if (e === eMax) {
    return m ? NaN : ((s ? -1 : 1) * Infinity)
  } else {
    m = m + Math.pow(2, mLen)
    e = e - eBias
  }
  return (s ? -1 : 1) * m * Math.pow(2, e - mLen)
}

exports.write = function (buffer, value, offset, isLE, mLen, nBytes) {
  var e, m, c,
      eLen = nBytes * 8 - mLen - 1,
      eMax = (1 << eLen) - 1,
      eBias = eMax >> 1,
      rt = (mLen === 23 ? Math.pow(2, -24) - Math.pow(2, -77) : 0),
      i = isLE ? 0 : (nBytes - 1),
      d = isLE ? 1 : -1,
      s = value < 0 || (value === 0 && 1 / value < 0) ? 1 : 0

  value = Math.abs(value)

  if (isNaN(value) || value === Infinity) {
    m = isNaN(value) ? 1 : 0
    e = eMax
  } else {
    e = Math.floor(Math.log(value) / Math.LN2)
    if (value * (c = Math.pow(2, -e)) < 1) {
      e--
      c *= 2
    }
    if (e + eBias >= 1) {
      value += rt / c
    } else {
      value += rt * Math.pow(2, 1 - eBias)
    }
    if (value * c >= 2) {
      e++
      c /= 2
    }

    if (e + eBias >= eMax) {
      m = 0
      e = eMax
    } else if (e + eBias >= 1) {
      m = (value * c - 1) * Math.pow(2, mLen)
      e = e + eBias
    } else {
      m = value * Math.pow(2, eBias - 1) * Math.pow(2, mLen)
      e = 0
    }
  }

  for (; mLen >= 8; buffer[offset + i] = m & 0xff, i += d, m /= 256, mLen -= 8) {}

  e = (e << mLen) | m
  eLen += mLen
  for (; eLen > 0; buffer[offset + i] = e & 0xff, i += d, e /= 256, eLen -= 8) {}

  buffer[offset + i - d] |= s * 128
}

},{}],6:[function(require,module,exports){

/**
 * isArray
 */

var isArray = Array.isArray;

/**
 * toString
 */

var str = Object.prototype.toString;

/**
 * Whether or not the given `val`
 * is an array.
 *
 * example:
 *
 *        isArray([]);
 *        // > true
 *        isArray(arguments);
 *        // > false
 *        isArray('');
 *        // > false
 *
 * @param {mixed} val
 * @return {bool}
 */

module.exports = isArray || function (val) {
  return !! val && '[object Array]' == str.call(val);
};

},{}],7:[function(require,module,exports){
(function (process){
// Copyright Joyent, Inc. and other Node contributors.
//
// Permission is hereby granted, free of charge, to any person obtaining a
// copy of this software and associated documentation files (the
// "Software"), to deal in the Software without restriction, including
// without limitation the rights to use, copy, modify, merge, publish,
// distribute, sublicense, and/or sell copies of the Software, and to permit
// persons to whom the Software is furnished to do so, subject to the
// following conditions:
//
// The above copyright notice and this permission notice shall be included
// in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
// OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
// NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
// DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
// OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
// USE OR OTHER DEALINGS IN THE SOFTWARE.

// resolves . and .. elements in a path array with directory names there
// must be no slashes, empty elements, or device names (c:\) in the array
// (so also no leading and trailing slashes - it does not distinguish
// relative and absolute paths)
function normalizeArray(parts, allowAboveRoot) {
  // if the path tries to go above the root, `up` ends up > 0
  var up = 0;
  for (var i = parts.length - 1; i >= 0; i--) {
    var last = parts[i];
    if (last === '.') {
      parts.splice(i, 1);
    } else if (last === '..') {
      parts.splice(i, 1);
      up++;
    } else if (up) {
      parts.splice(i, 1);
      up--;
    }
  }

  // if the path is allowed to go above the root, restore leading ..s
  if (allowAboveRoot) {
    for (; up--; up) {
      parts.unshift('..');
    }
  }

  return parts;
}

// Split a filename into [root, dir, basename, ext], unix version
// 'root' is just a slash, or nothing.
var splitPathRe =
    /^(\/?|)([\s\S]*?)((?:\.{1,2}|[^\/]+?|)(\.[^.\/]*|))(?:[\/]*)$/;
var splitPath = function(filename) {
  return splitPathRe.exec(filename).slice(1);
};

// path.resolve([from ...], to)
// posix version
exports.resolve = function() {
  var resolvedPath = '',
      resolvedAbsolute = false;

  for (var i = arguments.length - 1; i >= -1 && !resolvedAbsolute; i--) {
    var path = (i >= 0) ? arguments[i] : process.cwd();

    // Skip empty and invalid entries
    if (typeof path !== 'string') {
      throw new TypeError('Arguments to path.resolve must be strings');
    } else if (!path) {
      continue;
    }

    resolvedPath = path + '/' + resolvedPath;
    resolvedAbsolute = path.charAt(0) === '/';
  }

  // At this point the path should be resolved to a full absolute path, but
  // handle relative paths to be safe (might happen when process.cwd() fails)

  // Normalize the path
  resolvedPath = normalizeArray(filter(resolvedPath.split('/'), function(p) {
    return !!p;
  }), !resolvedAbsolute).join('/');

  return ((resolvedAbsolute ? '/' : '') + resolvedPath) || '.';
};

// path.normalize(path)
// posix version
exports.normalize = function(path) {
  var isAbsolute = exports.isAbsolute(path),
      trailingSlash = substr(path, -1) === '/';

  // Normalize the path
  path = normalizeArray(filter(path.split('/'), function(p) {
    return !!p;
  }), !isAbsolute).join('/');

  if (!path && !isAbsolute) {
    path = '.';
  }
  if (path && trailingSlash) {
    path += '/';
  }

  return (isAbsolute ? '/' : '') + path;
};

// posix version
exports.isAbsolute = function(path) {
  return path.charAt(0) === '/';
};

// posix version
exports.join = function() {
  var paths = Array.prototype.slice.call(arguments, 0);
  return exports.normalize(filter(paths, function(p, index) {
    if (typeof p !== 'string') {
      throw new TypeError('Arguments to path.join must be strings');
    }
    return p;
  }).join('/'));
};


// path.relative(from, to)
// posix version
exports.relative = function(from, to) {
  from = exports.resolve(from).substr(1);
  to = exports.resolve(to).substr(1);

  function trim(arr) {
    var start = 0;
    for (; start < arr.length; start++) {
      if (arr[start] !== '') break;
    }

    var end = arr.length - 1;
    for (; end >= 0; end--) {
      if (arr[end] !== '') break;
    }

    if (start > end) return [];
    return arr.slice(start, end - start + 1);
  }

  var fromParts = trim(from.split('/'));
  var toParts = trim(to.split('/'));

  var length = Math.min(fromParts.length, toParts.length);
  var samePartsLength = length;
  for (var i = 0; i < length; i++) {
    if (fromParts[i] !== toParts[i]) {
      samePartsLength = i;
      break;
    }
  }

  var outputParts = [];
  for (var i = samePartsLength; i < fromParts.length; i++) {
    outputParts.push('..');
  }

  outputParts = outputParts.concat(toParts.slice(samePartsLength));

  return outputParts.join('/');
};

exports.sep = '/';
exports.delimiter = ':';

exports.dirname = function(path) {
  var result = splitPath(path),
      root = result[0],
      dir = result[1];

  if (!root && !dir) {
    // No dirname whatsoever
    return '.';
  }

  if (dir) {
    // It has a dirname, strip trailing slash
    dir = dir.substr(0, dir.length - 1);
  }

  return root + dir;
};


exports.basename = function(path, ext) {
  var f = splitPath(path)[2];
  // TODO: make this comparison case-insensitive on windows?
  if (ext && f.substr(-1 * ext.length) === ext) {
    f = f.substr(0, f.length - ext.length);
  }
  return f;
};


exports.extname = function(path) {
  return splitPath(path)[3];
};

function filter (xs, f) {
    if (xs.filter) return xs.filter(f);
    var res = [];
    for (var i = 0; i < xs.length; i++) {
        if (f(xs[i], i, xs)) res.push(xs[i]);
    }
    return res;
}

// String.prototype.substr - negative index don't work in IE8
var substr = 'ab'.substr(-1) === 'b'
    ? function (str, start, len) { return str.substr(start, len) }
    : function (str, start, len) {
        if (start < 0) start = str.length + start;
        return str.substr(start, len);
    }
;

}).call(this,require('_process'))
},{"_process":8}],8:[function(require,module,exports){
// shim for using process in browser

var process = module.exports = {};
var queue = [];
var draining = false;
var currentQueue;
var queueIndex = -1;

function cleanUpNextTick() {
    draining = false;
    if (currentQueue.length) {
        queue = currentQueue.concat(queue);
    } else {
        queueIndex = -1;
    }
    if (queue.length) {
        drainQueue();
    }
}

function drainQueue() {
    if (draining) {
        return;
    }
    var timeout = setTimeout(cleanUpNextTick);
    draining = true;

    var len = queue.length;
    while(len) {
        currentQueue = queue;
        queue = [];
        while (++queueIndex < len) {
            currentQueue[queueIndex].run();
        }
        queueIndex = -1;
        len = queue.length;
    }
    currentQueue = null;
    draining = false;
    clearTimeout(timeout);
}

process.nextTick = function (fun) {
    var args = new Array(arguments.length - 1);
    if (arguments.length > 1) {
        for (var i = 1; i < arguments.length; i++) {
            args[i - 1] = arguments[i];
        }
    }
    queue.push(new Item(fun, args));
    if (queue.length === 1 && !draining) {
        setTimeout(drainQueue, 0);
    }
};

// v8 likes predictible objects
function Item(fun, array) {
    this.fun = fun;
    this.array = array;
}
Item.prototype.run = function () {
    this.fun.apply(null, this.array);
};
process.title = 'browser';
process.browser = true;
process.env = {};
process.argv = [];
process.version = ''; // empty string to avoid regexp issues
process.versions = {};

function noop() {}

process.on = noop;
process.addListener = noop;
process.once = noop;
process.off = noop;
process.removeListener = noop;
process.removeAllListeners = noop;
process.emit = noop;

process.binding = function (name) {
    throw new Error('process.binding is not supported');
};

// TODO(shtylman)
process.cwd = function () { return '/' };
process.chdir = function (dir) {
    throw new Error('process.chdir is not supported');
};
process.umask = function() { return 0; };

},{}],9:[function(require,module,exports){
var indexOf = require('indexof');

var Object_keys = function (obj) {
    if (Object.keys) return Object.keys(obj)
    else {
        var res = [];
        for (var key in obj) res.push(key)
        return res;
    }
};

var forEach = function (xs, fn) {
    if (xs.forEach) return xs.forEach(fn)
    else for (var i = 0; i < xs.length; i++) {
        fn(xs[i], i, xs);
    }
};

var defineProp = (function() {
    try {
        Object.defineProperty({}, '_', {});
        return function(obj, name, value) {
            Object.defineProperty(obj, name, {
                writable: true,
                enumerable: false,
                configurable: true,
                value: value
            })
        };
    } catch(e) {
        return function(obj, name, value) {
            obj[name] = value;
        };
    }
}());

var globals = ['Array', 'Boolean', 'Date', 'Error', 'EvalError', 'Function',
'Infinity', 'JSON', 'Math', 'NaN', 'Number', 'Object', 'RangeError',
'ReferenceError', 'RegExp', 'String', 'SyntaxError', 'TypeError', 'URIError',
'decodeURI', 'decodeURIComponent', 'encodeURI', 'encodeURIComponent', 'escape',
'eval', 'isFinite', 'isNaN', 'parseFloat', 'parseInt', 'undefined', 'unescape'];

function Context() {}
Context.prototype = {};

var Script = exports.Script = function NodeScript (code) {
    if (!(this instanceof Script)) return new Script(code);
    this.code = code;
};

Script.prototype.runInContext = function (context) {
    if (!(context instanceof Context)) {
        throw new TypeError("needs a 'context' argument.");
    }
    
    var iframe = document.createElement('iframe');
    if (!iframe.style) iframe.style = {};
    iframe.style.display = 'none';
    
    document.body.appendChild(iframe);
    
    var win = iframe.contentWindow;
    var wEval = win.eval, wExecScript = win.execScript;

    if (!wEval && wExecScript) {
        // win.eval() magically appears when this is called in IE:
        wExecScript.call(win, 'null');
        wEval = win.eval;
    }
    
    forEach(Object_keys(context), function (key) {
        win[key] = context[key];
    });
    forEach(globals, function (key) {
        if (context[key]) {
            win[key] = context[key];
        }
    });
    
    var winKeys = Object_keys(win);

    var res = wEval.call(win, this.code);
    
    forEach(Object_keys(win), function (key) {
        // Avoid copying circular objects like `top` and `window` by only
        // updating existing context properties or new properties in the `win`
        // that was only introduced after the eval.
        if (key in context || indexOf(winKeys, key) === -1) {
            context[key] = win[key];
        }
    });

    forEach(globals, function (key) {
        if (!(key in context)) {
            defineProp(context, key, win[key]);
        }
    });
    
    document.body.removeChild(iframe);
    
    return res;
};

Script.prototype.runInThisContext = function () {
    return eval(this.code); // maybe...
};

Script.prototype.runInNewContext = function (context) {
    var ctx = Script.createContext(context);
    var res = this.runInContext(ctx);

    forEach(Object_keys(ctx), function (key) {
        context[key] = ctx[key];
    });

    return res;
};

forEach(Object_keys(Script.prototype), function (name) {
    exports[name] = Script[name] = function (code) {
        var s = Script(code);
        return s[name].apply(s, [].slice.call(arguments, 1));
    };
});

exports.createScript = function (code) {
    return exports.Script(code);
};

exports.createContext = Script.createContext = function (context) {
    var copy = new Context();
    if(typeof context === 'object') {
        forEach(Object_keys(context), function (key) {
            copy[key] = context[key];
        });
    }
    return copy;
};

},{"indexof":10}],10:[function(require,module,exports){

var indexOf = [].indexOf;

module.exports = function(arr, obj){
  if (indexOf) return arr.indexOf(obj);
  for (var i = 0; i < arr.length; ++i) {
    if (arr[i] === obj) return i;
  }
  return -1;
};
},{}],11:[function(require,module,exports){
// CodeMirror, copyright (c) by Marijn Haverbeke and others
// Distributed under an MIT license: http://codemirror.net/LICENSE

// This is CodeMirror (http://codemirror.net), a code editor
// implemented in JavaScript on top of the browser's DOM.
//
// You can find some technical background for some of the code below
// at http://marijnhaverbeke.nl/blog/#cm-internals .

(function(mod) {
  if (typeof exports == "object" && typeof module == "object") // CommonJS
    module.exports = mod();
  else if (typeof define == "function" && define.amd) // AMD
    return define([], mod);
  else // Plain browser env
    this.CodeMirror = mod();
})(function() {
  "use strict";

  // BROWSER SNIFFING

  // Kludges for bugs and behavior differences that can't be feature
  // detected are enabled based on userAgent etc sniffing.

  var gecko = /gecko\/\d/i.test(navigator.userAgent);
  var ie_upto10 = /MSIE \d/.test(navigator.userAgent);
  var ie_11up = /Trident\/(?:[7-9]|\d{2,})\..*rv:(\d+)/.exec(navigator.userAgent);
  var ie = ie_upto10 || ie_11up;
  var ie_version = ie && (ie_upto10 ? document.documentMode || 6 : ie_11up[1]);
  var webkit = /WebKit\//.test(navigator.userAgent);
  var qtwebkit = webkit && /Qt\/\d+\.\d+/.test(navigator.userAgent);
  var chrome = /Chrome\//.test(navigator.userAgent);
  var presto = /Opera\//.test(navigator.userAgent);
  var safari = /Apple Computer/.test(navigator.vendor);
  var mac_geMountainLion = /Mac OS X 1\d\D([8-9]|\d\d)\D/.test(navigator.userAgent);
  var phantom = /PhantomJS/.test(navigator.userAgent);

  var ios = /AppleWebKit/.test(navigator.userAgent) && /Mobile\/\w+/.test(navigator.userAgent);
  // This is woefully incomplete. Suggestions for alternative methods welcome.
  var mobile = ios || /Android|webOS|BlackBerry|Opera Mini|Opera Mobi|IEMobile/i.test(navigator.userAgent);
  var mac = ios || /Mac/.test(navigator.platform);
  var windows = /win/i.test(navigator.platform);

  var presto_version = presto && navigator.userAgent.match(/Version\/(\d*\.\d*)/);
  if (presto_version) presto_version = Number(presto_version[1]);
  if (presto_version && presto_version >= 15) { presto = false; webkit = true; }
  // Some browsers use the wrong event properties to signal cmd/ctrl on OS X
  var flipCtrlCmd = mac && (qtwebkit || presto && (presto_version == null || presto_version < 12.11));
  var captureRightClick = gecko || (ie && ie_version >= 9);

  // Optimize some code when these features are not used.
  var sawReadOnlySpans = false, sawCollapsedSpans = false;

  // EDITOR CONSTRUCTOR

  // A CodeMirror instance represents an editor. This is the object
  // that user code is usually dealing with.

  function CodeMirror(place, options) {
    if (!(this instanceof CodeMirror)) return new CodeMirror(place, options);

    this.options = options = options ? copyObj(options) : {};
    // Determine effective options based on given values and defaults.
    copyObj(defaults, options, false);
    setGuttersForLineNumbers(options);

    var doc = options.value;
    if (typeof doc == "string") doc = new Doc(doc, options.mode);
    this.doc = doc;

    var input = new CodeMirror.inputStyles[options.inputStyle](this);
    var display = this.display = new Display(place, doc, input);
    display.wrapper.CodeMirror = this;
    updateGutters(this);
    themeChanged(this);
    if (options.lineWrapping)
      this.display.wrapper.className += " CodeMirror-wrap";
    if (options.autofocus && !mobile) display.input.focus();
    initScrollbars(this);

    this.state = {
      keyMaps: [],  // stores maps added by addKeyMap
      overlays: [], // highlighting overlays, as added by addOverlay
      modeGen: 0,   // bumped when mode/overlay changes, used to invalidate highlighting info
      overwrite: false,
      delayingBlurEvent: false,
      focused: false,
      suppressEdits: false, // used to disable editing during key handlers when in readOnly mode
      pasteIncoming: false, cutIncoming: false, // help recognize paste/cut edits in input.poll
      draggingText: false,
      highlight: new Delayed(), // stores highlight worker timeout
      keySeq: null,  // Unfinished key sequence
      specialChars: null
    };

    var cm = this;

    // Override magic textarea content restore that IE sometimes does
    // on our hidden textarea on reload
    if (ie && ie_version < 11) setTimeout(function() { cm.display.input.reset(true); }, 20);

    registerEventHandlers(this);
    ensureGlobalHandlers();

    startOperation(this);
    this.curOp.forceUpdate = true;
    attachDoc(this, doc);

    if ((options.autofocus && !mobile) || cm.hasFocus())
      setTimeout(bind(onFocus, this), 20);
    else
      onBlur(this);

    for (var opt in optionHandlers) if (optionHandlers.hasOwnProperty(opt))
      optionHandlers[opt](this, options[opt], Init);
    maybeUpdateLineNumberWidth(this);
    if (options.finishInit) options.finishInit(this);
    for (var i = 0; i < initHooks.length; ++i) initHooks[i](this);
    endOperation(this);
    // Suppress optimizelegibility in Webkit, since it breaks text
    // measuring on line wrapping boundaries.
    if (webkit && options.lineWrapping &&
        getComputedStyle(display.lineDiv).textRendering == "optimizelegibility")
      display.lineDiv.style.textRendering = "auto";
  }

  // DISPLAY CONSTRUCTOR

  // The display handles the DOM integration, both for input reading
  // and content drawing. It holds references to DOM nodes and
  // display-related state.

  function Display(place, doc, input) {
    var d = this;
    this.input = input;

    // Covers bottom-right square when both scrollbars are present.
    d.scrollbarFiller = elt("div", null, "CodeMirror-scrollbar-filler");
    d.scrollbarFiller.setAttribute("cm-not-content", "true");
    // Covers bottom of gutter when coverGutterNextToScrollbar is on
    // and h scrollbar is present.
    d.gutterFiller = elt("div", null, "CodeMirror-gutter-filler");
    d.gutterFiller.setAttribute("cm-not-content", "true");
    // Will contain the actual code, positioned to cover the viewport.
    d.lineDiv = elt("div", null, "CodeMirror-code");
    // Elements are added to these to represent selection and cursors.
    d.selectionDiv = elt("div", null, null, "position: relative; z-index: 1");
    d.cursorDiv = elt("div", null, "CodeMirror-cursors");
    // A visibility: hidden element used to find the size of things.
    d.measure = elt("div", null, "CodeMirror-measure");
    // When lines outside of the viewport are measured, they are drawn in this.
    d.lineMeasure = elt("div", null, "CodeMirror-measure");
    // Wraps everything that needs to exist inside the vertically-padded coordinate system
    d.lineSpace = elt("div", [d.measure, d.lineMeasure, d.selectionDiv, d.cursorDiv, d.lineDiv],
                      null, "position: relative; outline: none");
    // Moved around its parent to cover visible view.
    d.mover = elt("div", [elt("div", [d.lineSpace], "CodeMirror-lines")], null, "position: relative");
    // Set to the height of the document, allowing scrolling.
    d.sizer = elt("div", [d.mover], "CodeMirror-sizer");
    d.sizerWidth = null;
    // Behavior of elts with overflow: auto and padding is
    // inconsistent across browsers. This is used to ensure the
    // scrollable area is big enough.
    d.heightForcer = elt("div", null, null, "position: absolute; height: " + scrollerGap + "px; width: 1px;");
    // Will contain the gutters, if any.
    d.gutters = elt("div", null, "CodeMirror-gutters");
    d.lineGutter = null;
    // Actual scrollable element.
    d.scroller = elt("div", [d.sizer, d.heightForcer, d.gutters], "CodeMirror-scroll");
    d.scroller.setAttribute("tabIndex", "-1");
    // The element in which the editor lives.
    d.wrapper = elt("div", [d.scrollbarFiller, d.gutterFiller, d.scroller], "CodeMirror");

    // Work around IE7 z-index bug (not perfect, hence IE7 not really being supported)
    if (ie && ie_version < 8) { d.gutters.style.zIndex = -1; d.scroller.style.paddingRight = 0; }
    if (!webkit && !(gecko && mobile)) d.scroller.draggable = true;

    if (place) {
      if (place.appendChild) place.appendChild(d.wrapper);
      else place(d.wrapper);
    }

    // Current rendered range (may be bigger than the view window).
    d.viewFrom = d.viewTo = doc.first;
    d.reportedViewFrom = d.reportedViewTo = doc.first;
    // Information about the rendered lines.
    d.view = [];
    d.renderedView = null;
    // Holds info about a single rendered line when it was rendered
    // for measurement, while not in view.
    d.externalMeasured = null;
    // Empty space (in pixels) above the view
    d.viewOffset = 0;
    d.lastWrapHeight = d.lastWrapWidth = 0;
    d.updateLineNumbers = null;

    d.nativeBarWidth = d.barHeight = d.barWidth = 0;
    d.scrollbarsClipped = false;

    // Used to only resize the line number gutter when necessary (when
    // the amount of lines crosses a boundary that makes its width change)
    d.lineNumWidth = d.lineNumInnerWidth = d.lineNumChars = null;
    // Set to true when a non-horizontal-scrolling line widget is
    // added. As an optimization, line widget aligning is skipped when
    // this is false.
    d.alignWidgets = false;

    d.cachedCharWidth = d.cachedTextHeight = d.cachedPaddingH = null;

    // Tracks the maximum line length so that the horizontal scrollbar
    // can be kept static when scrolling.
    d.maxLine = null;
    d.maxLineLength = 0;
    d.maxLineChanged = false;

    // Used for measuring wheel scrolling granularity
    d.wheelDX = d.wheelDY = d.wheelStartX = d.wheelStartY = null;

    // True when shift is held down.
    d.shift = false;

    // Used to track whether anything happened since the context menu
    // was opened.
    d.selForContextMenu = null;

    d.activeTouch = null;

    input.init(d);
  }

  // STATE UPDATES

  // Used to get the editor into a consistent state again when options change.

  function loadMode(cm) {
    cm.doc.mode = CodeMirror.getMode(cm.options, cm.doc.modeOption);
    resetModeState(cm);
  }

  function resetModeState(cm) {
    cm.doc.iter(function(line) {
      if (line.stateAfter) line.stateAfter = null;
      if (line.styles) line.styles = null;
    });
    cm.doc.frontier = cm.doc.first;
    startWorker(cm, 100);
    cm.state.modeGen++;
    if (cm.curOp) regChange(cm);
  }

  function wrappingChanged(cm) {
    if (cm.options.lineWrapping) {
      addClass(cm.display.wrapper, "CodeMirror-wrap");
      cm.display.sizer.style.minWidth = "";
      cm.display.sizerWidth = null;
    } else {
      rmClass(cm.display.wrapper, "CodeMirror-wrap");
      findMaxLine(cm);
    }
    estimateLineHeights(cm);
    regChange(cm);
    clearCaches(cm);
    setTimeout(function(){updateScrollbars(cm);}, 100);
  }

  // Returns a function that estimates the height of a line, to use as
  // first approximation until the line becomes visible (and is thus
  // properly measurable).
  function estimateHeight(cm) {
    var th = textHeight(cm.display), wrapping = cm.options.lineWrapping;
    var perLine = wrapping && Math.max(5, cm.display.scroller.clientWidth / charWidth(cm.display) - 3);
    return function(line) {
      if (lineIsHidden(cm.doc, line)) return 0;

      var widgetsHeight = 0;
      if (line.widgets) for (var i = 0; i < line.widgets.length; i++) {
        if (line.widgets[i].height) widgetsHeight += line.widgets[i].height;
      }

      if (wrapping)
        return widgetsHeight + (Math.ceil(line.text.length / perLine) || 1) * th;
      else
        return widgetsHeight + th;
    };
  }

  function estimateLineHeights(cm) {
    var doc = cm.doc, est = estimateHeight(cm);
    doc.iter(function(line) {
      var estHeight = est(line);
      if (estHeight != line.height) updateLineHeight(line, estHeight);
    });
  }

  function themeChanged(cm) {
    cm.display.wrapper.className = cm.display.wrapper.className.replace(/\s*cm-s-\S+/g, "") +
      cm.options.theme.replace(/(^|\s)\s*/g, " cm-s-");
    clearCaches(cm);
  }

  function guttersChanged(cm) {
    updateGutters(cm);
    regChange(cm);
    setTimeout(function(){alignHorizontally(cm);}, 20);
  }

  // Rebuild the gutter elements, ensure the margin to the left of the
  // code matches their width.
  function updateGutters(cm) {
    var gutters = cm.display.gutters, specs = cm.options.gutters;
    removeChildren(gutters);
    for (var i = 0; i < specs.length; ++i) {
      var gutterClass = specs[i];
      var gElt = gutters.appendChild(elt("div", null, "CodeMirror-gutter " + gutterClass));
      if (gutterClass == "CodeMirror-linenumbers") {
        cm.display.lineGutter = gElt;
        gElt.style.width = (cm.display.lineNumWidth || 1) + "px";
      }
    }
    gutters.style.display = i ? "" : "none";
    updateGutterSpace(cm);
  }

  function updateGutterSpace(cm) {
    var width = cm.display.gutters.offsetWidth;
    cm.display.sizer.style.marginLeft = width + "px";
  }

  // Compute the character length of a line, taking into account
  // collapsed ranges (see markText) that might hide parts, and join
  // other lines onto it.
  function lineLength(line) {
    if (line.height == 0) return 0;
    var len = line.text.length, merged, cur = line;
    while (merged = collapsedSpanAtStart(cur)) {
      var found = merged.find(0, true);
      cur = found.from.line;
      len += found.from.ch - found.to.ch;
    }
    cur = line;
    while (merged = collapsedSpanAtEnd(cur)) {
      var found = merged.find(0, true);
      len -= cur.text.length - found.from.ch;
      cur = found.to.line;
      len += cur.text.length - found.to.ch;
    }
    return len;
  }

  // Find the longest line in the document.
  function findMaxLine(cm) {
    var d = cm.display, doc = cm.doc;
    d.maxLine = getLine(doc, doc.first);
    d.maxLineLength = lineLength(d.maxLine);
    d.maxLineChanged = true;
    doc.iter(function(line) {
      var len = lineLength(line);
      if (len > d.maxLineLength) {
        d.maxLineLength = len;
        d.maxLine = line;
      }
    });
  }

  // Make sure the gutters options contains the element
  // "CodeMirror-linenumbers" when the lineNumbers option is true.
  function setGuttersForLineNumbers(options) {
    var found = indexOf(options.gutters, "CodeMirror-linenumbers");
    if (found == -1 && options.lineNumbers) {
      options.gutters = options.gutters.concat(["CodeMirror-linenumbers"]);
    } else if (found > -1 && !options.lineNumbers) {
      options.gutters = options.gutters.slice(0);
      options.gutters.splice(found, 1);
    }
  }

  // SCROLLBARS

  // Prepare DOM reads needed to update the scrollbars. Done in one
  // shot to minimize update/measure roundtrips.
  function measureForScrollbars(cm) {
    var d = cm.display, gutterW = d.gutters.offsetWidth;
    var docH = Math.round(cm.doc.height + paddingVert(cm.display));
    return {
      clientHeight: d.scroller.clientHeight,
      viewHeight: d.wrapper.clientHeight,
      scrollWidth: d.scroller.scrollWidth, clientWidth: d.scroller.clientWidth,
      viewWidth: d.wrapper.clientWidth,
      barLeft: cm.options.fixedGutter ? gutterW : 0,
      docHeight: docH,
      scrollHeight: docH + scrollGap(cm) + d.barHeight,
      nativeBarWidth: d.nativeBarWidth,
      gutterWidth: gutterW
    };
  }

  function NativeScrollbars(place, scroll, cm) {
    this.cm = cm;
    var vert = this.vert = elt("div", [elt("div", null, null, "min-width: 1px")], "CodeMirror-vscrollbar");
    var horiz = this.horiz = elt("div", [elt("div", null, null, "height: 100%; min-height: 1px")], "CodeMirror-hscrollbar");
    place(vert); place(horiz);

    on(vert, "scroll", function() {
      if (vert.clientHeight) scroll(vert.scrollTop, "vertical");
    });
    on(horiz, "scroll", function() {
      if (horiz.clientWidth) scroll(horiz.scrollLeft, "horizontal");
    });

    this.checkedOverlay = false;
    // Need to set a minimum width to see the scrollbar on IE7 (but must not set it on IE8).
    if (ie && ie_version < 8) this.horiz.style.minHeight = this.vert.style.minWidth = "18px";
  }

  NativeScrollbars.prototype = copyObj({
    update: function(measure) {
      var needsH = measure.scrollWidth > measure.clientWidth + 1;
      var needsV = measure.scrollHeight > measure.clientHeight + 1;
      var sWidth = measure.nativeBarWidth;

      if (needsV) {
        this.vert.style.display = "block";
        this.vert.style.bottom = needsH ? sWidth + "px" : "0";
        var totalHeight = measure.viewHeight - (needsH ? sWidth : 0);
        // A bug in IE8 can cause this value to be negative, so guard it.
        this.vert.firstChild.style.height =
          Math.max(0, measure.scrollHeight - measure.clientHeight + totalHeight) + "px";
      } else {
        this.vert.style.display = "";
        this.vert.firstChild.style.height = "0";
      }

      if (needsH) {
        this.horiz.style.display = "block";
        this.horiz.style.right = needsV ? sWidth + "px" : "0";
        this.horiz.style.left = measure.barLeft + "px";
        var totalWidth = measure.viewWidth - measure.barLeft - (needsV ? sWidth : 0);
        this.horiz.firstChild.style.width =
          (measure.scrollWidth - measure.clientWidth + totalWidth) + "px";
      } else {
        this.horiz.style.display = "";
        this.horiz.firstChild.style.width = "0";
      }

      if (!this.checkedOverlay && measure.clientHeight > 0) {
        if (sWidth == 0) this.overlayHack();
        this.checkedOverlay = true;
      }

      return {right: needsV ? sWidth : 0, bottom: needsH ? sWidth : 0};
    },
    setScrollLeft: function(pos) {
      if (this.horiz.scrollLeft != pos) this.horiz.scrollLeft = pos;
    },
    setScrollTop: function(pos) {
      if (this.vert.scrollTop != pos) this.vert.scrollTop = pos;
    },
    overlayHack: function() {
      var w = mac && !mac_geMountainLion ? "12px" : "18px";
      this.horiz.style.minHeight = this.vert.style.minWidth = w;
      var self = this;
      var barMouseDown = function(e) {
        if (e_target(e) != self.vert && e_target(e) != self.horiz)
          operation(self.cm, onMouseDown)(e);
      };
      on(this.vert, "mousedown", barMouseDown);
      on(this.horiz, "mousedown", barMouseDown);
    },
    clear: function() {
      var parent = this.horiz.parentNode;
      parent.removeChild(this.horiz);
      parent.removeChild(this.vert);
    }
  }, NativeScrollbars.prototype);

  function NullScrollbars() {}

  NullScrollbars.prototype = copyObj({
    update: function() { return {bottom: 0, right: 0}; },
    setScrollLeft: function() {},
    setScrollTop: function() {},
    clear: function() {}
  }, NullScrollbars.prototype);

  CodeMirror.scrollbarModel = {"native": NativeScrollbars, "null": NullScrollbars};

  function initScrollbars(cm) {
    if (cm.display.scrollbars) {
      cm.display.scrollbars.clear();
      if (cm.display.scrollbars.addClass)
        rmClass(cm.display.wrapper, cm.display.scrollbars.addClass);
    }

    cm.display.scrollbars = new CodeMirror.scrollbarModel[cm.options.scrollbarStyle](function(node) {
      cm.display.wrapper.insertBefore(node, cm.display.scrollbarFiller);
      // Prevent clicks in the scrollbars from killing focus
      on(node, "mousedown", function() {
        if (cm.state.focused) setTimeout(function() { cm.display.input.focus(); }, 0);
      });
      node.setAttribute("cm-not-content", "true");
    }, function(pos, axis) {
      if (axis == "horizontal") setScrollLeft(cm, pos);
      else setScrollTop(cm, pos);
    }, cm);
    if (cm.display.scrollbars.addClass)
      addClass(cm.display.wrapper, cm.display.scrollbars.addClass);
  }

  function updateScrollbars(cm, measure) {
    if (!measure) measure = measureForScrollbars(cm);
    var startWidth = cm.display.barWidth, startHeight = cm.display.barHeight;
    updateScrollbarsInner(cm, measure);
    for (var i = 0; i < 4 && startWidth != cm.display.barWidth || startHeight != cm.display.barHeight; i++) {
      if (startWidth != cm.display.barWidth && cm.options.lineWrapping)
        updateHeightsInViewport(cm);
      updateScrollbarsInner(cm, measureForScrollbars(cm));
      startWidth = cm.display.barWidth; startHeight = cm.display.barHeight;
    }
  }

  // Re-synchronize the fake scrollbars with the actual size of the
  // content.
  function updateScrollbarsInner(cm, measure) {
    var d = cm.display;
    var sizes = d.scrollbars.update(measure);

    d.sizer.style.paddingRight = (d.barWidth = sizes.right) + "px";
    d.sizer.style.paddingBottom = (d.barHeight = sizes.bottom) + "px";

    if (sizes.right && sizes.bottom) {
      d.scrollbarFiller.style.display = "block";
      d.scrollbarFiller.style.height = sizes.bottom + "px";
      d.scrollbarFiller.style.width = sizes.right + "px";
    } else d.scrollbarFiller.style.display = "";
    if (sizes.bottom && cm.options.coverGutterNextToScrollbar && cm.options.fixedGutter) {
      d.gutterFiller.style.display = "block";
      d.gutterFiller.style.height = sizes.bottom + "px";
      d.gutterFiller.style.width = measure.gutterWidth + "px";
    } else d.gutterFiller.style.display = "";
  }

  // Compute the lines that are visible in a given viewport (defaults
  // the the current scroll position). viewport may contain top,
  // height, and ensure (see op.scrollToPos) properties.
  function visibleLines(display, doc, viewport) {
    var top = viewport && viewport.top != null ? Math.max(0, viewport.top) : display.scroller.scrollTop;
    top = Math.floor(top - paddingTop(display));
    var bottom = viewport && viewport.bottom != null ? viewport.bottom : top + display.wrapper.clientHeight;

    var from = lineAtHeight(doc, top), to = lineAtHeight(doc, bottom);
    // Ensure is a {from: {line, ch}, to: {line, ch}} object, and
    // forces those lines into the viewport (if possible).
    if (viewport && viewport.ensure) {
      var ensureFrom = viewport.ensure.from.line, ensureTo = viewport.ensure.to.line;
      if (ensureFrom < from) {
        from = ensureFrom;
        to = lineAtHeight(doc, heightAtLine(getLine(doc, ensureFrom)) + display.wrapper.clientHeight);
      } else if (Math.min(ensureTo, doc.lastLine()) >= to) {
        from = lineAtHeight(doc, heightAtLine(getLine(doc, ensureTo)) - display.wrapper.clientHeight);
        to = ensureTo;
      }
    }
    return {from: from, to: Math.max(to, from + 1)};
  }

  // LINE NUMBERS

  // Re-align line numbers and gutter marks to compensate for
  // horizontal scrolling.
  function alignHorizontally(cm) {
    var display = cm.display, view = display.view;
    if (!display.alignWidgets && (!display.gutters.firstChild || !cm.options.fixedGutter)) return;
    var comp = compensateForHScroll(display) - display.scroller.scrollLeft + cm.doc.scrollLeft;
    var gutterW = display.gutters.offsetWidth, left = comp + "px";
    for (var i = 0; i < view.length; i++) if (!view[i].hidden) {
      if (cm.options.fixedGutter && view[i].gutter)
        view[i].gutter.style.left = left;
      var align = view[i].alignable;
      if (align) for (var j = 0; j < align.length; j++)
        align[j].style.left = left;
    }
    if (cm.options.fixedGutter)
      display.gutters.style.left = (comp + gutterW) + "px";
  }

  // Used to ensure that the line number gutter is still the right
  // size for the current document size. Returns true when an update
  // is needed.
  function maybeUpdateLineNumberWidth(cm) {
    if (!cm.options.lineNumbers) return false;
    var doc = cm.doc, last = lineNumberFor(cm.options, doc.first + doc.size - 1), display = cm.display;
    if (last.length != display.lineNumChars) {
      var test = display.measure.appendChild(elt("div", [elt("div", last)],
                                                 "CodeMirror-linenumber CodeMirror-gutter-elt"));
      var innerW = test.firstChild.offsetWidth, padding = test.offsetWidth - innerW;
      display.lineGutter.style.width = "";
      display.lineNumInnerWidth = Math.max(innerW, display.lineGutter.offsetWidth - padding) + 1;
      display.lineNumWidth = display.lineNumInnerWidth + padding;
      display.lineNumChars = display.lineNumInnerWidth ? last.length : -1;
      display.lineGutter.style.width = display.lineNumWidth + "px";
      updateGutterSpace(cm);
      return true;
    }
    return false;
  }

  function lineNumberFor(options, i) {
    return String(options.lineNumberFormatter(i + options.firstLineNumber));
  }

  // Computes display.scroller.scrollLeft + display.gutters.offsetWidth,
  // but using getBoundingClientRect to get a sub-pixel-accurate
  // result.
  function compensateForHScroll(display) {
    return display.scroller.getBoundingClientRect().left - display.sizer.getBoundingClientRect().left;
  }

  // DISPLAY DRAWING

  function DisplayUpdate(cm, viewport, force) {
    var display = cm.display;

    this.viewport = viewport;
    // Store some values that we'll need later (but don't want to force a relayout for)
    this.visible = visibleLines(display, cm.doc, viewport);
    this.editorIsHidden = !display.wrapper.offsetWidth;
    this.wrapperHeight = display.wrapper.clientHeight;
    this.wrapperWidth = display.wrapper.clientWidth;
    this.oldDisplayWidth = displayWidth(cm);
    this.force = force;
    this.dims = getDimensions(cm);
    this.events = [];
  }

  DisplayUpdate.prototype.signal = function(emitter, type) {
    if (hasHandler(emitter, type))
      this.events.push(arguments);
  };
  DisplayUpdate.prototype.finish = function() {
    for (var i = 0; i < this.events.length; i++)
      signal.apply(null, this.events[i]);
  };

  function maybeClipScrollbars(cm) {
    var display = cm.display;
    if (!display.scrollbarsClipped && display.scroller.offsetWidth) {
      display.nativeBarWidth = display.scroller.offsetWidth - display.scroller.clientWidth;
      display.heightForcer.style.height = scrollGap(cm) + "px";
      display.sizer.style.marginBottom = -display.nativeBarWidth + "px";
      display.sizer.style.borderRightWidth = scrollGap(cm) + "px";
      display.scrollbarsClipped = true;
    }
  }

  // Does the actual updating of the line display. Bails out
  // (returning false) when there is nothing to be done and forced is
  // false.
  function updateDisplayIfNeeded(cm, update) {
    var display = cm.display, doc = cm.doc;

    if (update.editorIsHidden) {
      resetView(cm);
      return false;
    }

    // Bail out if the visible area is already rendered and nothing changed.
    if (!update.force &&
        update.visible.from >= display.viewFrom && update.visible.to <= display.viewTo &&
        (display.updateLineNumbers == null || display.updateLineNumbers >= display.viewTo) &&
        display.renderedView == display.view && countDirtyView(cm) == 0)
      return false;

    if (maybeUpdateLineNumberWidth(cm)) {
      resetView(cm);
      update.dims = getDimensions(cm);
    }

    // Compute a suitable new viewport (from & to)
    var end = doc.first + doc.size;
    var from = Math.max(update.visible.from - cm.options.viewportMargin, doc.first);
    var to = Math.min(end, update.visible.to + cm.options.viewportMargin);
    if (display.viewFrom < from && from - display.viewFrom < 20) from = Math.max(doc.first, display.viewFrom);
    if (display.viewTo > to && display.viewTo - to < 20) to = Math.min(end, display.viewTo);
    if (sawCollapsedSpans) {
      from = visualLineNo(cm.doc, from);
      to = visualLineEndNo(cm.doc, to);
    }

    var different = from != display.viewFrom || to != display.viewTo ||
      display.lastWrapHeight != update.wrapperHeight || display.lastWrapWidth != update.wrapperWidth;
    adjustView(cm, from, to);

    display.viewOffset = heightAtLine(getLine(cm.doc, display.viewFrom));
    // Position the mover div to align with the current scroll position
    cm.display.mover.style.top = display.viewOffset + "px";

    var toUpdate = countDirtyView(cm);
    if (!different && toUpdate == 0 && !update.force && display.renderedView == display.view &&
        (display.updateLineNumbers == null || display.updateLineNumbers >= display.viewTo))
      return false;

    // For big changes, we hide the enclosing element during the
    // update, since that speeds up the operations on most browsers.
    var focused = activeElt();
    if (toUpdate > 4) display.lineDiv.style.display = "none";
    patchDisplay(cm, display.updateLineNumbers, update.dims);
    if (toUpdate > 4) display.lineDiv.style.display = "";
    display.renderedView = display.view;
    // There might have been a widget with a focused element that got
    // hidden or updated, if so re-focus it.
    if (focused && activeElt() != focused && focused.offsetHeight) focused.focus();

    // Prevent selection and cursors from interfering with the scroll
    // width and height.
    removeChildren(display.cursorDiv);
    removeChildren(display.selectionDiv);
    display.gutters.style.height = 0;

    if (different) {
      display.lastWrapHeight = update.wrapperHeight;
      display.lastWrapWidth = update.wrapperWidth;
      startWorker(cm, 400);
    }

    display.updateLineNumbers = null;

    return true;
  }

  function postUpdateDisplay(cm, update) {
    var viewport = update.viewport;
    for (var first = true;; first = false) {
      if (!first || !cm.options.lineWrapping || update.oldDisplayWidth == displayWidth(cm)) {
        // Clip forced viewport to actual scrollable area.
        if (viewport && viewport.top != null)
          viewport = {top: Math.min(cm.doc.height + paddingVert(cm.display) - displayHeight(cm), viewport.top)};
        // Updated line heights might result in the drawn area not
        // actually covering the viewport. Keep looping until it does.
        update.visible = visibleLines(cm.display, cm.doc, viewport);
        if (update.visible.from >= cm.display.viewFrom && update.visible.to <= cm.display.viewTo)
          break;
      }
      if (!updateDisplayIfNeeded(cm, update)) break;
      updateHeightsInViewport(cm);
      var barMeasure = measureForScrollbars(cm);
      updateSelection(cm);
      setDocumentHeight(cm, barMeasure);
      updateScrollbars(cm, barMeasure);
    }

    update.signal(cm, "update", cm);
    if (cm.display.viewFrom != cm.display.reportedViewFrom || cm.display.viewTo != cm.display.reportedViewTo) {
      update.signal(cm, "viewportChange", cm, cm.display.viewFrom, cm.display.viewTo);
      cm.display.reportedViewFrom = cm.display.viewFrom; cm.display.reportedViewTo = cm.display.viewTo;
    }
  }

  function updateDisplaySimple(cm, viewport) {
    var update = new DisplayUpdate(cm, viewport);
    if (updateDisplayIfNeeded(cm, update)) {
      updateHeightsInViewport(cm);
      postUpdateDisplay(cm, update);
      var barMeasure = measureForScrollbars(cm);
      updateSelection(cm);
      setDocumentHeight(cm, barMeasure);
      updateScrollbars(cm, barMeasure);
      update.finish();
    }
  }

  function setDocumentHeight(cm, measure) {
    cm.display.sizer.style.minHeight = measure.docHeight + "px";
    var total = measure.docHeight + cm.display.barHeight;
    cm.display.heightForcer.style.top = total + "px";
    cm.display.gutters.style.height = Math.max(total + scrollGap(cm), measure.clientHeight) + "px";
  }

  // Read the actual heights of the rendered lines, and update their
  // stored heights to match.
  function updateHeightsInViewport(cm) {
    var display = cm.display;
    var prevBottom = display.lineDiv.offsetTop;
    for (var i = 0; i < display.view.length; i++) {
      var cur = display.view[i], height;
      if (cur.hidden) continue;
      if (ie && ie_version < 8) {
        var bot = cur.node.offsetTop + cur.node.offsetHeight;
        height = bot - prevBottom;
        prevBottom = bot;
      } else {
        var box = cur.node.getBoundingClientRect();
        height = box.bottom - box.top;
      }
      var diff = cur.line.height - height;
      if (height < 2) height = textHeight(display);
      if (diff > .001 || diff < -.001) {
        updateLineHeight(cur.line, height);
        updateWidgetHeight(cur.line);
        if (cur.rest) for (var j = 0; j < cur.rest.length; j++)
          updateWidgetHeight(cur.rest[j]);
      }
    }
  }

  // Read and store the height of line widgets associated with the
  // given line.
  function updateWidgetHeight(line) {
    if (line.widgets) for (var i = 0; i < line.widgets.length; ++i)
      line.widgets[i].height = line.widgets[i].node.offsetHeight;
  }

  // Do a bulk-read of the DOM positions and sizes needed to draw the
  // view, so that we don't interleave reading and writing to the DOM.
  function getDimensions(cm) {
    var d = cm.display, left = {}, width = {};
    var gutterLeft = d.gutters.clientLeft;
    for (var n = d.gutters.firstChild, i = 0; n; n = n.nextSibling, ++i) {
      left[cm.options.gutters[i]] = n.offsetLeft + n.clientLeft + gutterLeft;
      width[cm.options.gutters[i]] = n.clientWidth;
    }
    return {fixedPos: compensateForHScroll(d),
            gutterTotalWidth: d.gutters.offsetWidth,
            gutterLeft: left,
            gutterWidth: width,
            wrapperWidth: d.wrapper.clientWidth};
  }

  // Sync the actual display DOM structure with display.view, removing
  // nodes for lines that are no longer in view, and creating the ones
  // that are not there yet, and updating the ones that are out of
  // date.
  function patchDisplay(cm, updateNumbersFrom, dims) {
    var display = cm.display, lineNumbers = cm.options.lineNumbers;
    var container = display.lineDiv, cur = container.firstChild;

    function rm(node) {
      var next = node.nextSibling;
      // Works around a throw-scroll bug in OS X Webkit
      if (webkit && mac && cm.display.currentWheelTarget == node)
        node.style.display = "none";
      else
        node.parentNode.removeChild(node);
      return next;
    }

    var view = display.view, lineN = display.viewFrom;
    // Loop over the elements in the view, syncing cur (the DOM nodes
    // in display.lineDiv) with the view as we go.
    for (var i = 0; i < view.length; i++) {
      var lineView = view[i];
      if (lineView.hidden) {
      } else if (!lineView.node || lineView.node.parentNode != container) { // Not drawn yet
        var node = buildLineElement(cm, lineView, lineN, dims);
        container.insertBefore(node, cur);
      } else { // Already drawn
        while (cur != lineView.node) cur = rm(cur);
        var updateNumber = lineNumbers && updateNumbersFrom != null &&
          updateNumbersFrom <= lineN && lineView.lineNumber;
        if (lineView.changes) {
          if (indexOf(lineView.changes, "gutter") > -1) updateNumber = false;
          updateLineForChanges(cm, lineView, lineN, dims);
        }
        if (updateNumber) {
          removeChildren(lineView.lineNumber);
          lineView.lineNumber.appendChild(document.createTextNode(lineNumberFor(cm.options, lineN)));
        }
        cur = lineView.node.nextSibling;
      }
      lineN += lineView.size;
    }
    while (cur) cur = rm(cur);
  }

  // When an aspect of a line changes, a string is added to
  // lineView.changes. This updates the relevant part of the line's
  // DOM structure.
  function updateLineForChanges(cm, lineView, lineN, dims) {
    for (var j = 0; j < lineView.changes.length; j++) {
      var type = lineView.changes[j];
      if (type == "text") updateLineText(cm, lineView);
      else if (type == "gutter") updateLineGutter(cm, lineView, lineN, dims);
      else if (type == "class") updateLineClasses(lineView);
      else if (type == "widget") updateLineWidgets(cm, lineView, dims);
    }
    lineView.changes = null;
  }

  // Lines with gutter elements, widgets or a background class need to
  // be wrapped, and have the extra elements added to the wrapper div
  function ensureLineWrapped(lineView) {
    if (lineView.node == lineView.text) {
      lineView.node = elt("div", null, null, "position: relative");
      if (lineView.text.parentNode)
        lineView.text.parentNode.replaceChild(lineView.node, lineView.text);
      lineView.node.appendChild(lineView.text);
      if (ie && ie_version < 8) lineView.node.style.zIndex = 2;
    }
    return lineView.node;
  }

  function updateLineBackground(lineView) {
    var cls = lineView.bgClass ? lineView.bgClass + " " + (lineView.line.bgClass || "") : lineView.line.bgClass;
    if (cls) cls += " CodeMirror-linebackground";
    if (lineView.background) {
      if (cls) lineView.background.className = cls;
      else { lineView.background.parentNode.removeChild(lineView.background); lineView.background = null; }
    } else if (cls) {
      var wrap = ensureLineWrapped(lineView);
      lineView.background = wrap.insertBefore(elt("div", null, cls), wrap.firstChild);
    }
  }

  // Wrapper around buildLineContent which will reuse the structure
  // in display.externalMeasured when possible.
  function getLineContent(cm, lineView) {
    var ext = cm.display.externalMeasured;
    if (ext && ext.line == lineView.line) {
      cm.display.externalMeasured = null;
      lineView.measure = ext.measure;
      return ext.built;
    }
    return buildLineContent(cm, lineView);
  }

  // Redraw the line's text. Interacts with the background and text
  // classes because the mode may output tokens that influence these
  // classes.
  function updateLineText(cm, lineView) {
    var cls = lineView.text.className;
    var built = getLineContent(cm, lineView);
    if (lineView.text == lineView.node) lineView.node = built.pre;
    lineView.text.parentNode.replaceChild(built.pre, lineView.text);
    lineView.text = built.pre;
    if (built.bgClass != lineView.bgClass || built.textClass != lineView.textClass) {
      lineView.bgClass = built.bgClass;
      lineView.textClass = built.textClass;
      updateLineClasses(lineView);
    } else if (cls) {
      lineView.text.className = cls;
    }
  }

  function updateLineClasses(lineView) {
    updateLineBackground(lineView);
    if (lineView.line.wrapClass)
      ensureLineWrapped(lineView).className = lineView.line.wrapClass;
    else if (lineView.node != lineView.text)
      lineView.node.className = "";
    var textClass = lineView.textClass ? lineView.textClass + " " + (lineView.line.textClass || "") : lineView.line.textClass;
    lineView.text.className = textClass || "";
  }

  function updateLineGutter(cm, lineView, lineN, dims) {
    if (lineView.gutter) {
      lineView.node.removeChild(lineView.gutter);
      lineView.gutter = null;
    }
    var markers = lineView.line.gutterMarkers;
    if (cm.options.lineNumbers || markers) {
      var wrap = ensureLineWrapped(lineView);
      var gutterWrap = lineView.gutter = elt("div", null, "CodeMirror-gutter-wrapper", "left: " +
                                             (cm.options.fixedGutter ? dims.fixedPos : -dims.gutterTotalWidth) +
                                             "px; width: " + dims.gutterTotalWidth + "px");
      cm.display.input.setUneditable(gutterWrap);
      wrap.insertBefore(gutterWrap, lineView.text);
      if (lineView.line.gutterClass)
        gutterWrap.className += " " + lineView.line.gutterClass;
      if (cm.options.lineNumbers && (!markers || !markers["CodeMirror-linenumbers"]))
        lineView.lineNumber = gutterWrap.appendChild(
          elt("div", lineNumberFor(cm.options, lineN),
              "CodeMirror-linenumber CodeMirror-gutter-elt",
              "left: " + dims.gutterLeft["CodeMirror-linenumbers"] + "px; width: "
              + cm.display.lineNumInnerWidth + "px"));
      if (markers) for (var k = 0; k < cm.options.gutters.length; ++k) {
        var id = cm.options.gutters[k], found = markers.hasOwnProperty(id) && markers[id];
        if (found)
          gutterWrap.appendChild(elt("div", [found], "CodeMirror-gutter-elt", "left: " +
                                     dims.gutterLeft[id] + "px; width: " + dims.gutterWidth[id] + "px"));
      }
    }
  }

  function updateLineWidgets(cm, lineView, dims) {
    if (lineView.alignable) lineView.alignable = null;
    for (var node = lineView.node.firstChild, next; node; node = next) {
      var next = node.nextSibling;
      if (node.className == "CodeMirror-linewidget")
        lineView.node.removeChild(node);
    }
    insertLineWidgets(cm, lineView, dims);
  }

  // Build a line's DOM representation from scratch
  function buildLineElement(cm, lineView, lineN, dims) {
    var built = getLineContent(cm, lineView);
    lineView.text = lineView.node = built.pre;
    if (built.bgClass) lineView.bgClass = built.bgClass;
    if (built.textClass) lineView.textClass = built.textClass;

    updateLineClasses(lineView);
    updateLineGutter(cm, lineView, lineN, dims);
    insertLineWidgets(cm, lineView, dims);
    return lineView.node;
  }

  // A lineView may contain multiple logical lines (when merged by
  // collapsed spans). The widgets for all of them need to be drawn.
  function insertLineWidgets(cm, lineView, dims) {
    insertLineWidgetsFor(cm, lineView.line, lineView, dims, true);
    if (lineView.rest) for (var i = 0; i < lineView.rest.length; i++)
      insertLineWidgetsFor(cm, lineView.rest[i], lineView, dims, false);
  }

  function insertLineWidgetsFor(cm, line, lineView, dims, allowAbove) {
    if (!line.widgets) return;
    var wrap = ensureLineWrapped(lineView);
    for (var i = 0, ws = line.widgets; i < ws.length; ++i) {
      var widget = ws[i], node = elt("div", [widget.node], "CodeMirror-linewidget");
      if (!widget.handleMouseEvents) node.setAttribute("cm-ignore-events", "true");
      positionLineWidget(widget, node, lineView, dims);
      cm.display.input.setUneditable(node);
      if (allowAbove && widget.above)
        wrap.insertBefore(node, lineView.gutter || lineView.text);
      else
        wrap.appendChild(node);
      signalLater(widget, "redraw");
    }
  }

  function positionLineWidget(widget, node, lineView, dims) {
    if (widget.noHScroll) {
      (lineView.alignable || (lineView.alignable = [])).push(node);
      var width = dims.wrapperWidth;
      node.style.left = dims.fixedPos + "px";
      if (!widget.coverGutter) {
        width -= dims.gutterTotalWidth;
        node.style.paddingLeft = dims.gutterTotalWidth + "px";
      }
      node.style.width = width + "px";
    }
    if (widget.coverGutter) {
      node.style.zIndex = 5;
      node.style.position = "relative";
      if (!widget.noHScroll) node.style.marginLeft = -dims.gutterTotalWidth + "px";
    }
  }

  // POSITION OBJECT

  // A Pos instance represents a position within the text.
  var Pos = CodeMirror.Pos = function(line, ch) {
    if (!(this instanceof Pos)) return new Pos(line, ch);
    this.line = line; this.ch = ch;
  };

  // Compare two positions, return 0 if they are the same, a negative
  // number when a is less, and a positive number otherwise.
  var cmp = CodeMirror.cmpPos = function(a, b) { return a.line - b.line || a.ch - b.ch; };

  function copyPos(x) {return Pos(x.line, x.ch);}
  function maxPos(a, b) { return cmp(a, b) < 0 ? b : a; }
  function minPos(a, b) { return cmp(a, b) < 0 ? a : b; }

  // INPUT HANDLING

  function ensureFocus(cm) {
    if (!cm.state.focused) { cm.display.input.focus(); onFocus(cm); }
  }

  function isReadOnly(cm) {
    return cm.options.readOnly || cm.doc.cantEdit;
  }

  // This will be set to an array of strings when copying, so that,
  // when pasting, we know what kind of selections the copied text
  // was made out of.
  var lastCopied = null;

  function applyTextInput(cm, inserted, deleted, sel, origin) {
    var doc = cm.doc;
    cm.display.shift = false;
    if (!sel) sel = doc.sel;

    var textLines = splitLines(inserted), multiPaste = null;
    // When pasing N lines into N selections, insert one line per selection
    if (cm.state.pasteIncoming && sel.ranges.length > 1) {
      if (lastCopied && lastCopied.join("\n") == inserted)
        multiPaste = sel.ranges.length % lastCopied.length == 0 && map(lastCopied, splitLines);
      else if (textLines.length == sel.ranges.length)
        multiPaste = map(textLines, function(l) { return [l]; });
    }

    // Normal behavior is to insert the new text into every selection
    for (var i = sel.ranges.length - 1; i >= 0; i--) {
      var range = sel.ranges[i];
      var from = range.from(), to = range.to();
      if (range.empty()) {
        if (deleted && deleted > 0) // Handle deletion
          from = Pos(from.line, from.ch - deleted);
        else if (cm.state.overwrite && !cm.state.pasteIncoming) // Handle overwrite
          to = Pos(to.line, Math.min(getLine(doc, to.line).text.length, to.ch + lst(textLines).length));
      }
      var updateInput = cm.curOp.updateInput;
      var changeEvent = {from: from, to: to, text: multiPaste ? multiPaste[i % multiPaste.length] : textLines,
                         origin: origin || (cm.state.pasteIncoming ? "paste" : cm.state.cutIncoming ? "cut" : "+input")};
      makeChange(cm.doc, changeEvent);
      signalLater(cm, "inputRead", cm, changeEvent);
    }
    if (inserted && !cm.state.pasteIncoming)
      triggerElectric(cm, inserted);

    ensureCursorVisible(cm);
    cm.curOp.updateInput = updateInput;
    cm.curOp.typing = true;
    cm.state.pasteIncoming = cm.state.cutIncoming = false;
  }

  function triggerElectric(cm, inserted) {
    // When an 'electric' character is inserted, immediately trigger a reindent
    if (!cm.options.electricChars || !cm.options.smartIndent) return;
    var sel = cm.doc.sel;

    for (var i = sel.ranges.length - 1; i >= 0; i--) {
      var range = sel.ranges[i];
      if (range.head.ch > 100 || (i && sel.ranges[i - 1].head.line == range.head.line)) continue;
      var mode = cm.getModeAt(range.head);
      var indented = false;
      if (mode.electricChars) {
        for (var j = 0; j < mode.electricChars.length; j++)
          if (inserted.indexOf(mode.electricChars.charAt(j)) > -1) {
            indented = indentLine(cm, range.head.line, "smart");
            break;
          }
      } else if (mode.electricInput) {
        if (mode.electricInput.test(getLine(cm.doc, range.head.line).text.slice(0, range.head.ch)))
          indented = indentLine(cm, range.head.line, "smart");
      }
      if (indented) signalLater(cm, "electricInput", cm, range.head.line);
    }
  }

  function copyableRanges(cm) {
    var text = [], ranges = [];
    for (var i = 0; i < cm.doc.sel.ranges.length; i++) {
      var line = cm.doc.sel.ranges[i].head.line;
      var lineRange = {anchor: Pos(line, 0), head: Pos(line + 1, 0)};
      ranges.push(lineRange);
      text.push(cm.getRange(lineRange.anchor, lineRange.head));
    }
    return {text: text, ranges: ranges};
  }

  function disableBrowserMagic(field) {
    field.setAttribute("autocorrect", "off");
    field.setAttribute("autocapitalize", "off");
    field.setAttribute("spellcheck", "false");
  }

  // TEXTAREA INPUT STYLE

  function TextareaInput(cm) {
    this.cm = cm;
    // See input.poll and input.reset
    this.prevInput = "";

    // Flag that indicates whether we expect input to appear real soon
    // now (after some event like 'keypress' or 'input') and are
    // polling intensively.
    this.pollingFast = false;
    // Self-resetting timeout for the poller
    this.polling = new Delayed();
    // Tracks when input.reset has punted to just putting a short
    // string into the textarea instead of the full selection.
    this.inaccurateSelection = false;
    // Used to work around IE issue with selection being forgotten when focus moves away from textarea
    this.hasSelection = false;
    this.composing = null;
  };

  function hiddenTextarea() {
    var te = elt("textarea", null, null, "position: absolute; padding: 0; width: 1px; height: 1em; outline: none");
    var div = elt("div", [te], null, "overflow: hidden; position: relative; width: 3px; height: 0px;");
    // The textarea is kept positioned near the cursor to prevent the
    // fact that it'll be scrolled into view on input from scrolling
    // our fake cursor out of view. On webkit, when wrap=off, paste is
    // very slow. So make the area wide instead.
    if (webkit) te.style.width = "1000px";
    else te.setAttribute("wrap", "off");
    // If border: 0; -- iOS fails to open keyboard (issue #1287)
    if (ios) te.style.border = "1px solid black";
    disableBrowserMagic(te);
    return div;
  }

  TextareaInput.prototype = copyObj({
    init: function(display) {
      var input = this, cm = this.cm;

      // Wraps and hides input textarea
      var div = this.wrapper = hiddenTextarea();
      // The semihidden textarea that is focused when the editor is
      // focused, and receives input.
      var te = this.textarea = div.firstChild;
      display.wrapper.insertBefore(div, display.wrapper.firstChild);

      // Needed to hide big blue blinking cursor on Mobile Safari (doesn't seem to work in iOS 8 anymore)
      if (ios) te.style.width = "0px";

      on(te, "input", function() {
        if (ie && ie_version >= 9 && input.hasSelection) input.hasSelection = null;
        input.poll();
      });

      on(te, "paste", function() {
        // Workaround for webkit bug https://bugs.webkit.org/show_bug.cgi?id=90206
        // Add a char to the end of textarea before paste occur so that
        // selection doesn't span to the end of textarea.
        if (webkit && !cm.state.fakedLastChar && !(new Date - cm.state.lastMiddleDown < 200)) {
          var start = te.selectionStart, end = te.selectionEnd;
          te.value += "$";
          // The selection end needs to be set before the start, otherwise there
          // can be an intermediate non-empty selection between the two, which
          // can override the middle-click paste buffer on linux and cause the
          // wrong thing to get pasted.
          te.selectionEnd = end;
          te.selectionStart = start;
          cm.state.fakedLastChar = true;
        }
        cm.state.pasteIncoming = true;
        input.fastPoll();
      });

      function prepareCopyCut(e) {
        if (cm.somethingSelected()) {
          lastCopied = cm.getSelections();
          if (input.inaccurateSelection) {
            input.prevInput = "";
            input.inaccurateSelection = false;
            te.value = lastCopied.join("\n");
            selectInput(te);
          }
        } else if (!cm.options.lineWiseCopyCut) {
          return;
        } else {
          var ranges = copyableRanges(cm);
          lastCopied = ranges.text;
          if (e.type == "cut") {
            cm.setSelections(ranges.ranges, null, sel_dontScroll);
          } else {
            input.prevInput = "";
            te.value = ranges.text.join("\n");
            selectInput(te);
          }
        }
        if (e.type == "cut") cm.state.cutIncoming = true;
      }
      on(te, "cut", prepareCopyCut);
      on(te, "copy", prepareCopyCut);

      on(display.scroller, "paste", function(e) {
        if (eventInWidget(display, e)) return;
        cm.state.pasteIncoming = true;
        input.focus();
      });

      // Prevent normal selection in the editor (we handle our own)
      on(display.lineSpace, "selectstart", function(e) {
        if (!eventInWidget(display, e)) e_preventDefault(e);
      });

      on(te, "compositionstart", function() {
        var start = cm.getCursor("from");
        input.composing = {
          start: start,
          range: cm.markText(start, cm.getCursor("to"), {className: "CodeMirror-composing"})
        };
      });
      on(te, "compositionend", function() {
        if (input.composing) {
          input.poll();
          input.composing.range.clear();
          input.composing = null;
        }
      });
    },

    prepareSelection: function() {
      // Redraw the selection and/or cursor
      var cm = this.cm, display = cm.display, doc = cm.doc;
      var result = prepareSelection(cm);

      // Move the hidden textarea near the cursor to prevent scrolling artifacts
      if (cm.options.moveInputWithCursor) {
        var headPos = cursorCoords(cm, doc.sel.primary().head, "div");
        var wrapOff = display.wrapper.getBoundingClientRect(), lineOff = display.lineDiv.getBoundingClientRect();
        result.teTop = Math.max(0, Math.min(display.wrapper.clientHeight - 10,
                                            headPos.top + lineOff.top - wrapOff.top));
        result.teLeft = Math.max(0, Math.min(display.wrapper.clientWidth - 10,
                                             headPos.left + lineOff.left - wrapOff.left));
      }

      return result;
    },

    showSelection: function(drawn) {
      var cm = this.cm, display = cm.display;
      removeChildrenAndAdd(display.cursorDiv, drawn.cursors);
      removeChildrenAndAdd(display.selectionDiv, drawn.selection);
      if (drawn.teTop != null) {
        this.wrapper.style.top = drawn.teTop + "px";
        this.wrapper.style.left = drawn.teLeft + "px";
      }
    },

    // Reset the input to correspond to the selection (or to be empty,
    // when not typing and nothing is selected)
    reset: function(typing) {
      if (this.contextMenuPending) return;
      var minimal, selected, cm = this.cm, doc = cm.doc;
      if (cm.somethingSelected()) {
        this.prevInput = "";
        var range = doc.sel.primary();
        minimal = hasCopyEvent &&
          (range.to().line - range.from().line > 100 || (selected = cm.getSelection()).length > 1000);
        var content = minimal ? "-" : selected || cm.getSelection();
        this.textarea.value = content;
        if (cm.state.focused) selectInput(this.textarea);
        if (ie && ie_version >= 9) this.hasSelection = content;
      } else if (!typing) {
        this.prevInput = this.textarea.value = "";
        if (ie && ie_version >= 9) this.hasSelection = null;
      }
      this.inaccurateSelection = minimal;
    },

    getField: function() { return this.textarea; },

    supportsTouch: function() { return false; },

    focus: function() {
      if (this.cm.options.readOnly != "nocursor" && (!mobile || activeElt() != this.textarea)) {
        try { this.textarea.focus(); }
        catch (e) {} // IE8 will throw if the textarea is display: none or not in DOM
      }
    },

    blur: function() { this.textarea.blur(); },

    resetPosition: function() {
      this.wrapper.style.top = this.wrapper.style.left = 0;
    },

    receivedFocus: function() { this.slowPoll(); },

    // Poll for input changes, using the normal rate of polling. This
    // runs as long as the editor is focused.
    slowPoll: function() {
      var input = this;
      if (input.pollingFast) return;
      input.polling.set(this.cm.options.pollInterval, function() {
        input.poll();
        if (input.cm.state.focused) input.slowPoll();
      });
    },

    // When an event has just come in that is likely to add or change
    // something in the input textarea, we poll faster, to ensure that
    // the change appears on the screen quickly.
    fastPoll: function() {
      var missed = false, input = this;
      input.pollingFast = true;
      function p() {
        var changed = input.poll();
        if (!changed && !missed) {missed = true; input.polling.set(60, p);}
        else {input.pollingFast = false; input.slowPoll();}
      }
      input.polling.set(20, p);
    },

    // Read input from the textarea, and update the document to match.
    // When something is selected, it is present in the textarea, and
    // selected (unless it is huge, in which case a placeholder is
    // used). When nothing is selected, the cursor sits after previously
    // seen text (can be empty), which is stored in prevInput (we must
    // not reset the textarea when typing, because that breaks IME).
    poll: function() {
      var cm = this.cm, input = this.textarea, prevInput = this.prevInput;
      // Since this is called a *lot*, try to bail out as cheaply as
      // possible when it is clear that nothing happened. hasSelection
      // will be the case when there is a lot of text in the textarea,
      // in which case reading its value would be expensive.
      if (!cm.state.focused || (hasSelection(input) && !prevInput) ||
          isReadOnly(cm) || cm.options.disableInput || cm.state.keySeq)
        return false;
      // See paste handler for more on the fakedLastChar kludge
      if (cm.state.pasteIncoming && cm.state.fakedLastChar) {
        input.value = input.value.substring(0, input.value.length - 1);
        cm.state.fakedLastChar = false;
      }
      var text = input.value;
      // If nothing changed, bail.
      if (text == prevInput && !cm.somethingSelected()) return false;
      // Work around nonsensical selection resetting in IE9/10, and
      // inexplicable appearance of private area unicode characters on
      // some key combos in Mac (#2689).
      if (ie && ie_version >= 9 && this.hasSelection === text ||
          mac && /[\uf700-\uf7ff]/.test(text)) {
        cm.display.input.reset();
        return false;
      }

      if (cm.doc.sel == cm.display.selForContextMenu) {
        var first = text.charCodeAt(0);
        if (first == 0x200b && !prevInput) prevInput = "\u200b";
        if (first == 0x21da) { this.reset(); return this.cm.execCommand("undo"); }
      }
      // Find the part of the input that is actually new
      var same = 0, l = Math.min(prevInput.length, text.length);
      while (same < l && prevInput.charCodeAt(same) == text.charCodeAt(same)) ++same;

      var self = this;
      runInOp(cm, function() {
        applyTextInput(cm, text.slice(same), prevInput.length - same,
                       null, self.composing ? "*compose" : null);

        // Don't leave long text in the textarea, since it makes further polling slow
        if (text.length > 1000 || text.indexOf("\n") > -1) input.value = self.prevInput = "";
        else self.prevInput = text;

        if (self.composing) {
          self.composing.range.clear();
          self.composing.range = cm.markText(self.composing.start, cm.getCursor("to"),
                                             {className: "CodeMirror-composing"});
        }
      });
      return true;
    },

    ensurePolled: function() {
      if (this.pollingFast && this.poll()) this.pollingFast = false;
    },

    onKeyPress: function() {
      if (ie && ie_version >= 9) this.hasSelection = null;
      this.fastPoll();
    },

    onContextMenu: function(e) {
      var input = this, cm = input.cm, display = cm.display, te = input.textarea;
      var pos = posFromMouse(cm, e), scrollPos = display.scroller.scrollTop;
      if (!pos || presto) return; // Opera is difficult.

      // Reset the current text selection only if the click is done outside of the selection
      // and 'resetSelectionOnContextMenu' option is true.
      var reset = cm.options.resetSelectionOnContextMenu;
      if (reset && cm.doc.sel.contains(pos) == -1)
        operation(cm, setSelection)(cm.doc, simpleSelection(pos), sel_dontScroll);

      var oldCSS = te.style.cssText;
      input.wrapper.style.position = "absolute";
      te.style.cssText = "position: fixed; width: 30px; height: 30px; top: " + (e.clientY - 5) +
        "px; left: " + (e.clientX - 5) + "px; z-index: 1000; background: " +
        (ie ? "rgba(255, 255, 255, .05)" : "transparent") +
        "; outline: none; border-width: 0; outline: none; overflow: hidden; opacity: .05; filter: alpha(opacity=5);";
      if (webkit) var oldScrollY = window.scrollY; // Work around Chrome issue (#2712)
      display.input.focus();
      if (webkit) window.scrollTo(null, oldScrollY);
      display.input.reset();
      // Adds "Select all" to context menu in FF
      if (!cm.somethingSelected()) te.value = input.prevInput = " ";
      input.contextMenuPending = true;
      display.selForContextMenu = cm.doc.sel;
      clearTimeout(display.detectingSelectAll);

      // Select-all will be greyed out if there's nothing to select, so
      // this adds a zero-width space so that we can later check whether
      // it got selected.
      function prepareSelectAllHack() {
        if (te.selectionStart != null) {
          var selected = cm.somethingSelected();
          var extval = "\u200b" + (selected ? te.value : "");
          te.value = "\u21da"; // Used to catch context-menu undo
          te.value = extval;
          input.prevInput = selected ? "" : "\u200b";
          te.selectionStart = 1; te.selectionEnd = extval.length;
          // Re-set this, in case some other handler touched the
          // selection in the meantime.
          display.selForContextMenu = cm.doc.sel;
        }
      }
      function rehide() {
        input.contextMenuPending = false;
        input.wrapper.style.position = "relative";
        te.style.cssText = oldCSS;
        if (ie && ie_version < 9) display.scrollbars.setScrollTop(display.scroller.scrollTop = scrollPos);

        // Try to detect the user choosing select-all
        if (te.selectionStart != null) {
          if (!ie || (ie && ie_version < 9)) prepareSelectAllHack();
          var i = 0, poll = function() {
            if (display.selForContextMenu == cm.doc.sel && te.selectionStart == 0 &&
                te.selectionEnd > 0 && input.prevInput == "\u200b")
              operation(cm, commands.selectAll)(cm);
            else if (i++ < 10) display.detectingSelectAll = setTimeout(poll, 500);
            else display.input.reset();
          };
          display.detectingSelectAll = setTimeout(poll, 200);
        }
      }

      if (ie && ie_version >= 9) prepareSelectAllHack();
      if (captureRightClick) {
        e_stop(e);
        var mouseup = function() {
          off(window, "mouseup", mouseup);
          setTimeout(rehide, 20);
        };
        on(window, "mouseup", mouseup);
      } else {
        setTimeout(rehide, 50);
      }
    },

    setUneditable: nothing,

    needsContentAttribute: false
  }, TextareaInput.prototype);

  // CONTENTEDITABLE INPUT STYLE

  function ContentEditableInput(cm) {
    this.cm = cm;
    this.lastAnchorNode = this.lastAnchorOffset = this.lastFocusNode = this.lastFocusOffset = null;
    this.polling = new Delayed();
    this.gracePeriod = false;
  }

  ContentEditableInput.prototype = copyObj({
    init: function(display) {
      var input = this, cm = input.cm;
      var div = input.div = display.lineDiv;
      div.contentEditable = "true";
      disableBrowserMagic(div);

      on(div, "paste", function(e) {
        var pasted = e.clipboardData && e.clipboardData.getData("text/plain");
        if (pasted) {
          e.preventDefault();
          cm.replaceSelection(pasted, null, "paste");
        }
      });

      on(div, "compositionstart", function(e) {
        var data = e.data;
        input.composing = {sel: cm.doc.sel, data: data, startData: data};
        if (!data) return;
        var prim = cm.doc.sel.primary();
        var line = cm.getLine(prim.head.line);
        var found = line.indexOf(data, Math.max(0, prim.head.ch - data.length));
        if (found > -1 && found <= prim.head.ch)
          input.composing.sel = simpleSelection(Pos(prim.head.line, found),
                                                Pos(prim.head.line, found + data.length));
      });
      on(div, "compositionupdate", function(e) {
        input.composing.data = e.data;
      });
      on(div, "compositionend", function(e) {
        var ours = input.composing;
        if (!ours) return;
        if (e.data != ours.startData && !/\u200b/.test(e.data))
          ours.data = e.data;
        // Need a small delay to prevent other code (input event,
        // selection polling) from doing damage when fired right after
        // compositionend.
        setTimeout(function() {
          if (!ours.handled)
            input.applyComposition(ours);
          if (input.composing == ours)
            input.composing = null;
        }, 50);
      });

      on(div, "touchstart", function() {
        input.forceCompositionEnd();
      });

      on(div, "input", function() {
        if (input.composing) return;
        if (!input.pollContent())
          runInOp(input.cm, function() {regChange(cm);});
      });

      function onCopyCut(e) {
        if (cm.somethingSelected()) {
          lastCopied = cm.getSelections();
          if (e.type == "cut") cm.replaceSelection("", null, "cut");
        } else if (!cm.options.lineWiseCopyCut) {
          return;
        } else {
          var ranges = copyableRanges(cm);
          lastCopied = ranges.text;
          if (e.type == "cut") {
            cm.operation(function() {
              cm.setSelections(ranges.ranges, 0, sel_dontScroll);
              cm.replaceSelection("", null, "cut");
            });
          }
        }
        // iOS exposes the clipboard API, but seems to discard content inserted into it
        if (e.clipboardData && !ios) {
          e.preventDefault();
          e.clipboardData.clearData();
          e.clipboardData.setData("text/plain", lastCopied.join("\n"));
        } else {
          // Old-fashioned briefly-focus-a-textarea hack
          var kludge = hiddenTextarea(), te = kludge.firstChild;
          cm.display.lineSpace.insertBefore(kludge, cm.display.lineSpace.firstChild);
          te.value = lastCopied.join("\n");
          var hadFocus = document.activeElement;
          selectInput(te);
          setTimeout(function() {
            cm.display.lineSpace.removeChild(kludge);
            hadFocus.focus();
          }, 50);
        }
      }
      on(div, "copy", onCopyCut);
      on(div, "cut", onCopyCut);
    },

    prepareSelection: function() {
      var result = prepareSelection(this.cm, false);
      result.focus = this.cm.state.focused;
      return result;
    },

    showSelection: function(info) {
      if (!info || !this.cm.display.view.length) return;
      if (info.focus) this.showPrimarySelection();
      this.showMultipleSelections(info);
    },

    showPrimarySelection: function() {
      var sel = window.getSelection(), prim = this.cm.doc.sel.primary();
      var curAnchor = domToPos(this.cm, sel.anchorNode, sel.anchorOffset);
      var curFocus = domToPos(this.cm, sel.focusNode, sel.focusOffset);
      if (curAnchor && !curAnchor.bad && curFocus && !curFocus.bad &&
          cmp(minPos(curAnchor, curFocus), prim.from()) == 0 &&
          cmp(maxPos(curAnchor, curFocus), prim.to()) == 0)
        return;

      var start = posToDOM(this.cm, prim.from());
      var end = posToDOM(this.cm, prim.to());
      if (!start && !end) return;

      var view = this.cm.display.view;
      var old = sel.rangeCount && sel.getRangeAt(0);
      if (!start) {
        start = {node: view[0].measure.map[2], offset: 0};
      } else if (!end) { // FIXME dangerously hacky
        var measure = view[view.length - 1].measure;
        var map = measure.maps ? measure.maps[measure.maps.length - 1] : measure.map;
        end = {node: map[map.length - 1], offset: map[map.length - 2] - map[map.length - 3]};
      }

      try { var rng = range(start.node, start.offset, end.offset, end.node); }
      catch(e) {} // Our model of the DOM might be outdated, in which case the range we try to set can be impossible
      if (rng) {
        sel.removeAllRanges();
        sel.addRange(rng);
        if (old && sel.anchorNode == null) sel.addRange(old);
        else if (gecko) this.startGracePeriod();
      }
      this.rememberSelection();
    },

    startGracePeriod: function() {
      var input = this;
      clearTimeout(this.gracePeriod);
      this.gracePeriod = setTimeout(function() {
        input.gracePeriod = false;
        if (input.selectionChanged())
          input.cm.operation(function() { input.cm.curOp.selectionChanged = true; });
      }, 20);
    },

    showMultipleSelections: function(info) {
      removeChildrenAndAdd(this.cm.display.cursorDiv, info.cursors);
      removeChildrenAndAdd(this.cm.display.selectionDiv, info.selection);
    },

    rememberSelection: function() {
      var sel = window.getSelection();
      this.lastAnchorNode = sel.anchorNode; this.lastAnchorOffset = sel.anchorOffset;
      this.lastFocusNode = sel.focusNode; this.lastFocusOffset = sel.focusOffset;
    },

    selectionInEditor: function() {
      var sel = window.getSelection();
      if (!sel.rangeCount) return false;
      var node = sel.getRangeAt(0).commonAncestorContainer;
      return contains(this.div, node);
    },

    focus: function() {
      if (this.cm.options.readOnly != "nocursor") this.div.focus();
    },
    blur: function() { this.div.blur(); },
    getField: function() { return this.div; },

    supportsTouch: function() { return true; },

    receivedFocus: function() {
      var input = this;
      if (this.selectionInEditor())
        this.pollSelection();
      else
        runInOp(this.cm, function() { input.cm.curOp.selectionChanged = true; });

      function poll() {
        if (input.cm.state.focused) {
          input.pollSelection();
          input.polling.set(input.cm.options.pollInterval, poll);
        }
      }
      this.polling.set(this.cm.options.pollInterval, poll);
    },

    selectionChanged: function() {
      var sel = window.getSelection();
      return sel.anchorNode != this.lastAnchorNode || sel.anchorOffset != this.lastAnchorOffset ||
        sel.focusNode != this.lastFocusNode || sel.focusOffset != this.lastFocusOffset;
    },

    pollSelection: function() {
      if (!this.composing && !this.gracePeriod && this.selectionChanged()) {
        var sel = window.getSelection(), cm = this.cm;
        this.rememberSelection();
        var anchor = domToPos(cm, sel.anchorNode, sel.anchorOffset);
        var head = domToPos(cm, sel.focusNode, sel.focusOffset);
        if (anchor && head) runInOp(cm, function() {
          setSelection(cm.doc, simpleSelection(anchor, head), sel_dontScroll);
          if (anchor.bad || head.bad) cm.curOp.selectionChanged = true;
        });
      }
    },

    pollContent: function() {
      var cm = this.cm, display = cm.display, sel = cm.doc.sel.primary();
      var from = sel.from(), to = sel.to();
      if (from.line < display.viewFrom || to.line > display.viewTo - 1) return false;

      var fromIndex;
      if (from.line == display.viewFrom || (fromIndex = findViewIndex(cm, from.line)) == 0) {
        var fromLine = lineNo(display.view[0].line);
        var fromNode = display.view[0].node;
      } else {
        var fromLine = lineNo(display.view[fromIndex].line);
        var fromNode = display.view[fromIndex - 1].node.nextSibling;
      }
      var toIndex = findViewIndex(cm, to.line);
      if (toIndex == display.view.length - 1) {
        var toLine = display.viewTo - 1;
        var toNode = display.view[toIndex].node;
      } else {
        var toLine = lineNo(display.view[toIndex + 1].line) - 1;
        var toNode = display.view[toIndex + 1].node.previousSibling;
      }

      var newText = splitLines(domTextBetween(cm, fromNode, toNode, fromLine, toLine));
      var oldText = getBetween(cm.doc, Pos(fromLine, 0), Pos(toLine, getLine(cm.doc, toLine).text.length));
      while (newText.length > 1 && oldText.length > 1) {
        if (lst(newText) == lst(oldText)) { newText.pop(); oldText.pop(); toLine--; }
        else if (newText[0] == oldText[0]) { newText.shift(); oldText.shift(); fromLine++; }
        else break;
      }

      var cutFront = 0, cutEnd = 0;
      var newTop = newText[0], oldTop = oldText[0], maxCutFront = Math.min(newTop.length, oldTop.length);
      while (cutFront < maxCutFront && newTop.charCodeAt(cutFront) == oldTop.charCodeAt(cutFront))
        ++cutFront;
      var newBot = lst(newText), oldBot = lst(oldText);
      var maxCutEnd = Math.min(newBot.length - (newText.length == 1 ? cutFront : 0),
                               oldBot.length - (oldText.length == 1 ? cutFront : 0));
      while (cutEnd < maxCutEnd &&
             newBot.charCodeAt(newBot.length - cutEnd - 1) == oldBot.charCodeAt(oldBot.length - cutEnd - 1))
        ++cutEnd;

      newText[newText.length - 1] = newBot.slice(0, newBot.length - cutEnd);
      newText[0] = newText[0].slice(cutFront);

      var chFrom = Pos(fromLine, cutFront);
      var chTo = Pos(toLine, oldText.length ? lst(oldText).length - cutEnd : 0);
      if (newText.length > 1 || newText[0] || cmp(chFrom, chTo)) {
        replaceRange(cm.doc, newText, chFrom, chTo, "+input");
        return true;
      }
    },

    ensurePolled: function() {
      this.forceCompositionEnd();
    },
    reset: function() {
      this.forceCompositionEnd();
    },
    forceCompositionEnd: function() {
      if (!this.composing || this.composing.handled) return;
      this.applyComposition(this.composing);
      this.composing.handled = true;
      this.div.blur();
      this.div.focus();
    },
    applyComposition: function(composing) {
      if (composing.data && composing.data != composing.startData)
        operation(this.cm, applyTextInput)(this.cm, composing.data, 0, composing.sel);
    },

    setUneditable: function(node) {
      node.setAttribute("contenteditable", "false");
    },

    onKeyPress: function(e) {
      e.preventDefault();
      operation(this.cm, applyTextInput)(this.cm, String.fromCharCode(e.charCode == null ? e.keyCode : e.charCode), 0);
    },

    onContextMenu: nothing,
    resetPosition: nothing,

    needsContentAttribute: true
  }, ContentEditableInput.prototype);

  function posToDOM(cm, pos) {
    var view = findViewForLine(cm, pos.line);
    if (!view || view.hidden) return null;
    var line = getLine(cm.doc, pos.line);
    var info = mapFromLineView(view, line, pos.line);

    var order = getOrder(line), side = "left";
    if (order) {
      var partPos = getBidiPartAt(order, pos.ch);
      side = partPos % 2 ? "right" : "left";
    }
    var result = nodeAndOffsetInLineMap(info.map, pos.ch, side);
    result.offset = result.collapse == "right" ? result.end : result.start;
    return result;
  }

  function badPos(pos, bad) { if (bad) pos.bad = true; return pos; }

  function domToPos(cm, node, offset) {
    var lineNode;
    if (node == cm.display.lineDiv) {
      lineNode = cm.display.lineDiv.childNodes[offset];
      if (!lineNode) return badPos(cm.clipPos(Pos(cm.display.viewTo - 1)), true);
      node = null; offset = 0;
    } else {
      for (lineNode = node;; lineNode = lineNode.parentNode) {
        if (!lineNode || lineNode == cm.display.lineDiv) return null;
        if (lineNode.parentNode && lineNode.parentNode == cm.display.lineDiv) break;
      }
    }
    for (var i = 0; i < cm.display.view.length; i++) {
      var lineView = cm.display.view[i];
      if (lineView.node == lineNode)
        return locateNodeInLineView(lineView, node, offset);
    }
  }

  function locateNodeInLineView(lineView, node, offset) {
    var wrapper = lineView.text.firstChild, bad = false;
    if (!node || !contains(wrapper, node)) return badPos(Pos(lineNo(lineView.line), 0), true);
    if (node == wrapper) {
      bad = true;
      node = wrapper.childNodes[offset];
      offset = 0;
      if (!node) {
        var line = lineView.rest ? lst(lineView.rest) : lineView.line;
        return badPos(Pos(lineNo(line), line.text.length), bad);
      }
    }

    var textNode = node.nodeType == 3 ? node : null, topNode = node;
    if (!textNode && node.childNodes.length == 1 && node.firstChild.nodeType == 3) {
      textNode = node.firstChild;
      if (offset) offset = textNode.nodeValue.length;
    }
    while (topNode.parentNode != wrapper) topNode = topNode.parentNode;
    var measure = lineView.measure, maps = measure.maps;

    function find(textNode, topNode, offset) {
      for (var i = -1; i < (maps ? maps.length : 0); i++) {
        var map = i < 0 ? measure.map : maps[i];
        for (var j = 0; j < map.length; j += 3) {
          var curNode = map[j + 2];
          if (curNode == textNode || curNode == topNode) {
            var line = lineNo(i < 0 ? lineView.line : lineView.rest[i]);
            var ch = map[j] + offset;
            if (offset < 0 || curNode != textNode) ch = map[j + (offset ? 1 : 0)];
            return Pos(line, ch);
          }
        }
      }
    }
    var found = find(textNode, topNode, offset);
    if (found) return badPos(found, bad);

    // FIXME this is all really shaky. might handle the few cases it needs to handle, but likely to cause problems
    for (var after = topNode.nextSibling, dist = textNode ? textNode.nodeValue.length - offset : 0; after; after = after.nextSibling) {
      found = find(after, after.firstChild, 0);
      if (found)
        return badPos(Pos(found.line, found.ch - dist), bad);
      else
        dist += after.textContent.length;
    }
    for (var before = topNode.previousSibling, dist = offset; before; before = before.previousSibling) {
      found = find(before, before.firstChild, -1);
      if (found)
        return badPos(Pos(found.line, found.ch + dist), bad);
      else
        dist += after.textContent.length;
    }
  }

  function domTextBetween(cm, from, to, fromLine, toLine) {
    var text = "", closing = false;
    function recognizeMarker(id) { return function(marker) { return marker.id == id; }; }
    function walk(node) {
      if (node.nodeType == 1) {
        var cmText = node.getAttribute("cm-text");
        if (cmText != null) {
          if (cmText == "") cmText = node.textContent.replace(/\u200b/g, "");
          text += cmText;
          return;
        }
        var markerID = node.getAttribute("cm-marker"), range;
        if (markerID) {
          var found = cm.findMarks(Pos(fromLine, 0), Pos(toLine + 1, 0), recognizeMarker(+markerID));
          if (found.length && (range = found[0].find()))
            text += getBetween(cm.doc, range.from, range.to).join("\n");
          return;
        }
        if (node.getAttribute("contenteditable") == "false") return;
        for (var i = 0; i < node.childNodes.length; i++)
          walk(node.childNodes[i]);
        if (/^(pre|div|p)$/i.test(node.nodeName))
          closing = true;
      } else if (node.nodeType == 3) {
        var val = node.nodeValue;
        if (!val) return;
        if (closing) {
          text += "\n";
          closing = false;
        }
        text += val;
      }
    }
    for (;;) {
      walk(from);
      if (from == to) break;
      from = from.nextSibling;
    }
    return text;
  }

  CodeMirror.inputStyles = {"textarea": TextareaInput, "contenteditable": ContentEditableInput};

  // SELECTION / CURSOR

  // Selection objects are immutable. A new one is created every time
  // the selection changes. A selection is one or more non-overlapping
  // (and non-touching) ranges, sorted, and an integer that indicates
  // which one is the primary selection (the one that's scrolled into
  // view, that getCursor returns, etc).
  function Selection(ranges, primIndex) {
    this.ranges = ranges;
    this.primIndex = primIndex;
  }

  Selection.prototype = {
    primary: function() { return this.ranges[this.primIndex]; },
    equals: function(other) {
      if (other == this) return true;
      if (other.primIndex != this.primIndex || other.ranges.length != this.ranges.length) return false;
      for (var i = 0; i < this.ranges.length; i++) {
        var here = this.ranges[i], there = other.ranges[i];
        if (cmp(here.anchor, there.anchor) != 0 || cmp(here.head, there.head) != 0) return false;
      }
      return true;
    },
    deepCopy: function() {
      for (var out = [], i = 0; i < this.ranges.length; i++)
        out[i] = new Range(copyPos(this.ranges[i].anchor), copyPos(this.ranges[i].head));
      return new Selection(out, this.primIndex);
    },
    somethingSelected: function() {
      for (var i = 0; i < this.ranges.length; i++)
        if (!this.ranges[i].empty()) return true;
      return false;
    },
    contains: function(pos, end) {
      if (!end) end = pos;
      for (var i = 0; i < this.ranges.length; i++) {
        var range = this.ranges[i];
        if (cmp(end, range.from()) >= 0 && cmp(pos, range.to()) <= 0)
          return i;
      }
      return -1;
    }
  };

  function Range(anchor, head) {
    this.anchor = anchor; this.head = head;
  }

  Range.prototype = {
    from: function() { return minPos(this.anchor, this.head); },
    to: function() { return maxPos(this.anchor, this.head); },
    empty: function() {
      return this.head.line == this.anchor.line && this.head.ch == this.anchor.ch;
    }
  };

  // Take an unsorted, potentially overlapping set of ranges, and
  // build a selection out of it. 'Consumes' ranges array (modifying
  // it).
  function normalizeSelection(ranges, primIndex) {
    var prim = ranges[primIndex];
    ranges.sort(function(a, b) { return cmp(a.from(), b.from()); });
    primIndex = indexOf(ranges, prim);
    for (var i = 1; i < ranges.length; i++) {
      var cur = ranges[i], prev = ranges[i - 1];
      if (cmp(prev.to(), cur.from()) >= 0) {
        var from = minPos(prev.from(), cur.from()), to = maxPos(prev.to(), cur.to());
        var inv = prev.empty() ? cur.from() == cur.head : prev.from() == prev.head;
        if (i <= primIndex) --primIndex;
        ranges.splice(--i, 2, new Range(inv ? to : from, inv ? from : to));
      }
    }
    return new Selection(ranges, primIndex);
  }

  function simpleSelection(anchor, head) {
    return new Selection([new Range(anchor, head || anchor)], 0);
  }

  // Most of the external API clips given positions to make sure they
  // actually exist within the document.
  function clipLine(doc, n) {return Math.max(doc.first, Math.min(n, doc.first + doc.size - 1));}
  function clipPos(doc, pos) {
    if (pos.line < doc.first) return Pos(doc.first, 0);
    var last = doc.first + doc.size - 1;
    if (pos.line > last) return Pos(last, getLine(doc, last).text.length);
    return clipToLen(pos, getLine(doc, pos.line).text.length);
  }
  function clipToLen(pos, linelen) {
    var ch = pos.ch;
    if (ch == null || ch > linelen) return Pos(pos.line, linelen);
    else if (ch < 0) return Pos(pos.line, 0);
    else return pos;
  }
  function isLine(doc, l) {return l >= doc.first && l < doc.first + doc.size;}
  function clipPosArray(doc, array) {
    for (var out = [], i = 0; i < array.length; i++) out[i] = clipPos(doc, array[i]);
    return out;
  }

  // SELECTION UPDATES

  // The 'scroll' parameter given to many of these indicated whether
  // the new cursor position should be scrolled into view after
  // modifying the selection.

  // If shift is held or the extend flag is set, extends a range to
  // include a given position (and optionally a second position).
  // Otherwise, simply returns the range between the given positions.
  // Used for cursor motion and such.
  function extendRange(doc, range, head, other) {
    if (doc.cm && doc.cm.display.shift || doc.extend) {
      var anchor = range.anchor;
      if (other) {
        var posBefore = cmp(head, anchor) < 0;
        if (posBefore != (cmp(other, anchor) < 0)) {
          anchor = head;
          head = other;
        } else if (posBefore != (cmp(head, other) < 0)) {
          head = other;
        }
      }
      return new Range(anchor, head);
    } else {
      return new Range(other || head, head);
    }
  }

  // Extend the primary selection range, discard the rest.
  function extendSelection(doc, head, other, options) {
    setSelection(doc, new Selection([extendRange(doc, doc.sel.primary(), head, other)], 0), options);
  }

  // Extend all selections (pos is an array of selections with length
  // equal the number of selections)
  function extendSelections(doc, heads, options) {
    for (var out = [], i = 0; i < doc.sel.ranges.length; i++)
      out[i] = extendRange(doc, doc.sel.ranges[i], heads[i], null);
    var newSel = normalizeSelection(out, doc.sel.primIndex);
    setSelection(doc, newSel, options);
  }

  // Updates a single range in the selection.
  function replaceOneSelection(doc, i, range, options) {
    var ranges = doc.sel.ranges.slice(0);
    ranges[i] = range;
    setSelection(doc, normalizeSelection(ranges, doc.sel.primIndex), options);
  }

  // Reset the selection to a single range.
  function setSimpleSelection(doc, anchor, head, options) {
    setSelection(doc, simpleSelection(anchor, head), options);
  }

  // Give beforeSelectionChange handlers a change to influence a
  // selection update.
  function filterSelectionChange(doc, sel) {
    var obj = {
      ranges: sel.ranges,
      update: function(ranges) {
        this.ranges = [];
        for (var i = 0; i < ranges.length; i++)
          this.ranges[i] = new Range(clipPos(doc, ranges[i].anchor),
                                     clipPos(doc, ranges[i].head));
      }
    };
    signal(doc, "beforeSelectionChange", doc, obj);
    if (doc.cm) signal(doc.cm, "beforeSelectionChange", doc.cm, obj);
    if (obj.ranges != sel.ranges) return normalizeSelection(obj.ranges, obj.ranges.length - 1);
    else return sel;
  }

  function setSelectionReplaceHistory(doc, sel, options) {
    var done = doc.history.done, last = lst(done);
    if (last && last.ranges) {
      done[done.length - 1] = sel;
      setSelectionNoUndo(doc, sel, options);
    } else {
      setSelection(doc, sel, options);
    }
  }

  // Set a new selection.
  function setSelection(doc, sel, options) {
    setSelectionNoUndo(doc, sel, options);
    addSelectionToHistory(doc, doc.sel, doc.cm ? doc.cm.curOp.id : NaN, options);
  }

  function setSelectionNoUndo(doc, sel, options) {
    if (hasHandler(doc, "beforeSelectionChange") || doc.cm && hasHandler(doc.cm, "beforeSelectionChange"))
      sel = filterSelectionChange(doc, sel);

    var bias = options && options.bias ||
      (cmp(sel.primary().head, doc.sel.primary().head) < 0 ? -1 : 1);
    setSelectionInner(doc, skipAtomicInSelection(doc, sel, bias, true));

    if (!(options && options.scroll === false) && doc.cm)
      ensureCursorVisible(doc.cm);
  }

  function setSelectionInner(doc, sel) {
    if (sel.equals(doc.sel)) return;

    doc.sel = sel;

    if (doc.cm) {
      doc.cm.curOp.updateInput = doc.cm.curOp.selectionChanged = true;
      signalCursorActivity(doc.cm);
    }
    signalLater(doc, "cursorActivity", doc);
  }

  // Verify that the selection does not partially select any atomic
  // marked ranges.
  function reCheckSelection(doc) {
    setSelectionInner(doc, skipAtomicInSelection(doc, doc.sel, null, false), sel_dontScroll);
  }

  // Return a selection that does not partially select any atomic
  // ranges.
  function skipAtomicInSelection(doc, sel, bias, mayClear) {
    var out;
    for (var i = 0; i < sel.ranges.length; i++) {
      var range = sel.ranges[i];
      var newAnchor = skipAtomic(doc, range.anchor, bias, mayClear);
      var newHead = skipAtomic(doc, range.head, bias, mayClear);
      if (out || newAnchor != range.anchor || newHead != range.head) {
        if (!out) out = sel.ranges.slice(0, i);
        out[i] = new Range(newAnchor, newHead);
      }
    }
    return out ? normalizeSelection(out, sel.primIndex) : sel;
  }

  // Ensure a given position is not inside an atomic range.
  function skipAtomic(doc, pos, bias, mayClear) {
    var flipped = false, curPos = pos;
    var dir = bias || 1;
    doc.cantEdit = false;
    search: for (;;) {
      var line = getLine(doc, curPos.line);
      if (line.markedSpans) {
        for (var i = 0; i < line.markedSpans.length; ++i) {
          var sp = line.markedSpans[i], m = sp.marker;
          if ((sp.from == null || (m.inclusiveLeft ? sp.from <= curPos.ch : sp.from < curPos.ch)) &&
              (sp.to == null || (m.inclusiveRight ? sp.to >= curPos.ch : sp.to > curPos.ch))) {
            if (mayClear) {
              signal(m, "beforeCursorEnter");
              if (m.explicitlyCleared) {
                if (!line.markedSpans) break;
                else {--i; continue;}
              }
            }
            if (!m.atomic) continue;
            var newPos = m.find(dir < 0 ? -1 : 1);
            if (cmp(newPos, curPos) == 0) {
              newPos.ch += dir;
              if (newPos.ch < 0) {
                if (newPos.line > doc.first) newPos = clipPos(doc, Pos(newPos.line - 1));
                else newPos = null;
              } else if (newPos.ch > line.text.length) {
                if (newPos.line < doc.first + doc.size - 1) newPos = Pos(newPos.line + 1, 0);
                else newPos = null;
              }
              if (!newPos) {
                if (flipped) {
                  // Driven in a corner -- no valid cursor position found at all
                  // -- try again *with* clearing, if we didn't already
                  if (!mayClear) return skipAtomic(doc, pos, bias, true);
                  // Otherwise, turn off editing until further notice, and return the start of the doc
                  doc.cantEdit = true;
                  return Pos(doc.first, 0);
                }
                flipped = true; newPos = pos; dir = -dir;
              }
            }
            curPos = newPos;
            continue search;
          }
        }
      }
      return curPos;
    }
  }

  // SELECTION DRAWING

  function updateSelection(cm) {
    cm.display.input.showSelection(cm.display.input.prepareSelection());
  }

  function prepareSelection(cm, primary) {
    var doc = cm.doc, result = {};
    var curFragment = result.cursors = document.createDocumentFragment();
    var selFragment = result.selection = document.createDocumentFragment();

    for (var i = 0; i < doc.sel.ranges.length; i++) {
      if (primary === false && i == doc.sel.primIndex) continue;
      var range = doc.sel.ranges[i];
      var collapsed = range.empty();
      if (collapsed || cm.options.showCursorWhenSelecting)
        drawSelectionCursor(cm, range, curFragment);
      if (!collapsed)
        drawSelectionRange(cm, range, selFragment);
    }
    return result;
  }

  // Draws a cursor for the given range
  function drawSelectionCursor(cm, range, output) {
    var pos = cursorCoords(cm, range.head, "div", null, null, !cm.options.singleCursorHeightPerLine);

    var cursor = output.appendChild(elt("div", "\u00a0", "CodeMirror-cursor"));
    cursor.style.left = pos.left + "px";
    cursor.style.top = pos.top + "px";
    cursor.style.height = Math.max(0, pos.bottom - pos.top) * cm.options.cursorHeight + "px";

    if (pos.other) {
      // Secondary cursor, shown when on a 'jump' in bi-directional text
      var otherCursor = output.appendChild(elt("div", "\u00a0", "CodeMirror-cursor CodeMirror-secondarycursor"));
      otherCursor.style.display = "";
      otherCursor.style.left = pos.other.left + "px";
      otherCursor.style.top = pos.other.top + "px";
      otherCursor.style.height = (pos.other.bottom - pos.other.top) * .85 + "px";
    }
  }

  // Draws the given range as a highlighted selection
  function drawSelectionRange(cm, range, output) {
    var display = cm.display, doc = cm.doc;
    var fragment = document.createDocumentFragment();
    var padding = paddingH(cm.display), leftSide = padding.left;
    var rightSide = Math.max(display.sizerWidth, displayWidth(cm) - display.sizer.offsetLeft) - padding.right;

    function add(left, top, width, bottom) {
      if (top < 0) top = 0;
      top = Math.round(top);
      bottom = Math.round(bottom);
      fragment.appendChild(elt("div", null, "CodeMirror-selected", "position: absolute; left: " + left +
                               "px; top: " + top + "px; width: " + (width == null ? rightSide - left : width) +
                               "px; height: " + (bottom - top) + "px"));
    }

    function drawForLine(line, fromArg, toArg) {
      var lineObj = getLine(doc, line);
      var lineLen = lineObj.text.length;
      var start, end;
      function coords(ch, bias) {
        return charCoords(cm, Pos(line, ch), "div", lineObj, bias);
      }

      iterateBidiSections(getOrder(lineObj), fromArg || 0, toArg == null ? lineLen : toArg, function(from, to, dir) {
        var leftPos = coords(from, "left"), rightPos, left, right;
        if (from == to) {
          rightPos = leftPos;
          left = right = leftPos.left;
        } else {
          rightPos = coords(to - 1, "right");
          if (dir == "rtl") { var tmp = leftPos; leftPos = rightPos; rightPos = tmp; }
          left = leftPos.left;
          right = rightPos.right;
        }
        if (fromArg == null && from == 0) left = leftSide;
        if (rightPos.top - leftPos.top > 3) { // Different lines, draw top part
          add(left, leftPos.top, null, leftPos.bottom);
          left = leftSide;
          if (leftPos.bottom < rightPos.top) add(left, leftPos.bottom, null, rightPos.top);
        }
        if (toArg == null && to == lineLen) right = rightSide;
        if (!start || leftPos.top < start.top || leftPos.top == start.top && leftPos.left < start.left)
          start = leftPos;
        if (!end || rightPos.bottom > end.bottom || rightPos.bottom == end.bottom && rightPos.right > end.right)
          end = rightPos;
        if (left < leftSide + 1) left = leftSide;
        add(left, rightPos.top, right - left, rightPos.bottom);
      });
      return {start: start, end: end};
    }

    var sFrom = range.from(), sTo = range.to();
    if (sFrom.line == sTo.line) {
      drawForLine(sFrom.line, sFrom.ch, sTo.ch);
    } else {
      var fromLine = getLine(doc, sFrom.line), toLine = getLine(doc, sTo.line);
      var singleVLine = visualLine(fromLine) == visualLine(toLine);
      var leftEnd = drawForLine(sFrom.line, sFrom.ch, singleVLine ? fromLine.text.length + 1 : null).end;
      var rightStart = drawForLine(sTo.line, singleVLine ? 0 : null, sTo.ch).start;
      if (singleVLine) {
        if (leftEnd.top < rightStart.top - 2) {
          add(leftEnd.right, leftEnd.top, null, leftEnd.bottom);
          add(leftSide, rightStart.top, rightStart.left, rightStart.bottom);
        } else {
          add(leftEnd.right, leftEnd.top, rightStart.left - leftEnd.right, leftEnd.bottom);
        }
      }
      if (leftEnd.bottom < rightStart.top)
        add(leftSide, leftEnd.bottom, null, rightStart.top);
    }

    output.appendChild(fragment);
  }

  // Cursor-blinking
  function restartBlink(cm) {
    if (!cm.state.focused) return;
    var display = cm.display;
    clearInterval(display.blinker);
    var on = true;
    display.cursorDiv.style.visibility = "";
    if (cm.options.cursorBlinkRate > 0)
      display.blinker = setInterval(function() {
        display.cursorDiv.style.visibility = (on = !on) ? "" : "hidden";
      }, cm.options.cursorBlinkRate);
    else if (cm.options.cursorBlinkRate < 0)
      display.cursorDiv.style.visibility = "hidden";
  }

  // HIGHLIGHT WORKER

  function startWorker(cm, time) {
    if (cm.doc.mode.startState && cm.doc.frontier < cm.display.viewTo)
      cm.state.highlight.set(time, bind(highlightWorker, cm));
  }

  function highlightWorker(cm) {
    var doc = cm.doc;
    if (doc.frontier < doc.first) doc.frontier = doc.first;
    if (doc.frontier >= cm.display.viewTo) return;
    var end = +new Date + cm.options.workTime;
    var state = copyState(doc.mode, getStateBefore(cm, doc.frontier));
    var changedLines = [];

    doc.iter(doc.frontier, Math.min(doc.first + doc.size, cm.display.viewTo + 500), function(line) {
      if (doc.frontier >= cm.display.viewFrom) { // Visible
        var oldStyles = line.styles;
        var highlighted = highlightLine(cm, line, state, true);
        line.styles = highlighted.styles;
        var oldCls = line.styleClasses, newCls = highlighted.classes;
        if (newCls) line.styleClasses = newCls;
        else if (oldCls) line.styleClasses = null;
        var ischange = !oldStyles || oldStyles.length != line.styles.length ||
          oldCls != newCls && (!oldCls || !newCls || oldCls.bgClass != newCls.bgClass || oldCls.textClass != newCls.textClass);
        for (var i = 0; !ischange && i < oldStyles.length; ++i) ischange = oldStyles[i] != line.styles[i];
        if (ischange) changedLines.push(doc.frontier);
        line.stateAfter = copyState(doc.mode, state);
      } else {
        processLine(cm, line.text, state);
        line.stateAfter = doc.frontier % 5 == 0 ? copyState(doc.mode, state) : null;
      }
      ++doc.frontier;
      if (+new Date > end) {
        startWorker(cm, cm.options.workDelay);
        return true;
      }
    });
    if (changedLines.length) runInOp(cm, function() {
      for (var i = 0; i < changedLines.length; i++)
        regLineChange(cm, changedLines[i], "text");
    });
  }

  // Finds the line to start with when starting a parse. Tries to
  // find a line with a stateAfter, so that it can start with a
  // valid state. If that fails, it returns the line with the
  // smallest indentation, which tends to need the least context to
  // parse correctly.
  function findStartLine(cm, n, precise) {
    var minindent, minline, doc = cm.doc;
    var lim = precise ? -1 : n - (cm.doc.mode.innerMode ? 1000 : 100);
    for (var search = n; search > lim; --search) {
      if (search <= doc.first) return doc.first;
      var line = getLine(doc, search - 1);
      if (line.stateAfter && (!precise || search <= doc.frontier)) return search;
      var indented = countColumn(line.text, null, cm.options.tabSize);
      if (minline == null || minindent > indented) {
        minline = search - 1;
        minindent = indented;
      }
    }
    return minline;
  }

  function getStateBefore(cm, n, precise) {
    var doc = cm.doc, display = cm.display;
    if (!doc.mode.startState) return true;
    var pos = findStartLine(cm, n, precise), state = pos > doc.first && getLine(doc, pos-1).stateAfter;
    if (!state) state = startState(doc.mode);
    else state = copyState(doc.mode, state);
    doc.iter(pos, n, function(line) {
      processLine(cm, line.text, state);
      var save = pos == n - 1 || pos % 5 == 0 || pos >= display.viewFrom && pos < display.viewTo;
      line.stateAfter = save ? copyState(doc.mode, state) : null;
      ++pos;
    });
    if (precise) doc.frontier = pos;
    return state;
  }

  // POSITION MEASUREMENT

  function paddingTop(display) {return display.lineSpace.offsetTop;}
  function paddingVert(display) {return display.mover.offsetHeight - display.lineSpace.offsetHeight;}
  function paddingH(display) {
    if (display.cachedPaddingH) return display.cachedPaddingH;
    var e = removeChildrenAndAdd(display.measure, elt("pre", "x"));
    var style = window.getComputedStyle ? window.getComputedStyle(e) : e.currentStyle;
    var data = {left: parseInt(style.paddingLeft), right: parseInt(style.paddingRight)};
    if (!isNaN(data.left) && !isNaN(data.right)) display.cachedPaddingH = data;
    return data;
  }

  function scrollGap(cm) { return scrollerGap - cm.display.nativeBarWidth; }
  function displayWidth(cm) {
    return cm.display.scroller.clientWidth - scrollGap(cm) - cm.display.barWidth;
  }
  function displayHeight(cm) {
    return cm.display.scroller.clientHeight - scrollGap(cm) - cm.display.barHeight;
  }

  // Ensure the lineView.wrapping.heights array is populated. This is
  // an array of bottom offsets for the lines that make up a drawn
  // line. When lineWrapping is on, there might be more than one
  // height.
  function ensureLineHeights(cm, lineView, rect) {
    var wrapping = cm.options.lineWrapping;
    var curWidth = wrapping && displayWidth(cm);
    if (!lineView.measure.heights || wrapping && lineView.measure.width != curWidth) {
      var heights = lineView.measure.heights = [];
      if (wrapping) {
        lineView.measure.width = curWidth;
        var rects = lineView.text.firstChild.getClientRects();
        for (var i = 0; i < rects.length - 1; i++) {
          var cur = rects[i], next = rects[i + 1];
          if (Math.abs(cur.bottom - next.bottom) > 2)
            heights.push((cur.bottom + next.top) / 2 - rect.top);
        }
      }
      heights.push(rect.bottom - rect.top);
    }
  }

  // Find a line map (mapping character offsets to text nodes) and a
  // measurement cache for the given line number. (A line view might
  // contain multiple lines when collapsed ranges are present.)
  function mapFromLineView(lineView, line, lineN) {
    if (lineView.line == line)
      return {map: lineView.measure.map, cache: lineView.measure.cache};
    for (var i = 0; i < lineView.rest.length; i++)
      if (lineView.rest[i] == line)
        return {map: lineView.measure.maps[i], cache: lineView.measure.caches[i]};
    for (var i = 0; i < lineView.rest.length; i++)
      if (lineNo(lineView.rest[i]) > lineN)
        return {map: lineView.measure.maps[i], cache: lineView.measure.caches[i], before: true};
  }

  // Render a line into the hidden node display.externalMeasured. Used
  // when measurement is needed for a line that's not in the viewport.
  function updateExternalMeasurement(cm, line) {
    line = visualLine(line);
    var lineN = lineNo(line);
    var view = cm.display.externalMeasured = new LineView(cm.doc, line, lineN);
    view.lineN = lineN;
    var built = view.built = buildLineContent(cm, view);
    view.text = built.pre;
    removeChildrenAndAdd(cm.display.lineMeasure, built.pre);
    return view;
  }

  // Get a {top, bottom, left, right} box (in line-local coordinates)
  // for a given character.
  function measureChar(cm, line, ch, bias) {
    return measureCharPrepared(cm, prepareMeasureForLine(cm, line), ch, bias);
  }

  // Find a line view that corresponds to the given line number.
  function findViewForLine(cm, lineN) {
    if (lineN >= cm.display.viewFrom && lineN < cm.display.viewTo)
      return cm.display.view[findViewIndex(cm, lineN)];
    var ext = cm.display.externalMeasured;
    if (ext && lineN >= ext.lineN && lineN < ext.lineN + ext.size)
      return ext;
  }

  // Measurement can be split in two steps, the set-up work that
  // applies to the whole line, and the measurement of the actual
  // character. Functions like coordsChar, that need to do a lot of
  // measurements in a row, can thus ensure that the set-up work is
  // only done once.
  function prepareMeasureForLine(cm, line) {
    var lineN = lineNo(line);
    var view = findViewForLine(cm, lineN);
    if (view && !view.text)
      view = null;
    else if (view && view.changes)
      updateLineForChanges(cm, view, lineN, getDimensions(cm));
    if (!view)
      view = updateExternalMeasurement(cm, line);

    var info = mapFromLineView(view, line, lineN);
    return {
      line: line, view: view, rect: null,
      map: info.map, cache: info.cache, before: info.before,
      hasHeights: false
    };
  }

  // Given a prepared measurement object, measures the position of an
  // actual character (or fetches it from the cache).
  function measureCharPrepared(cm, prepared, ch, bias, varHeight) {
    if (prepared.before) ch = -1;
    var key = ch + (bias || ""), found;
    if (prepared.cache.hasOwnProperty(key)) {
      found = prepared.cache[key];
    } else {
      if (!prepared.rect)
        prepared.rect = prepared.view.text.getBoundingClientRect();
      if (!prepared.hasHeights) {
        ensureLineHeights(cm, prepared.view, prepared.rect);
        prepared.hasHeights = true;
      }
      found = measureCharInner(cm, prepared, ch, bias);
      if (!found.bogus) prepared.cache[key] = found;
    }
    return {left: found.left, right: found.right,
            top: varHeight ? found.rtop : found.top,
            bottom: varHeight ? found.rbottom : found.bottom};
  }

  var nullRect = {left: 0, right: 0, top: 0, bottom: 0};

  function nodeAndOffsetInLineMap(map, ch, bias) {
    var node, start, end, collapse;
    // First, search the line map for the text node corresponding to,
    // or closest to, the target character.
    for (var i = 0; i < map.length; i += 3) {
      var mStart = map[i], mEnd = map[i + 1];
      if (ch < mStart) {
        start = 0; end = 1;
        collapse = "left";
      } else if (ch < mEnd) {
        start = ch - mStart;
        end = start + 1;
      } else if (i == map.length - 3 || ch == mEnd && map[i + 3] > ch) {
        end = mEnd - mStart;
        start = end - 1;
        if (ch >= mEnd) collapse = "right";
      }
      if (start != null) {
        node = map[i + 2];
        if (mStart == mEnd && bias == (node.insertLeft ? "left" : "right"))
          collapse = bias;
        if (bias == "left" && start == 0)
          while (i && map[i - 2] == map[i - 3] && map[i - 1].insertLeft) {
            node = map[(i -= 3) + 2];
            collapse = "left";
          }
        if (bias == "right" && start == mEnd - mStart)
          while (i < map.length - 3 && map[i + 3] == map[i + 4] && !map[i + 5].insertLeft) {
            node = map[(i += 3) + 2];
            collapse = "right";
          }
        break;
      }
    }
    return {node: node, start: start, end: end, collapse: collapse, coverStart: mStart, coverEnd: mEnd};
  }

  function measureCharInner(cm, prepared, ch, bias) {
    var place = nodeAndOffsetInLineMap(prepared.map, ch, bias);
    var node = place.node, start = place.start, end = place.end, collapse = place.collapse;

    var rect;
    if (node.nodeType == 3) { // If it is a text node, use a range to retrieve the coordinates.
      for (var i = 0; i < 4; i++) { // Retry a maximum of 4 times when nonsense rectangles are returned
        while (start && isExtendingChar(prepared.line.text.charAt(place.coverStart + start))) --start;
        while (place.coverStart + end < place.coverEnd && isExtendingChar(prepared.line.text.charAt(place.coverStart + end))) ++end;
        if (ie && ie_version < 9 && start == 0 && end == place.coverEnd - place.coverStart) {
          rect = node.parentNode.getBoundingClientRect();
        } else if (ie && cm.options.lineWrapping) {
          var rects = range(node, start, end).getClientRects();
          if (rects.length)
            rect = rects[bias == "right" ? rects.length - 1 : 0];
          else
            rect = nullRect;
        } else {
          rect = range(node, start, end).getBoundingClientRect() || nullRect;
        }
        if (rect.left || rect.right || start == 0) break;
        end = start;
        start = start - 1;
        collapse = "right";
      }
      if (ie && ie_version < 11) rect = maybeUpdateRectForZooming(cm.display.measure, rect);
    } else { // If it is a widget, simply get the box for the whole widget.
      if (start > 0) collapse = bias = "right";
      var rects;
      if (cm.options.lineWrapping && (rects = node.getClientRects()).length > 1)
        rect = rects[bias == "right" ? rects.length - 1 : 0];
      else
        rect = node.getBoundingClientRect();
    }
    if (ie && ie_version < 9 && !start && (!rect || !rect.left && !rect.right)) {
      var rSpan = node.parentNode.getClientRects()[0];
      if (rSpan)
        rect = {left: rSpan.left, right: rSpan.left + charWidth(cm.display), top: rSpan.top, bottom: rSpan.bottom};
      else
        rect = nullRect;
    }

    var rtop = rect.top - prepared.rect.top, rbot = rect.bottom - prepared.rect.top;
    var mid = (rtop + rbot) / 2;
    var heights = prepared.view.measure.heights;
    for (var i = 0; i < heights.length - 1; i++)
      if (mid < heights[i]) break;
    var top = i ? heights[i - 1] : 0, bot = heights[i];
    var result = {left: (collapse == "right" ? rect.right : rect.left) - prepared.rect.left,
                  right: (collapse == "left" ? rect.left : rect.right) - prepared.rect.left,
                  top: top, bottom: bot};
    if (!rect.left && !rect.right) result.bogus = true;
    if (!cm.options.singleCursorHeightPerLine) { result.rtop = rtop; result.rbottom = rbot; }

    return result;
  }

  // Work around problem with bounding client rects on ranges being
  // returned incorrectly when zoomed on IE10 and below.
  function maybeUpdateRectForZooming(measure, rect) {
    if (!window.screen || screen.logicalXDPI == null ||
        screen.logicalXDPI == screen.deviceXDPI || !hasBadZoomedRects(measure))
      return rect;
    var scaleX = screen.logicalXDPI / screen.deviceXDPI;
    var scaleY = screen.logicalYDPI / screen.deviceYDPI;
    return {left: rect.left * scaleX, right: rect.right * scaleX,
            top: rect.top * scaleY, bottom: rect.bottom * scaleY};
  }

  function clearLineMeasurementCacheFor(lineView) {
    if (lineView.measure) {
      lineView.measure.cache = {};
      lineView.measure.heights = null;
      if (lineView.rest) for (var i = 0; i < lineView.rest.length; i++)
        lineView.measure.caches[i] = {};
    }
  }

  function clearLineMeasurementCache(cm) {
    cm.display.externalMeasure = null;
    removeChildren(cm.display.lineMeasure);
    for (var i = 0; i < cm.display.view.length; i++)
      clearLineMeasurementCacheFor(cm.display.view[i]);
  }

  function clearCaches(cm) {
    clearLineMeasurementCache(cm);
    cm.display.cachedCharWidth = cm.display.cachedTextHeight = cm.display.cachedPaddingH = null;
    if (!cm.options.lineWrapping) cm.display.maxLineChanged = true;
    cm.display.lineNumChars = null;
  }

  function pageScrollX() { return window.pageXOffset || (document.documentElement || document.body).scrollLeft; }
  function pageScrollY() { return window.pageYOffset || (document.documentElement || document.body).scrollTop; }

  // Converts a {top, bottom, left, right} box from line-local
  // coordinates into another coordinate system. Context may be one of
  // "line", "div" (display.lineDiv), "local"/null (editor), "window",
  // or "page".
  function intoCoordSystem(cm, lineObj, rect, context) {
    if (lineObj.widgets) for (var i = 0; i < lineObj.widgets.length; ++i) if (lineObj.widgets[i].above) {
      var size = widgetHeight(lineObj.widgets[i]);
      rect.top += size; rect.bottom += size;
    }
    if (context == "line") return rect;
    if (!context) context = "local";
    var yOff = heightAtLine(lineObj);
    if (context == "local") yOff += paddingTop(cm.display);
    else yOff -= cm.display.viewOffset;
    if (context == "page" || context == "window") {
      var lOff = cm.display.lineSpace.getBoundingClientRect();
      yOff += lOff.top + (context == "window" ? 0 : pageScrollY());
      var xOff = lOff.left + (context == "window" ? 0 : pageScrollX());
      rect.left += xOff; rect.right += xOff;
    }
    rect.top += yOff; rect.bottom += yOff;
    return rect;
  }

  // Coverts a box from "div" coords to another coordinate system.
  // Context may be "window", "page", "div", or "local"/null.
  function fromCoordSystem(cm, coords, context) {
    if (context == "div") return coords;
    var left = coords.left, top = coords.top;
    // First move into "page" coordinate system
    if (context == "page") {
      left -= pageScrollX();
      top -= pageScrollY();
    } else if (context == "local" || !context) {
      var localBox = cm.display.sizer.getBoundingClientRect();
      left += localBox.left;
      top += localBox.top;
    }

    var lineSpaceBox = cm.display.lineSpace.getBoundingClientRect();
    return {left: left - lineSpaceBox.left, top: top - lineSpaceBox.top};
  }

  function charCoords(cm, pos, context, lineObj, bias) {
    if (!lineObj) lineObj = getLine(cm.doc, pos.line);
    return intoCoordSystem(cm, lineObj, measureChar(cm, lineObj, pos.ch, bias), context);
  }

  // Returns a box for a given cursor position, which may have an
  // 'other' property containing the position of the secondary cursor
  // on a bidi boundary.
  function cursorCoords(cm, pos, context, lineObj, preparedMeasure, varHeight) {
    lineObj = lineObj || getLine(cm.doc, pos.line);
    if (!preparedMeasure) preparedMeasure = prepareMeasureForLine(cm, lineObj);
    function get(ch, right) {
      var m = measureCharPrepared(cm, preparedMeasure, ch, right ? "right" : "left", varHeight);
      if (right) m.left = m.right; else m.right = m.left;
      return intoCoordSystem(cm, lineObj, m, context);
    }
    function getBidi(ch, partPos) {
      var part = order[partPos], right = part.level % 2;
      if (ch == bidiLeft(part) && partPos && part.level < order[partPos - 1].level) {
        part = order[--partPos];
        ch = bidiRight(part) - (part.level % 2 ? 0 : 1);
        right = true;
      } else if (ch == bidiRight(part) && partPos < order.length - 1 && part.level < order[partPos + 1].level) {
        part = order[++partPos];
        ch = bidiLeft(part) - part.level % 2;
        right = false;
      }
      if (right && ch == part.to && ch > part.from) return get(ch - 1);
      return get(ch, right);
    }
    var order = getOrder(lineObj), ch = pos.ch;
    if (!order) return get(ch);
    var partPos = getBidiPartAt(order, ch);
    var val = getBidi(ch, partPos);
    if (bidiOther != null) val.other = getBidi(ch, bidiOther);
    return val;
  }

  // Used to cheaply estimate the coordinates for a position. Used for
  // intermediate scroll updates.
  function estimateCoords(cm, pos) {
    var left = 0, pos = clipPos(cm.doc, pos);
    if (!cm.options.lineWrapping) left = charWidth(cm.display) * pos.ch;
    var lineObj = getLine(cm.doc, pos.line);
    var top = heightAtLine(lineObj) + paddingTop(cm.display);
    return {left: left, right: left, top: top, bottom: top + lineObj.height};
  }

  // Positions returned by coordsChar contain some extra information.
  // xRel is the relative x position of the input coordinates compared
  // to the found position (so xRel > 0 means the coordinates are to
  // the right of the character position, for example). When outside
  // is true, that means the coordinates lie outside the line's
  // vertical range.
  function PosWithInfo(line, ch, outside, xRel) {
    var pos = Pos(line, ch);
    pos.xRel = xRel;
    if (outside) pos.outside = true;
    return pos;
  }

  // Compute the character position closest to the given coordinates.
  // Input must be lineSpace-local ("div" coordinate system).
  function coordsChar(cm, x, y) {
    var doc = cm.doc;
    y += cm.display.viewOffset;
    if (y < 0) return PosWithInfo(doc.first, 0, true, -1);
    var lineN = lineAtHeight(doc, y), last = doc.first + doc.size - 1;
    if (lineN > last)
      return PosWithInfo(doc.first + doc.size - 1, getLine(doc, last).text.length, true, 1);
    if (x < 0) x = 0;

    var lineObj = getLine(doc, lineN);
    for (;;) {
      var found = coordsCharInner(cm, lineObj, lineN, x, y);
      var merged = collapsedSpanAtEnd(lineObj);
      var mergedPos = merged && merged.find(0, true);
      if (merged && (found.ch > mergedPos.from.ch || found.ch == mergedPos.from.ch && found.xRel > 0))
        lineN = lineNo(lineObj = mergedPos.to.line);
      else
        return found;
    }
  }

  function coordsCharInner(cm, lineObj, lineNo, x, y) {
    var innerOff = y - heightAtLine(lineObj);
    var wrongLine = false, adjust = 2 * cm.display.wrapper.clientWidth;
    var preparedMeasure = prepareMeasureForLine(cm, lineObj);

    function getX(ch) {
      var sp = cursorCoords(cm, Pos(lineNo, ch), "line", lineObj, preparedMeasure);
      wrongLine = true;
      if (innerOff > sp.bottom) return sp.left - adjust;
      else if (innerOff < sp.top) return sp.left + adjust;
      else wrongLine = false;
      return sp.left;
    }

    var bidi = getOrder(lineObj), dist = lineObj.text.length;
    var from = lineLeft(lineObj), to = lineRight(lineObj);
    var fromX = getX(from), fromOutside = wrongLine, toX = getX(to), toOutside = wrongLine;

    if (x > toX) return PosWithInfo(lineNo, to, toOutside, 1);
    // Do a binary search between these bounds.
    for (;;) {
      if (bidi ? to == from || to == moveVisually(lineObj, from, 1) : to - from <= 1) {
        var ch = x < fromX || x - fromX <= toX - x ? from : to;
        var xDiff = x - (ch == from ? fromX : toX);
        while (isExtendingChar(lineObj.text.charAt(ch))) ++ch;
        var pos = PosWithInfo(lineNo, ch, ch == from ? fromOutside : toOutside,
                              xDiff < -1 ? -1 : xDiff > 1 ? 1 : 0);
        return pos;
      }
      var step = Math.ceil(dist / 2), middle = from + step;
      if (bidi) {
        middle = from;
        for (var i = 0; i < step; ++i) middle = moveVisually(lineObj, middle, 1);
      }
      var middleX = getX(middle);
      if (middleX > x) {to = middle; toX = middleX; if (toOutside = wrongLine) toX += 1000; dist = step;}
      else {from = middle; fromX = middleX; fromOutside = wrongLine; dist -= step;}
    }
  }

  var measureText;
  // Compute the default text height.
  function textHeight(display) {
    if (display.cachedTextHeight != null) return display.cachedTextHeight;
    if (measureText == null) {
      measureText = elt("pre");
      // Measure a bunch of lines, for browsers that compute
      // fractional heights.
      for (var i = 0; i < 49; ++i) {
        measureText.appendChild(document.createTextNode("x"));
        measureText.appendChild(elt("br"));
      }
      measureText.appendChild(document.createTextNode("x"));
    }
    removeChildrenAndAdd(display.measure, measureText);
    var height = measureText.offsetHeight / 50;
    if (height > 3) display.cachedTextHeight = height;
    removeChildren(display.measure);
    return height || 1;
  }

  // Compute the default character width.
  function charWidth(display) {
    if (display.cachedCharWidth != null) return display.cachedCharWidth;
    var anchor = elt("span", "xxxxxxxxxx");
    var pre = elt("pre", [anchor]);
    removeChildrenAndAdd(display.measure, pre);
    var rect = anchor.getBoundingClientRect(), width = (rect.right - rect.left) / 10;
    if (width > 2) display.cachedCharWidth = width;
    return width || 10;
  }

  // OPERATIONS

  // Operations are used to wrap a series of changes to the editor
  // state in such a way that each change won't have to update the
  // cursor and display (which would be awkward, slow, and
  // error-prone). Instead, display updates are batched and then all
  // combined and executed at once.

  var operationGroup = null;

  var nextOpId = 0;
  // Start a new operation.
  function startOperation(cm) {
    cm.curOp = {
      cm: cm,
      viewChanged: false,      // Flag that indicates that lines might need to be redrawn
      startHeight: cm.doc.height, // Used to detect need to update scrollbar
      forceUpdate: false,      // Used to force a redraw
      updateInput: null,       // Whether to reset the input textarea
      typing: false,           // Whether this reset should be careful to leave existing text (for compositing)
      changeObjs: null,        // Accumulated changes, for firing change events
      cursorActivityHandlers: null, // Set of handlers to fire cursorActivity on
      cursorActivityCalled: 0, // Tracks which cursorActivity handlers have been called already
      selectionChanged: false, // Whether the selection needs to be redrawn
      updateMaxLine: false,    // Set when the widest line needs to be determined anew
      scrollLeft: null, scrollTop: null, // Intermediate scroll position, not pushed to DOM yet
      scrollToPos: null,       // Used to scroll to a specific position
      focus: false,
      id: ++nextOpId           // Unique ID
    };
    if (operationGroup) {
      operationGroup.ops.push(cm.curOp);
    } else {
      cm.curOp.ownsGroup = operationGroup = {
        ops: [cm.curOp],
        delayedCallbacks: []
      };
    }
  }

  function fireCallbacksForOps(group) {
    // Calls delayed callbacks and cursorActivity handlers until no
    // new ones appear
    var callbacks = group.delayedCallbacks, i = 0;
    do {
      for (; i < callbacks.length; i++)
        callbacks[i]();
      for (var j = 0; j < group.ops.length; j++) {
        var op = group.ops[j];
        if (op.cursorActivityHandlers)
          while (op.cursorActivityCalled < op.cursorActivityHandlers.length)
            op.cursorActivityHandlers[op.cursorActivityCalled++](op.cm);
      }
    } while (i < callbacks.length);
  }

  // Finish an operation, updating the display and signalling delayed events
  function endOperation(cm) {
    var op = cm.curOp, group = op.ownsGroup;
    if (!group) return;

    try { fireCallbacksForOps(group); }
    finally {
      operationGroup = null;
      for (var i = 0; i < group.ops.length; i++)
        group.ops[i].cm.curOp = null;
      endOperations(group);
    }
  }

  // The DOM updates done when an operation finishes are batched so
  // that the minimum number of relayouts are required.
  function endOperations(group) {
    var ops = group.ops;
    for (var i = 0; i < ops.length; i++) // Read DOM
      endOperation_R1(ops[i]);
    for (var i = 0; i < ops.length; i++) // Write DOM (maybe)
      endOperation_W1(ops[i]);
    for (var i = 0; i < ops.length; i++) // Read DOM
      endOperation_R2(ops[i]);
    for (var i = 0; i < ops.length; i++) // Write DOM (maybe)
      endOperation_W2(ops[i]);
    for (var i = 0; i < ops.length; i++) // Read DOM
      endOperation_finish(ops[i]);
  }

  function endOperation_R1(op) {
    var cm = op.cm, display = cm.display;
    maybeClipScrollbars(cm);
    if (op.updateMaxLine) findMaxLine(cm);

    op.mustUpdate = op.viewChanged || op.forceUpdate || op.scrollTop != null ||
      op.scrollToPos && (op.scrollToPos.from.line < display.viewFrom ||
                         op.scrollToPos.to.line >= display.viewTo) ||
      display.maxLineChanged && cm.options.lineWrapping;
    op.update = op.mustUpdate &&
      new DisplayUpdate(cm, op.mustUpdate && {top: op.scrollTop, ensure: op.scrollToPos}, op.forceUpdate);
  }

  function endOperation_W1(op) {
    op.updatedDisplay = op.mustUpdate && updateDisplayIfNeeded(op.cm, op.update);
  }

  function endOperation_R2(op) {
    var cm = op.cm, display = cm.display;
    if (op.updatedDisplay) updateHeightsInViewport(cm);

    op.barMeasure = measureForScrollbars(cm);

    // If the max line changed since it was last measured, measure it,
    // and ensure the document's width matches it.
    // updateDisplay_W2 will use these properties to do the actual resizing
    if (display.maxLineChanged && !cm.options.lineWrapping) {
      op.adjustWidthTo = measureChar(cm, display.maxLine, display.maxLine.text.length).left + 3;
      cm.display.sizerWidth = op.adjustWidthTo;
      op.barMeasure.scrollWidth =
        Math.max(display.scroller.clientWidth, display.sizer.offsetLeft + op.adjustWidthTo + scrollGap(cm) + cm.display.barWidth);
      op.maxScrollLeft = Math.max(0, display.sizer.offsetLeft + op.adjustWidthTo - displayWidth(cm));
    }

    if (op.updatedDisplay || op.selectionChanged)
      op.preparedSelection = display.input.prepareSelection();
  }

  function endOperation_W2(op) {
    var cm = op.cm;

    if (op.adjustWidthTo != null) {
      cm.display.sizer.style.minWidth = op.adjustWidthTo + "px";
      if (op.maxScrollLeft < cm.doc.scrollLeft)
        setScrollLeft(cm, Math.min(cm.display.scroller.scrollLeft, op.maxScrollLeft), true);
      cm.display.maxLineChanged = false;
    }

    if (op.preparedSelection)
      cm.display.input.showSelection(op.preparedSelection);
    if (op.updatedDisplay)
      setDocumentHeight(cm, op.barMeasure);
    if (op.updatedDisplay || op.startHeight != cm.doc.height)
      updateScrollbars(cm, op.barMeasure);

    if (op.selectionChanged) restartBlink(cm);

    if (cm.state.focused && op.updateInput)
      cm.display.input.reset(op.typing);
    if (op.focus && op.focus == activeElt()) ensureFocus(op.cm);
  }

  function endOperation_finish(op) {
    var cm = op.cm, display = cm.display, doc = cm.doc;

    if (op.updatedDisplay) postUpdateDisplay(cm, op.update);

    // Abort mouse wheel delta measurement, when scrolling explicitly
    if (display.wheelStartX != null && (op.scrollTop != null || op.scrollLeft != null || op.scrollToPos))
      display.wheelStartX = display.wheelStartY = null;

    // Propagate the scroll position to the actual DOM scroller
    if (op.scrollTop != null && (display.scroller.scrollTop != op.scrollTop || op.forceScroll)) {
      doc.scrollTop = Math.max(0, Math.min(display.scroller.scrollHeight - display.scroller.clientHeight, op.scrollTop));
      display.scrollbars.setScrollTop(doc.scrollTop);
      display.scroller.scrollTop = doc.scrollTop;
    }
    if (op.scrollLeft != null && (display.scroller.scrollLeft != op.scrollLeft || op.forceScroll)) {
      doc.scrollLeft = Math.max(0, Math.min(display.scroller.scrollWidth - displayWidth(cm), op.scrollLeft));
      display.scrollbars.setScrollLeft(doc.scrollLeft);
      display.scroller.scrollLeft = doc.scrollLeft;
      alignHorizontally(cm);
    }
    // If we need to scroll a specific position into view, do so.
    if (op.scrollToPos) {
      var coords = scrollPosIntoView(cm, clipPos(doc, op.scrollToPos.from),
                                     clipPos(doc, op.scrollToPos.to), op.scrollToPos.margin);
      if (op.scrollToPos.isCursor && cm.state.focused) maybeScrollWindow(cm, coords);
    }

    // Fire events for markers that are hidden/unidden by editing or
    // undoing
    var hidden = op.maybeHiddenMarkers, unhidden = op.maybeUnhiddenMarkers;
    if (hidden) for (var i = 0; i < hidden.length; ++i)
      if (!hidden[i].lines.length) signal(hidden[i], "hide");
    if (unhidden) for (var i = 0; i < unhidden.length; ++i)
      if (unhidden[i].lines.length) signal(unhidden[i], "unhide");

    if (display.wrapper.offsetHeight)
      doc.scrollTop = cm.display.scroller.scrollTop;

    // Fire change events, and delayed event handlers
    if (op.changeObjs)
      signal(cm, "changes", cm, op.changeObjs);
    if (op.update)
      op.update.finish();
  }

  // Run the given function in an operation
  function runInOp(cm, f) {
    if (cm.curOp) return f();
    startOperation(cm);
    try { return f(); }
    finally { endOperation(cm); }
  }
  // Wraps a function in an operation. Returns the wrapped function.
  function operation(cm, f) {
    return function() {
      if (cm.curOp) return f.apply(cm, arguments);
      startOperation(cm);
      try { return f.apply(cm, arguments); }
      finally { endOperation(cm); }
    };
  }
  // Used to add methods to editor and doc instances, wrapping them in
  // operations.
  function methodOp(f) {
    return function() {
      if (this.curOp) return f.apply(this, arguments);
      startOperation(this);
      try { return f.apply(this, arguments); }
      finally { endOperation(this); }
    };
  }
  function docMethodOp(f) {
    return function() {
      var cm = this.cm;
      if (!cm || cm.curOp) return f.apply(this, arguments);
      startOperation(cm);
      try { return f.apply(this, arguments); }
      finally { endOperation(cm); }
    };
  }

  // VIEW TRACKING

  // These objects are used to represent the visible (currently drawn)
  // part of the document. A LineView may correspond to multiple
  // logical lines, if those are connected by collapsed ranges.
  function LineView(doc, line, lineN) {
    // The starting line
    this.line = line;
    // Continuing lines, if any
    this.rest = visualLineContinued(line);
    // Number of logical lines in this visual line
    this.size = this.rest ? lineNo(lst(this.rest)) - lineN + 1 : 1;
    this.node = this.text = null;
    this.hidden = lineIsHidden(doc, line);
  }

  // Create a range of LineView objects for the given lines.
  function buildViewArray(cm, from, to) {
    var array = [], nextPos;
    for (var pos = from; pos < to; pos = nextPos) {
      var view = new LineView(cm.doc, getLine(cm.doc, pos), pos);
      nextPos = pos + view.size;
      array.push(view);
    }
    return array;
  }

  // Updates the display.view data structure for a given change to the
  // document. From and to are in pre-change coordinates. Lendiff is
  // the amount of lines added or subtracted by the change. This is
  // used for changes that span multiple lines, or change the way
  // lines are divided into visual lines. regLineChange (below)
  // registers single-line changes.
  function regChange(cm, from, to, lendiff) {
    if (from == null) from = cm.doc.first;
    if (to == null) to = cm.doc.first + cm.doc.size;
    if (!lendiff) lendiff = 0;

    var display = cm.display;
    if (lendiff && to < display.viewTo &&
        (display.updateLineNumbers == null || display.updateLineNumbers > from))
      display.updateLineNumbers = from;

    cm.curOp.viewChanged = true;

    if (from >= display.viewTo) { // Change after
      if (sawCollapsedSpans && visualLineNo(cm.doc, from) < display.viewTo)
        resetView(cm);
    } else if (to <= display.viewFrom) { // Change before
      if (sawCollapsedSpans && visualLineEndNo(cm.doc, to + lendiff) > display.viewFrom) {
        resetView(cm);
      } else {
        display.viewFrom += lendiff;
        display.viewTo += lendiff;
      }
    } else if (from <= display.viewFrom && to >= display.viewTo) { // Full overlap
      resetView(cm);
    } else if (from <= display.viewFrom) { // Top overlap
      var cut = viewCuttingPoint(cm, to, to + lendiff, 1);
      if (cut) {
        display.view = display.view.slice(cut.index);
        display.viewFrom = cut.lineN;
        display.viewTo += lendiff;
      } else {
        resetView(cm);
      }
    } else if (to >= display.viewTo) { // Bottom overlap
      var cut = viewCuttingPoint(cm, from, from, -1);
      if (cut) {
        display.view = display.view.slice(0, cut.index);
        display.viewTo = cut.lineN;
      } else {
        resetView(cm);
      }
    } else { // Gap in the middle
      var cutTop = viewCuttingPoint(cm, from, from, -1);
      var cutBot = viewCuttingPoint(cm, to, to + lendiff, 1);
      if (cutTop && cutBot) {
        display.view = display.view.slice(0, cutTop.index)
          .concat(buildViewArray(cm, cutTop.lineN, cutBot.lineN))
          .concat(display.view.slice(cutBot.index));
        display.viewTo += lendiff;
      } else {
        resetView(cm);
      }
    }

    var ext = display.externalMeasured;
    if (ext) {
      if (to < ext.lineN)
        ext.lineN += lendiff;
      else if (from < ext.lineN + ext.size)
        display.externalMeasured = null;
    }
  }

  // Register a change to a single line. Type must be one of "text",
  // "gutter", "class", "widget"
  function regLineChange(cm, line, type) {
    cm.curOp.viewChanged = true;
    var display = cm.display, ext = cm.display.externalMeasured;
    if (ext && line >= ext.lineN && line < ext.lineN + ext.size)
      display.externalMeasured = null;

    if (line < display.viewFrom || line >= display.viewTo) return;
    var lineView = display.view[findViewIndex(cm, line)];
    if (lineView.node == null) return;
    var arr = lineView.changes || (lineView.changes = []);
    if (indexOf(arr, type) == -1) arr.push(type);
  }

  // Clear the view.
  function resetView(cm) {
    cm.display.viewFrom = cm.display.viewTo = cm.doc.first;
    cm.display.view = [];
    cm.display.viewOffset = 0;
  }

  // Find the view element corresponding to a given line. Return null
  // when the line isn't visible.
  function findViewIndex(cm, n) {
    if (n >= cm.display.viewTo) return null;
    n -= cm.display.viewFrom;
    if (n < 0) return null;
    var view = cm.display.view;
    for (var i = 0; i < view.length; i++) {
      n -= view[i].size;
      if (n < 0) return i;
    }
  }

  function viewCuttingPoint(cm, oldN, newN, dir) {
    var index = findViewIndex(cm, oldN), diff, view = cm.display.view;
    if (!sawCollapsedSpans || newN == cm.doc.first + cm.doc.size)
      return {index: index, lineN: newN};
    for (var i = 0, n = cm.display.viewFrom; i < index; i++)
      n += view[i].size;
    if (n != oldN) {
      if (dir > 0) {
        if (index == view.length - 1) return null;
        diff = (n + view[index].size) - oldN;
        index++;
      } else {
        diff = n - oldN;
      }
      oldN += diff; newN += diff;
    }
    while (visualLineNo(cm.doc, newN) != newN) {
      if (index == (dir < 0 ? 0 : view.length - 1)) return null;
      newN += dir * view[index - (dir < 0 ? 1 : 0)].size;
      index += dir;
    }
    return {index: index, lineN: newN};
  }

  // Force the view to cover a given range, adding empty view element
  // or clipping off existing ones as needed.
  function adjustView(cm, from, to) {
    var display = cm.display, view = display.view;
    if (view.length == 0 || from >= display.viewTo || to <= display.viewFrom) {
      display.view = buildViewArray(cm, from, to);
      display.viewFrom = from;
    } else {
      if (display.viewFrom > from)
        display.view = buildViewArray(cm, from, display.viewFrom).concat(display.view);
      else if (display.viewFrom < from)
        display.view = display.view.slice(findViewIndex(cm, from));
      display.viewFrom = from;
      if (display.viewTo < to)
        display.view = display.view.concat(buildViewArray(cm, display.viewTo, to));
      else if (display.viewTo > to)
        display.view = display.view.slice(0, findViewIndex(cm, to));
    }
    display.viewTo = to;
  }

  // Count the number of lines in the view whose DOM representation is
  // out of date (or nonexistent).
  function countDirtyView(cm) {
    var view = cm.display.view, dirty = 0;
    for (var i = 0; i < view.length; i++) {
      var lineView = view[i];
      if (!lineView.hidden && (!lineView.node || lineView.changes)) ++dirty;
    }
    return dirty;
  }

  // EVENT HANDLERS

  // Attach the necessary event handlers when initializing the editor
  function registerEventHandlers(cm) {
    var d = cm.display;
    on(d.scroller, "mousedown", operation(cm, onMouseDown));
    // Older IE's will not fire a second mousedown for a double click
    if (ie && ie_version < 11)
      on(d.scroller, "dblclick", operation(cm, function(e) {
        if (signalDOMEvent(cm, e)) return;
        var pos = posFromMouse(cm, e);
        if (!pos || clickInGutter(cm, e) || eventInWidget(cm.display, e)) return;
        e_preventDefault(e);
        var word = cm.findWordAt(pos);
        extendSelection(cm.doc, word.anchor, word.head);
      }));
    else
      on(d.scroller, "dblclick", function(e) { signalDOMEvent(cm, e) || e_preventDefault(e); });
    // Some browsers fire contextmenu *after* opening the menu, at
    // which point we can't mess with it anymore. Context menu is
    // handled in onMouseDown for these browsers.
    if (!captureRightClick) on(d.scroller, "contextmenu", function(e) {onContextMenu(cm, e);});

    // Used to suppress mouse event handling when a touch happens
    var touchFinished, prevTouch = {end: 0};
    function finishTouch() {
      if (d.activeTouch) {
        touchFinished = setTimeout(function() {d.activeTouch = null;}, 1000);
        prevTouch = d.activeTouch;
        prevTouch.end = +new Date;
      }
    };
    function isMouseLikeTouchEvent(e) {
      if (e.touches.length != 1) return false;
      var touch = e.touches[0];
      return touch.radiusX <= 1 && touch.radiusY <= 1;
    }
    function farAway(touch, other) {
      if (other.left == null) return true;
      var dx = other.left - touch.left, dy = other.top - touch.top;
      return dx * dx + dy * dy > 20 * 20;
    }
    on(d.scroller, "touchstart", function(e) {
      if (!isMouseLikeTouchEvent(e)) {
        clearTimeout(touchFinished);
        var now = +new Date;
        d.activeTouch = {start: now, moved: false,
                         prev: now - prevTouch.end <= 300 ? prevTouch : null};
        if (e.touches.length == 1) {
          d.activeTouch.left = e.touches[0].pageX;
          d.activeTouch.top = e.touches[0].pageY;
        }
      }
    });
    on(d.scroller, "touchmove", function() {
      if (d.activeTouch) d.activeTouch.moved = true;
    });
    on(d.scroller, "touchend", function(e) {
      var touch = d.activeTouch;
      if (touch && !eventInWidget(d, e) && touch.left != null &&
          !touch.moved && new Date - touch.start < 300) {
        var pos = cm.coordsChar(d.activeTouch, "page"), range;
        if (!touch.prev || farAway(touch, touch.prev)) // Single tap
          range = new Range(pos, pos);
        else if (!touch.prev.prev || farAway(touch, touch.prev.prev)) // Double tap
          range = cm.findWordAt(pos);
        else // Triple tap
          range = new Range(Pos(pos.line, 0), clipPos(cm.doc, Pos(pos.line + 1, 0)));
        cm.setSelection(range.anchor, range.head);
        cm.focus();
        e_preventDefault(e);
      }
      finishTouch();
    });
    on(d.scroller, "touchcancel", finishTouch);

    // Sync scrolling between fake scrollbars and real scrollable
    // area, ensure viewport is updated when scrolling.
    on(d.scroller, "scroll", function() {
      if (d.scroller.clientHeight) {
        setScrollTop(cm, d.scroller.scrollTop);
        setScrollLeft(cm, d.scroller.scrollLeft, true);
        signal(cm, "scroll", cm);
      }
    });

    // Listen to wheel events in order to try and update the viewport on time.
    on(d.scroller, "mousewheel", function(e){onScrollWheel(cm, e);});
    on(d.scroller, "DOMMouseScroll", function(e){onScrollWheel(cm, e);});

    // Prevent wrapper from ever scrolling
    on(d.wrapper, "scroll", function() { d.wrapper.scrollTop = d.wrapper.scrollLeft = 0; });

    d.dragFunctions = {
      simple: function(e) {if (!signalDOMEvent(cm, e)) e_stop(e);},
      start: function(e){onDragStart(cm, e);},
      drop: operation(cm, onDrop)
    };

    var inp = d.input.getField();
    on(inp, "keyup", function(e) { onKeyUp.call(cm, e); });
    on(inp, "keydown", operation(cm, onKeyDown));
    on(inp, "keypress", operation(cm, onKeyPress));
    on(inp, "focus", bind(onFocus, cm));
    on(inp, "blur", bind(onBlur, cm));
  }

  function dragDropChanged(cm, value, old) {
    var wasOn = old && old != CodeMirror.Init;
    if (!value != !wasOn) {
      var funcs = cm.display.dragFunctions;
      var toggle = value ? on : off;
      toggle(cm.display.scroller, "dragstart", funcs.start);
      toggle(cm.display.scroller, "dragenter", funcs.simple);
      toggle(cm.display.scroller, "dragover", funcs.simple);
      toggle(cm.display.scroller, "drop", funcs.drop);
    }
  }

  // Called when the window resizes
  function onResize(cm) {
    var d = cm.display;
    if (d.lastWrapHeight == d.wrapper.clientHeight && d.lastWrapWidth == d.wrapper.clientWidth)
      return;
    // Might be a text scaling operation, clear size caches.
    d.cachedCharWidth = d.cachedTextHeight = d.cachedPaddingH = null;
    d.scrollbarsClipped = false;
    cm.setSize();
  }

  // MOUSE EVENTS

  // Return true when the given mouse event happened in a widget
  function eventInWidget(display, e) {
    for (var n = e_target(e); n != display.wrapper; n = n.parentNode) {
      if (!n || (n.nodeType == 1 && n.getAttribute("cm-ignore-events") == "true") ||
          (n.parentNode == display.sizer && n != display.mover))
        return true;
    }
  }

  // Given a mouse event, find the corresponding position. If liberal
  // is false, it checks whether a gutter or scrollbar was clicked,
  // and returns null if it was. forRect is used by rectangular
  // selections, and tries to estimate a character position even for
  // coordinates beyond the right of the text.
  function posFromMouse(cm, e, liberal, forRect) {
    var display = cm.display;
    if (!liberal && e_target(e).getAttribute("cm-not-content") == "true") return null;

    var x, y, space = display.lineSpace.getBoundingClientRect();
    // Fails unpredictably on IE[67] when mouse is dragged around quickly.
    try { x = e.clientX - space.left; y = e.clientY - space.top; }
    catch (e) { return null; }
    var coords = coordsChar(cm, x, y), line;
    if (forRect && coords.xRel == 1 && (line = getLine(cm.doc, coords.line).text).length == coords.ch) {
      var colDiff = countColumn(line, line.length, cm.options.tabSize) - line.length;
      coords = Pos(coords.line, Math.max(0, Math.round((x - paddingH(cm.display).left) / charWidth(cm.display)) - colDiff));
    }
    return coords;
  }

  // A mouse down can be a single click, double click, triple click,
  // start of selection drag, start of text drag, new cursor
  // (ctrl-click), rectangle drag (alt-drag), or xwin
  // middle-click-paste. Or it might be a click on something we should
  // not interfere with, such as a scrollbar or widget.
  function onMouseDown(e) {
    var cm = this, display = cm.display;
    if (display.activeTouch && display.input.supportsTouch() || signalDOMEvent(cm, e)) return;
    display.shift = e.shiftKey;

    if (eventInWidget(display, e)) {
      if (!webkit) {
        // Briefly turn off draggability, to allow widgets to do
        // normal dragging things.
        display.scroller.draggable = false;
        setTimeout(function(){display.scroller.draggable = true;}, 100);
      }
      return;
    }
    if (clickInGutter(cm, e)) return;
    var start = posFromMouse(cm, e);
    window.focus();

    switch (e_button(e)) {
    case 1:
      if (start)
        leftButtonDown(cm, e, start);
      else if (e_target(e) == display.scroller)
        e_preventDefault(e);
      break;
    case 2:
      if (webkit) cm.state.lastMiddleDown = +new Date;
      if (start) extendSelection(cm.doc, start);
      setTimeout(function() {display.input.focus();}, 20);
      e_preventDefault(e);
      break;
    case 3:
      if (captureRightClick) onContextMenu(cm, e);
      else delayBlurEvent(cm);
      break;
    }
  }

  var lastClick, lastDoubleClick;
  function leftButtonDown(cm, e, start) {
    if (ie) setTimeout(bind(ensureFocus, cm), 0);
    else cm.curOp.focus = activeElt();

    var now = +new Date, type;
    if (lastDoubleClick && lastDoubleClick.time > now - 400 && cmp(lastDoubleClick.pos, start) == 0) {
      type = "triple";
    } else if (lastClick && lastClick.time > now - 400 && cmp(lastClick.pos, start) == 0) {
      type = "double";
      lastDoubleClick = {time: now, pos: start};
    } else {
      type = "single";
      lastClick = {time: now, pos: start};
    }

    var sel = cm.doc.sel, modifier = mac ? e.metaKey : e.ctrlKey, contained;
    if (cm.options.dragDrop && dragAndDrop && !isReadOnly(cm) &&
        type == "single" && (contained = sel.contains(start)) > -1 &&
        !sel.ranges[contained].empty())
      leftButtonStartDrag(cm, e, start, modifier);
    else
      leftButtonSelect(cm, e, start, type, modifier);
  }

  // Start a text drag. When it ends, see if any dragging actually
  // happen, and treat as a click if it didn't.
  function leftButtonStartDrag(cm, e, start, modifier) {
    var display = cm.display, startTime = +new Date;
    var dragEnd = operation(cm, function(e2) {
      if (webkit) display.scroller.draggable = false;
      cm.state.draggingText = false;
      off(document, "mouseup", dragEnd);
      off(display.scroller, "drop", dragEnd);
      if (Math.abs(e.clientX - e2.clientX) + Math.abs(e.clientY - e2.clientY) < 10) {
        e_preventDefault(e2);
        if (!modifier && +new Date - 200 < startTime)
          extendSelection(cm.doc, start);
        // Work around unexplainable focus problem in IE9 (#2127) and Chrome (#3081)
        if (webkit || ie && ie_version == 9)
          setTimeout(function() {document.body.focus(); display.input.focus();}, 20);
        else
          display.input.focus();
      }
    });
    // Let the drag handler handle this.
    if (webkit) display.scroller.draggable = true;
    cm.state.draggingText = dragEnd;
    // IE's approach to draggable
    if (display.scroller.dragDrop) display.scroller.dragDrop();
    on(document, "mouseup", dragEnd);
    on(display.scroller, "drop", dragEnd);
  }

  // Normal selection, as opposed to text dragging.
  function leftButtonSelect(cm, e, start, type, addNew) {
    var display = cm.display, doc = cm.doc;
    e_preventDefault(e);

    var ourRange, ourIndex, startSel = doc.sel, ranges = startSel.ranges;
    if (addNew && !e.shiftKey) {
      ourIndex = doc.sel.contains(start);
      if (ourIndex > -1)
        ourRange = ranges[ourIndex];
      else
        ourRange = new Range(start, start);
    } else {
      ourRange = doc.sel.primary();
      ourIndex = doc.sel.primIndex;
    }

    if (e.altKey) {
      type = "rect";
      if (!addNew) ourRange = new Range(start, start);
      start = posFromMouse(cm, e, true, true);
      ourIndex = -1;
    } else if (type == "double") {
      var word = cm.findWordAt(start);
      if (cm.display.shift || doc.extend)
        ourRange = extendRange(doc, ourRange, word.anchor, word.head);
      else
        ourRange = word;
    } else if (type == "triple") {
      var line = new Range(Pos(start.line, 0), clipPos(doc, Pos(start.line + 1, 0)));
      if (cm.display.shift || doc.extend)
        ourRange = extendRange(doc, ourRange, line.anchor, line.head);
      else
        ourRange = line;
    } else {
      ourRange = extendRange(doc, ourRange, start);
    }

    if (!addNew) {
      ourIndex = 0;
      setSelection(doc, new Selection([ourRange], 0), sel_mouse);
      startSel = doc.sel;
    } else if (ourIndex == -1) {
      ourIndex = ranges.length;
      setSelection(doc, normalizeSelection(ranges.concat([ourRange]), ourIndex),
                   {scroll: false, origin: "*mouse"});
    } else if (ranges.length > 1 && ranges[ourIndex].empty() && type == "single" && !e.shiftKey) {
      setSelection(doc, normalizeSelection(ranges.slice(0, ourIndex).concat(ranges.slice(ourIndex + 1)), 0));
      startSel = doc.sel;
    } else {
      replaceOneSelection(doc, ourIndex, ourRange, sel_mouse);
    }

    var lastPos = start;
    function extendTo(pos) {
      if (cmp(lastPos, pos) == 0) return;
      lastPos = pos;

      if (type == "rect") {
        var ranges = [], tabSize = cm.options.tabSize;
        var startCol = countColumn(getLine(doc, start.line).text, start.ch, tabSize);
        var posCol = countColumn(getLine(doc, pos.line).text, pos.ch, tabSize);
        var left = Math.min(startCol, posCol), right = Math.max(startCol, posCol);
        for (var line = Math.min(start.line, pos.line), end = Math.min(cm.lastLine(), Math.max(start.line, pos.line));
             line <= end; line++) {
          var text = getLine(doc, line).text, leftPos = findColumn(text, left, tabSize);
          if (left == right)
            ranges.push(new Range(Pos(line, leftPos), Pos(line, leftPos)));
          else if (text.length > leftPos)
            ranges.push(new Range(Pos(line, leftPos), Pos(line, findColumn(text, right, tabSize))));
        }
        if (!ranges.length) ranges.push(new Range(start, start));
        setSelection(doc, normalizeSelection(startSel.ranges.slice(0, ourIndex).concat(ranges), ourIndex),
                     {origin: "*mouse", scroll: false});
        cm.scrollIntoView(pos);
      } else {
        var oldRange = ourRange;
        var anchor = oldRange.anchor, head = pos;
        if (type != "single") {
          if (type == "double")
            var range = cm.findWordAt(pos);
          else
            var range = new Range(Pos(pos.line, 0), clipPos(doc, Pos(pos.line + 1, 0)));
          if (cmp(range.anchor, anchor) > 0) {
            head = range.head;
            anchor = minPos(oldRange.from(), range.anchor);
          } else {
            head = range.anchor;
            anchor = maxPos(oldRange.to(), range.head);
          }
        }
        var ranges = startSel.ranges.slice(0);
        ranges[ourIndex] = new Range(clipPos(doc, anchor), head);
        setSelection(doc, normalizeSelection(ranges, ourIndex), sel_mouse);
      }
    }

    var editorSize = display.wrapper.getBoundingClientRect();
    // Used to ensure timeout re-tries don't fire when another extend
    // happened in the meantime (clearTimeout isn't reliable -- at
    // least on Chrome, the timeouts still happen even when cleared,
    // if the clear happens after their scheduled firing time).
    var counter = 0;

    function extend(e) {
      var curCount = ++counter;
      var cur = posFromMouse(cm, e, true, type == "rect");
      if (!cur) return;
      if (cmp(cur, lastPos) != 0) {
        cm.curOp.focus = activeElt();
        extendTo(cur);
        var visible = visibleLines(display, doc);
        if (cur.line >= visible.to || cur.line < visible.from)
          setTimeout(operation(cm, function(){if (counter == curCount) extend(e);}), 150);
      } else {
        var outside = e.clientY < editorSize.top ? -20 : e.clientY > editorSize.bottom ? 20 : 0;
        if (outside) setTimeout(operation(cm, function() {
          if (counter != curCount) return;
          display.scroller.scrollTop += outside;
          extend(e);
        }), 50);
      }
    }

    function done(e) {
      counter = Infinity;
      e_preventDefault(e);
      display.input.focus();
      off(document, "mousemove", move);
      off(document, "mouseup", up);
      doc.history.lastSelOrigin = null;
    }

    var move = operation(cm, function(e) {
      if (!e_button(e)) done(e);
      else extend(e);
    });
    var up = operation(cm, done);
    on(document, "mousemove", move);
    on(document, "mouseup", up);
  }

  // Determines whether an event happened in the gutter, and fires the
  // handlers for the corresponding event.
  function gutterEvent(cm, e, type, prevent, signalfn) {
    try { var mX = e.clientX, mY = e.clientY; }
    catch(e) { return false; }
    if (mX >= Math.floor(cm.display.gutters.getBoundingClientRect().right)) return false;
    if (prevent) e_preventDefault(e);

    var display = cm.display;
    var lineBox = display.lineDiv.getBoundingClientRect();

    if (mY > lineBox.bottom || !hasHandler(cm, type)) return e_defaultPrevented(e);
    mY -= lineBox.top - display.viewOffset;

    for (var i = 0; i < cm.options.gutters.length; ++i) {
      var g = display.gutters.childNodes[i];
      if (g && g.getBoundingClientRect().right >= mX) {
        var line = lineAtHeight(cm.doc, mY);
        var gutter = cm.options.gutters[i];
        signalfn(cm, type, cm, line, gutter, e);
        return e_defaultPrevented(e);
      }
    }
  }

  function clickInGutter(cm, e) {
    return gutterEvent(cm, e, "gutterClick", true, signalLater);
  }

  // Kludge to work around strange IE behavior where it'll sometimes
  // re-fire a series of drag-related events right after the drop (#1551)
  var lastDrop = 0;

  function onDrop(e) {
    var cm = this;
    if (signalDOMEvent(cm, e) || eventInWidget(cm.display, e))
      return;
    e_preventDefault(e);
    if (ie) lastDrop = +new Date;
    var pos = posFromMouse(cm, e, true), files = e.dataTransfer.files;
    if (!pos || isReadOnly(cm)) return;
    // Might be a file drop, in which case we simply extract the text
    // and insert it.
    if (files && files.length && window.FileReader && window.File) {
      var n = files.length, text = Array(n), read = 0;
      var loadFile = function(file, i) {
        var reader = new FileReader;
        reader.onload = operation(cm, function() {
          text[i] = reader.result;
          if (++read == n) {
            pos = clipPos(cm.doc, pos);
            var change = {from: pos, to: pos, text: splitLines(text.join("\n")), origin: "paste"};
            makeChange(cm.doc, change);
            setSelectionReplaceHistory(cm.doc, simpleSelection(pos, changeEnd(change)));
          }
        });
        reader.readAsText(file);
      };
      for (var i = 0; i < n; ++i) loadFile(files[i], i);
    } else { // Normal drop
      // Don't do a replace if the drop happened inside of the selected text.
      if (cm.state.draggingText && cm.doc.sel.contains(pos) > -1) {
        cm.state.draggingText(e);
        // Ensure the editor is re-focused
        setTimeout(function() {cm.display.input.focus();}, 20);
        return;
      }
      try {
        var text = e.dataTransfer.getData("Text");
        if (text) {
          if (cm.state.draggingText && !(mac ? e.altKey : e.ctrlKey))
            var selected = cm.listSelections();
          setSelectionNoUndo(cm.doc, simpleSelection(pos, pos));
          if (selected) for (var i = 0; i < selected.length; ++i)
            replaceRange(cm.doc, "", selected[i].anchor, selected[i].head, "drag");
          cm.replaceSelection(text, "around", "paste");
          cm.display.input.focus();
        }
      }
      catch(e){}
    }
  }

  function onDragStart(cm, e) {
    if (ie && (!cm.state.draggingText || +new Date - lastDrop < 100)) { e_stop(e); return; }
    if (signalDOMEvent(cm, e) || eventInWidget(cm.display, e)) return;

    e.dataTransfer.setData("Text", cm.getSelection());

    // Use dummy image instead of default browsers image.
    // Recent Safari (~6.0.2) have a tendency to segfault when this happens, so we don't do it there.
    if (e.dataTransfer.setDragImage && !safari) {
      var img = elt("img", null, null, "position: fixed; left: 0; top: 0;");
      img.src = "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==";
      if (presto) {
        img.width = img.height = 1;
        cm.display.wrapper.appendChild(img);
        // Force a relayout, or Opera won't use our image for some obscure reason
        img._top = img.offsetTop;
      }
      e.dataTransfer.setDragImage(img, 0, 0);
      if (presto) img.parentNode.removeChild(img);
    }
  }

  // SCROLL EVENTS

  // Sync the scrollable area and scrollbars, ensure the viewport
  // covers the visible area.
  function setScrollTop(cm, val) {
    if (Math.abs(cm.doc.scrollTop - val) < 2) return;
    cm.doc.scrollTop = val;
    if (!gecko) updateDisplaySimple(cm, {top: val});
    if (cm.display.scroller.scrollTop != val) cm.display.scroller.scrollTop = val;
    cm.display.scrollbars.setScrollTop(val);
    if (gecko) updateDisplaySimple(cm);
    startWorker(cm, 100);
  }
  // Sync scroller and scrollbar, ensure the gutter elements are
  // aligned.
  function setScrollLeft(cm, val, isScroller) {
    if (isScroller ? val == cm.doc.scrollLeft : Math.abs(cm.doc.scrollLeft - val) < 2) return;
    val = Math.min(val, cm.display.scroller.scrollWidth - cm.display.scroller.clientWidth);
    cm.doc.scrollLeft = val;
    alignHorizontally(cm);
    if (cm.display.scroller.scrollLeft != val) cm.display.scroller.scrollLeft = val;
    cm.display.scrollbars.setScrollLeft(val);
  }

  // Since the delta values reported on mouse wheel events are
  // unstandardized between browsers and even browser versions, and
  // generally horribly unpredictable, this code starts by measuring
  // the scroll effect that the first few mouse wheel events have,
  // and, from that, detects the way it can convert deltas to pixel
  // offsets afterwards.
  //
  // The reason we want to know the amount a wheel event will scroll
  // is that it gives us a chance to update the display before the
  // actual scrolling happens, reducing flickering.

  var wheelSamples = 0, wheelPixelsPerUnit = null;
  // Fill in a browser-detected starting value on browsers where we
  // know one. These don't have to be accurate -- the result of them
  // being wrong would just be a slight flicker on the first wheel
  // scroll (if it is large enough).
  if (ie) wheelPixelsPerUnit = -.53;
  else if (gecko) wheelPixelsPerUnit = 15;
  else if (chrome) wheelPixelsPerUnit = -.7;
  else if (safari) wheelPixelsPerUnit = -1/3;

  var wheelEventDelta = function(e) {
    var dx = e.wheelDeltaX, dy = e.wheelDeltaY;
    if (dx == null && e.detail && e.axis == e.HORIZONTAL_AXIS) dx = e.detail;
    if (dy == null && e.detail && e.axis == e.VERTICAL_AXIS) dy = e.detail;
    else if (dy == null) dy = e.wheelDelta;
    return {x: dx, y: dy};
  };
  CodeMirror.wheelEventPixels = function(e) {
    var delta = wheelEventDelta(e);
    delta.x *= wheelPixelsPerUnit;
    delta.y *= wheelPixelsPerUnit;
    return delta;
  };

  function onScrollWheel(cm, e) {
    var delta = wheelEventDelta(e), dx = delta.x, dy = delta.y;

    var display = cm.display, scroll = display.scroller;
    // Quit if there's nothing to scroll here
    if (!(dx && scroll.scrollWidth > scroll.clientWidth ||
          dy && scroll.scrollHeight > scroll.clientHeight)) return;

    // Webkit browsers on OS X abort momentum scrolls when the target
    // of the scroll event is removed from the scrollable element.
    // This hack (see related code in patchDisplay) makes sure the
    // element is kept around.
    if (dy && mac && webkit) {
      outer: for (var cur = e.target, view = display.view; cur != scroll; cur = cur.parentNode) {
        for (var i = 0; i < view.length; i++) {
          if (view[i].node == cur) {
            cm.display.currentWheelTarget = cur;
            break outer;
          }
        }
      }
    }

    // On some browsers, horizontal scrolling will cause redraws to
    // happen before the gutter has been realigned, causing it to
    // wriggle around in a most unseemly way. When we have an
    // estimated pixels/delta value, we just handle horizontal
    // scrolling entirely here. It'll be slightly off from native, but
    // better than glitching out.
    if (dx && !gecko && !presto && wheelPixelsPerUnit != null) {
      if (dy)
        setScrollTop(cm, Math.max(0, Math.min(scroll.scrollTop + dy * wheelPixelsPerUnit, scroll.scrollHeight - scroll.clientHeight)));
      setScrollLeft(cm, Math.max(0, Math.min(scroll.scrollLeft + dx * wheelPixelsPerUnit, scroll.scrollWidth - scroll.clientWidth)));
      e_preventDefault(e);
      display.wheelStartX = null; // Abort measurement, if in progress
      return;
    }

    // 'Project' the visible viewport to cover the area that is being
    // scrolled into view (if we know enough to estimate it).
    if (dy && wheelPixelsPerUnit != null) {
      var pixels = dy * wheelPixelsPerUnit;
      var top = cm.doc.scrollTop, bot = top + display.wrapper.clientHeight;
      if (pixels < 0) top = Math.max(0, top + pixels - 50);
      else bot = Math.min(cm.doc.height, bot + pixels + 50);
      updateDisplaySimple(cm, {top: top, bottom: bot});
    }

    if (wheelSamples < 20) {
      if (display.wheelStartX == null) {
        display.wheelStartX = scroll.scrollLeft; display.wheelStartY = scroll.scrollTop;
        display.wheelDX = dx; display.wheelDY = dy;
        setTimeout(function() {
          if (display.wheelStartX == null) return;
          var movedX = scroll.scrollLeft - display.wheelStartX;
          var movedY = scroll.scrollTop - display.wheelStartY;
          var sample = (movedY && display.wheelDY && movedY / display.wheelDY) ||
            (movedX && display.wheelDX && movedX / display.wheelDX);
          display.wheelStartX = display.wheelStartY = null;
          if (!sample) return;
          wheelPixelsPerUnit = (wheelPixelsPerUnit * wheelSamples + sample) / (wheelSamples + 1);
          ++wheelSamples;
        }, 200);
      } else {
        display.wheelDX += dx; display.wheelDY += dy;
      }
    }
  }

  // KEY EVENTS

  // Run a handler that was bound to a key.
  function doHandleBinding(cm, bound, dropShift) {
    if (typeof bound == "string") {
      bound = commands[bound];
      if (!bound) return false;
    }
    // Ensure previous input has been read, so that the handler sees a
    // consistent view of the document
    cm.display.input.ensurePolled();
    var prevShift = cm.display.shift, done = false;
    try {
      if (isReadOnly(cm)) cm.state.suppressEdits = true;
      if (dropShift) cm.display.shift = false;
      done = bound(cm) != Pass;
    } finally {
      cm.display.shift = prevShift;
      cm.state.suppressEdits = false;
    }
    return done;
  }

  function lookupKeyForEditor(cm, name, handle) {
    for (var i = 0; i < cm.state.keyMaps.length; i++) {
      var result = lookupKey(name, cm.state.keyMaps[i], handle, cm);
      if (result) return result;
    }
    return (cm.options.extraKeys && lookupKey(name, cm.options.extraKeys, handle, cm))
      || lookupKey(name, cm.options.keyMap, handle, cm);
  }

  var stopSeq = new Delayed;
  function dispatchKey(cm, name, e, handle) {
    var seq = cm.state.keySeq;
    if (seq) {
      if (isModifierKey(name)) return "handled";
      stopSeq.set(50, function() {
        if (cm.state.keySeq == seq) {
          cm.state.keySeq = null;
          cm.display.input.reset();
        }
      });
      name = seq + " " + name;
    }
    var result = lookupKeyForEditor(cm, name, handle);

    if (result == "multi")
      cm.state.keySeq = name;
    if (result == "handled")
      signalLater(cm, "keyHandled", cm, name, e);

    if (result == "handled" || result == "multi") {
      e_preventDefault(e);
      restartBlink(cm);
    }

    if (seq && !result && /\'$/.test(name)) {
      e_preventDefault(e);
      return true;
    }
    return !!result;
  }

  // Handle a key from the keydown event.
  function handleKeyBinding(cm, e) {
    var name = keyName(e, true);
    if (!name) return false;

    if (e.shiftKey && !cm.state.keySeq) {
      // First try to resolve full name (including 'Shift-'). Failing
      // that, see if there is a cursor-motion command (starting with
      // 'go') bound to the keyname without 'Shift-'.
      return dispatchKey(cm, "Shift-" + name, e, function(b) {return doHandleBinding(cm, b, true);})
          || dispatchKey(cm, name, e, function(b) {
               if (typeof b == "string" ? /^go[A-Z]/.test(b) : b.motion)
                 return doHandleBinding(cm, b);
             });
    } else {
      return dispatchKey(cm, name, e, function(b) { return doHandleBinding(cm, b); });
    }
  }

  // Handle a key from the keypress event
  function handleCharBinding(cm, e, ch) {
    return dispatchKey(cm, "'" + ch + "'", e,
                       function(b) { return doHandleBinding(cm, b, true); });
  }

  var lastStoppedKey = null;
  function onKeyDown(e) {
    var cm = this;
    cm.curOp.focus = activeElt();
    if (signalDOMEvent(cm, e)) return;
    // IE does strange things with escape.
    if (ie && ie_version < 11 && e.keyCode == 27) e.returnValue = false;
    var code = e.keyCode;
    cm.display.shift = code == 16 || e.shiftKey;
    var handled = handleKeyBinding(cm, e);
    if (presto) {
      lastStoppedKey = handled ? code : null;
      // Opera has no cut event... we try to at least catch the key combo
      if (!handled && code == 88 && !hasCopyEvent && (mac ? e.metaKey : e.ctrlKey))
        cm.replaceSelection("", null, "cut");
    }

    // Turn mouse into crosshair when Alt is held on Mac.
    if (code == 18 && !/\bCodeMirror-crosshair\b/.test(cm.display.lineDiv.className))
      showCrossHair(cm);
  }

  function showCrossHair(cm) {
    var lineDiv = cm.display.lineDiv;
    addClass(lineDiv, "CodeMirror-crosshair");

    function up(e) {
      if (e.keyCode == 18 || !e.altKey) {
        rmClass(lineDiv, "CodeMirror-crosshair");
        off(document, "keyup", up);
        off(document, "mouseover", up);
      }
    }
    on(document, "keyup", up);
    on(document, "mouseover", up);
  }

  function onKeyUp(e) {
    if (e.keyCode == 16) this.doc.sel.shift = false;
    signalDOMEvent(this, e);
  }

  function onKeyPress(e) {
    var cm = this;
    if (eventInWidget(cm.display, e) || signalDOMEvent(cm, e) || e.ctrlKey && !e.altKey || mac && e.metaKey) return;
    var keyCode = e.keyCode, charCode = e.charCode;
    if (presto && keyCode == lastStoppedKey) {lastStoppedKey = null; e_preventDefault(e); return;}
    if ((presto && (!e.which || e.which < 10)) && handleKeyBinding(cm, e)) return;
    var ch = String.fromCharCode(charCode == null ? keyCode : charCode);
    if (handleCharBinding(cm, e, ch)) return;
    cm.display.input.onKeyPress(e);
  }

  // FOCUS/BLUR EVENTS

  function delayBlurEvent(cm) {
    cm.state.delayingBlurEvent = true;
    setTimeout(function() {
      if (cm.state.delayingBlurEvent) {
        cm.state.delayingBlurEvent = false;
        onBlur(cm);
      }
    }, 100);
  }

  function onFocus(cm) {
    if (cm.state.delayingBlurEvent) cm.state.delayingBlurEvent = false;

    if (cm.options.readOnly == "nocursor") return;
    if (!cm.state.focused) {
      signal(cm, "focus", cm);
      cm.state.focused = true;
      addClass(cm.display.wrapper, "CodeMirror-focused");
      // This test prevents this from firing when a context
      // menu is closed (since the input reset would kill the
      // select-all detection hack)
      if (!cm.curOp && cm.display.selForContextMenu != cm.doc.sel) {
        cm.display.input.reset();
        if (webkit) setTimeout(function() { cm.display.input.reset(true); }, 20); // Issue #1730
      }
      cm.display.input.receivedFocus();
    }
    restartBlink(cm);
  }
  function onBlur(cm) {
    if (cm.state.delayingBlurEvent) return;

    if (cm.state.focused) {
      signal(cm, "blur", cm);
      cm.state.focused = false;
      rmClass(cm.display.wrapper, "CodeMirror-focused");
    }
    clearInterval(cm.display.blinker);
    setTimeout(function() {if (!cm.state.focused) cm.display.shift = false;}, 150);
  }

  // CONTEXT MENU HANDLING

  // To make the context menu work, we need to briefly unhide the
  // textarea (making it as unobtrusive as possible) to let the
  // right-click take effect on it.
  function onContextMenu(cm, e) {
    if (eventInWidget(cm.display, e) || contextMenuInGutter(cm, e)) return;
    cm.display.input.onContextMenu(e);
  }

  function contextMenuInGutter(cm, e) {
    if (!hasHandler(cm, "gutterContextMenu")) return false;
    return gutterEvent(cm, e, "gutterContextMenu", false, signal);
  }

  // UPDATING

  // Compute the position of the end of a change (its 'to' property
  // refers to the pre-change end).
  var changeEnd = CodeMirror.changeEnd = function(change) {
    if (!change.text) return change.to;
    return Pos(change.from.line + change.text.length - 1,
               lst(change.text).length + (change.text.length == 1 ? change.from.ch : 0));
  };

  // Adjust a position to refer to the post-change position of the
  // same text, or the end of the change if the change covers it.
  function adjustForChange(pos, change) {
    if (cmp(pos, change.from) < 0) return pos;
    if (cmp(pos, change.to) <= 0) return changeEnd(change);

    var line = pos.line + change.text.length - (change.to.line - change.from.line) - 1, ch = pos.ch;
    if (pos.line == change.to.line) ch += changeEnd(change).ch - change.to.ch;
    return Pos(line, ch);
  }

  function computeSelAfterChange(doc, change) {
    var out = [];
    for (var i = 0; i < doc.sel.ranges.length; i++) {
      var range = doc.sel.ranges[i];
      out.push(new Range(adjustForChange(range.anchor, change),
                         adjustForChange(range.head, change)));
    }
    return normalizeSelection(out, doc.sel.primIndex);
  }

  function offsetPos(pos, old, nw) {
    if (pos.line == old.line)
      return Pos(nw.line, pos.ch - old.ch + nw.ch);
    else
      return Pos(nw.line + (pos.line - old.line), pos.ch);
  }

  // Used by replaceSelections to allow moving the selection to the
  // start or around the replaced test. Hint may be "start" or "around".
  function computeReplacedSel(doc, changes, hint) {
    var out = [];
    var oldPrev = Pos(doc.first, 0), newPrev = oldPrev;
    for (var i = 0; i < changes.length; i++) {
      var change = changes[i];
      var from = offsetPos(change.from, oldPrev, newPrev);
      var to = offsetPos(changeEnd(change), oldPrev, newPrev);
      oldPrev = change.to;
      newPrev = to;
      if (hint == "around") {
        var range = doc.sel.ranges[i], inv = cmp(range.head, range.anchor) < 0;
        out[i] = new Range(inv ? to : from, inv ? from : to);
      } else {
        out[i] = new Range(from, from);
      }
    }
    return new Selection(out, doc.sel.primIndex);
  }

  // Allow "beforeChange" event handlers to influence a change
  function filterChange(doc, change, update) {
    var obj = {
      canceled: false,
      from: change.from,
      to: change.to,
      text: change.text,
      origin: change.origin,
      cancel: function() { this.canceled = true; }
    };
    if (update) obj.update = function(from, to, text, origin) {
      if (from) this.from = clipPos(doc, from);
      if (to) this.to = clipPos(doc, to);
      if (text) this.text = text;
      if (origin !== undefined) this.origin = origin;
    };
    signal(doc, "beforeChange", doc, obj);
    if (doc.cm) signal(doc.cm, "beforeChange", doc.cm, obj);

    if (obj.canceled) return null;
    return {from: obj.from, to: obj.to, text: obj.text, origin: obj.origin};
  }

  // Apply a change to a document, and add it to the document's
  // history, and propagating it to all linked documents.
  function makeChange(doc, change, ignoreReadOnly) {
    if (doc.cm) {
      if (!doc.cm.curOp) return operation(doc.cm, makeChange)(doc, change, ignoreReadOnly);
      if (doc.cm.state.suppressEdits) return;
    }

    if (hasHandler(doc, "beforeChange") || doc.cm && hasHandler(doc.cm, "beforeChange")) {
      change = filterChange(doc, change, true);
      if (!change) return;
    }

    // Possibly split or suppress the update based on the presence
    // of read-only spans in its range.
    var split = sawReadOnlySpans && !ignoreReadOnly && removeReadOnlyRanges(doc, change.from, change.to);
    if (split) {
      for (var i = split.length - 1; i >= 0; --i)
        makeChangeInner(doc, {from: split[i].from, to: split[i].to, text: i ? [""] : change.text});
    } else {
      makeChangeInner(doc, change);
    }
  }

  function makeChangeInner(doc, change) {
    if (change.text.length == 1 && change.text[0] == "" && cmp(change.from, change.to) == 0) return;
    var selAfter = computeSelAfterChange(doc, change);
    addChangeToHistory(doc, change, selAfter, doc.cm ? doc.cm.curOp.id : NaN);

    makeChangeSingleDoc(doc, change, selAfter, stretchSpansOverChange(doc, change));
    var rebased = [];

    linkedDocs(doc, function(doc, sharedHist) {
      if (!sharedHist && indexOf(rebased, doc.history) == -1) {
        rebaseHist(doc.history, change);
        rebased.push(doc.history);
      }
      makeChangeSingleDoc(doc, change, null, stretchSpansOverChange(doc, change));
    });
  }

  // Revert a change stored in a document's history.
  function makeChangeFromHistory(doc, type, allowSelectionOnly) {
    if (doc.cm && doc.cm.state.suppressEdits) return;

    var hist = doc.history, event, selAfter = doc.sel;
    var source = type == "undo" ? hist.done : hist.undone, dest = type == "undo" ? hist.undone : hist.done;

    // Verify that there is a useable event (so that ctrl-z won't
    // needlessly clear selection events)
    for (var i = 0; i < source.length; i++) {
      event = source[i];
      if (allowSelectionOnly ? event.ranges && !event.equals(doc.sel) : !event.ranges)
        break;
    }
    if (i == source.length) return;
    hist.lastOrigin = hist.lastSelOrigin = null;

    for (;;) {
      event = source.pop();
      if (event.ranges) {
        pushSelectionToHistory(event, dest);
        if (allowSelectionOnly && !event.equals(doc.sel)) {
          setSelection(doc, event, {clearRedo: false});
          return;
        }
        selAfter = event;
      }
      else break;
    }

    // Build up a reverse change object to add to the opposite history
    // stack (redo when undoing, and vice versa).
    var antiChanges = [];
    pushSelectionToHistory(selAfter, dest);
    dest.push({changes: antiChanges, generation: hist.generation});
    hist.generation = event.generation || ++hist.maxGeneration;

    var filter = hasHandler(doc, "beforeChange") || doc.cm && hasHandler(doc.cm, "beforeChange");

    for (var i = event.changes.length - 1; i >= 0; --i) {
      var change = event.changes[i];
      change.origin = type;
      if (filter && !filterChange(doc, change, false)) {
        source.length = 0;
        return;
      }

      antiChanges.push(historyChangeFromChange(doc, change));

      var after = i ? computeSelAfterChange(doc, change) : lst(source);
      makeChangeSingleDoc(doc, change, after, mergeOldSpans(doc, change));
      if (!i && doc.cm) doc.cm.scrollIntoView({from: change.from, to: changeEnd(change)});
      var rebased = [];

      // Propagate to the linked documents
      linkedDocs(doc, function(doc, sharedHist) {
        if (!sharedHist && indexOf(rebased, doc.history) == -1) {
          rebaseHist(doc.history, change);
          rebased.push(doc.history);
        }
        makeChangeSingleDoc(doc, change, null, mergeOldSpans(doc, change));
      });
    }
  }

  // Sub-views need their line numbers shifted when text is added
  // above or below them in the parent document.
  function shiftDoc(doc, distance) {
    if (distance == 0) return;
    doc.first += distance;
    doc.sel = new Selection(map(doc.sel.ranges, function(range) {
      return new Range(Pos(range.anchor.line + distance, range.anchor.ch),
                       Pos(range.head.line + distance, range.head.ch));
    }), doc.sel.primIndex);
    if (doc.cm) {
      regChange(doc.cm, doc.first, doc.first - distance, distance);
      for (var d = doc.cm.display, l = d.viewFrom; l < d.viewTo; l++)
        regLineChange(doc.cm, l, "gutter");
    }
  }

  // More lower-level change function, handling only a single document
  // (not linked ones).
  function makeChangeSingleDoc(doc, change, selAfter, spans) {
    if (doc.cm && !doc.cm.curOp)
      return operation(doc.cm, makeChangeSingleDoc)(doc, change, selAfter, spans);

    if (change.to.line < doc.first) {
      shiftDoc(doc, change.text.length - 1 - (change.to.line - change.from.line));
      return;
    }
    if (change.from.line > doc.lastLine()) return;

    // Clip the change to the size of this doc
    if (change.from.line < doc.first) {
      var shift = change.text.length - 1 - (doc.first - change.from.line);
      shiftDoc(doc, shift);
      change = {from: Pos(doc.first, 0), to: Pos(change.to.line + shift, change.to.ch),
                text: [lst(change.text)], origin: change.origin};
    }
    var last = doc.lastLine();
    if (change.to.line > last) {
      change = {from: change.from, to: Pos(last, getLine(doc, last).text.length),
                text: [change.text[0]], origin: change.origin};
    }

    change.removed = getBetween(doc, change.from, change.to);

    if (!selAfter) selAfter = computeSelAfterChange(doc, change);
    if (doc.cm) makeChangeSingleDocInEditor(doc.cm, change, spans);
    else updateDoc(doc, change, spans);
    setSelectionNoUndo(doc, selAfter, sel_dontScroll);
  }

  // Handle the interaction of a change to a document with the editor
  // that this document is part of.
  function makeChangeSingleDocInEditor(cm, change, spans) {
    var doc = cm.doc, display = cm.display, from = change.from, to = change.to;

    var recomputeMaxLength = false, checkWidthStart = from.line;
    if (!cm.options.lineWrapping) {
      checkWidthStart = lineNo(visualLine(getLine(doc, from.line)));
      doc.iter(checkWidthStart, to.line + 1, function(line) {
        if (line == display.maxLine) {
          recomputeMaxLength = true;
          return true;
        }
      });
    }

    if (doc.sel.contains(change.from, change.to) > -1)
      signalCursorActivity(cm);

    updateDoc(doc, change, spans, estimateHeight(cm));

    if (!cm.options.lineWrapping) {
      doc.iter(checkWidthStart, from.line + change.text.length, function(line) {
        var len = lineLength(line);
        if (len > display.maxLineLength) {
          display.maxLine = line;
          display.maxLineLength = len;
          display.maxLineChanged = true;
          recomputeMaxLength = false;
        }
      });
      if (recomputeMaxLength) cm.curOp.updateMaxLine = true;
    }

    // Adjust frontier, schedule worker
    doc.frontier = Math.min(doc.frontier, from.line);
    startWorker(cm, 400);

    var lendiff = change.text.length - (to.line - from.line) - 1;
    // Remember that these lines changed, for updating the display
    if (change.full)
      regChange(cm);
    else if (from.line == to.line && change.text.length == 1 && !isWholeLineUpdate(cm.doc, change))
      regLineChange(cm, from.line, "text");
    else
      regChange(cm, from.line, to.line + 1, lendiff);

    var changesHandler = hasHandler(cm, "changes"), changeHandler = hasHandler(cm, "change");
    if (changeHandler || changesHandler) {
      var obj = {
        from: from, to: to,
        text: change.text,
        removed: change.removed,
        origin: change.origin
      };
      if (changeHandler) signalLater(cm, "change", cm, obj);
      if (changesHandler) (cm.curOp.changeObjs || (cm.curOp.changeObjs = [])).push(obj);
    }
    cm.display.selForContextMenu = null;
  }

  function replaceRange(doc, code, from, to, origin) {
    if (!to) to = from;
    if (cmp(to, from) < 0) { var tmp = to; to = from; from = tmp; }
    if (typeof code == "string") code = splitLines(code);
    makeChange(doc, {from: from, to: to, text: code, origin: origin});
  }

  // SCROLLING THINGS INTO VIEW

  // If an editor sits on the top or bottom of the window, partially
  // scrolled out of view, this ensures that the cursor is visible.
  function maybeScrollWindow(cm, coords) {
    if (signalDOMEvent(cm, "scrollCursorIntoView")) return;

    var display = cm.display, box = display.sizer.getBoundingClientRect(), doScroll = null;
    if (coords.top + box.top < 0) doScroll = true;
    else if (coords.bottom + box.top > (window.innerHeight || document.documentElement.clientHeight)) doScroll = false;
    if (doScroll != null && !phantom) {
      var scrollNode = elt("div", "\u200b", null, "position: absolute; top: " +
                           (coords.top - display.viewOffset - paddingTop(cm.display)) + "px; height: " +
                           (coords.bottom - coords.top + scrollGap(cm) + display.barHeight) + "px; left: " +
                           coords.left + "px; width: 2px;");
      cm.display.lineSpace.appendChild(scrollNode);
      scrollNode.scrollIntoView(doScroll);
      cm.display.lineSpace.removeChild(scrollNode);
    }
  }

  // Scroll a given position into view (immediately), verifying that
  // it actually became visible (as line heights are accurately
  // measured, the position of something may 'drift' during drawing).
  function scrollPosIntoView(cm, pos, end, margin) {
    if (margin == null) margin = 0;
    for (var limit = 0; limit < 5; limit++) {
      var changed = false, coords = cursorCoords(cm, pos);
      var endCoords = !end || end == pos ? coords : cursorCoords(cm, end);
      var scrollPos = calculateScrollPos(cm, Math.min(coords.left, endCoords.left),
                                         Math.min(coords.top, endCoords.top) - margin,
                                         Math.max(coords.left, endCoords.left),
                                         Math.max(coords.bottom, endCoords.bottom) + margin);
      var startTop = cm.doc.scrollTop, startLeft = cm.doc.scrollLeft;
      if (scrollPos.scrollTop != null) {
        setScrollTop(cm, scrollPos.scrollTop);
        if (Math.abs(cm.doc.scrollTop - startTop) > 1) changed = true;
      }
      if (scrollPos.scrollLeft != null) {
        setScrollLeft(cm, scrollPos.scrollLeft);
        if (Math.abs(cm.doc.scrollLeft - startLeft) > 1) changed = true;
      }
      if (!changed) break;
    }
    return coords;
  }

  // Scroll a given set of coordinates into view (immediately).
  function scrollIntoView(cm, x1, y1, x2, y2) {
    var scrollPos = calculateScrollPos(cm, x1, y1, x2, y2);
    if (scrollPos.scrollTop != null) setScrollTop(cm, scrollPos.scrollTop);
    if (scrollPos.scrollLeft != null) setScrollLeft(cm, scrollPos.scrollLeft);
  }

  // Calculate a new scroll position needed to scroll the given
  // rectangle into view. Returns an object with scrollTop and
  // scrollLeft properties. When these are undefined, the
  // vertical/horizontal position does not need to be adjusted.
  function calculateScrollPos(cm, x1, y1, x2, y2) {
    var display = cm.display, snapMargin = textHeight(cm.display);
    if (y1 < 0) y1 = 0;
    var screentop = cm.curOp && cm.curOp.scrollTop != null ? cm.curOp.scrollTop : display.scroller.scrollTop;
    var screen = displayHeight(cm), result = {};
    if (y2 - y1 > screen) y2 = y1 + screen;
    var docBottom = cm.doc.height + paddingVert(display);
    var atTop = y1 < snapMargin, atBottom = y2 > docBottom - snapMargin;
    if (y1 < screentop) {
      result.scrollTop = atTop ? 0 : y1;
    } else if (y2 > screentop + screen) {
      var newTop = Math.min(y1, (atBottom ? docBottom : y2) - screen);
      if (newTop != screentop) result.scrollTop = newTop;
    }

    var screenleft = cm.curOp && cm.curOp.scrollLeft != null ? cm.curOp.scrollLeft : display.scroller.scrollLeft;
    var screenw = displayWidth(cm) - (cm.options.fixedGutter ? display.gutters.offsetWidth : 0);
    var tooWide = x2 - x1 > screenw;
    if (tooWide) x2 = x1 + screenw;
    if (x1 < 10)
      result.scrollLeft = 0;
    else if (x1 < screenleft)
      result.scrollLeft = Math.max(0, x1 - (tooWide ? 0 : 10));
    else if (x2 > screenw + screenleft - 3)
      result.scrollLeft = x2 + (tooWide ? 0 : 10) - screenw;
    return result;
  }

  // Store a relative adjustment to the scroll position in the current
  // operation (to be applied when the operation finishes).
  function addToScrollPos(cm, left, top) {
    if (left != null || top != null) resolveScrollToPos(cm);
    if (left != null)
      cm.curOp.scrollLeft = (cm.curOp.scrollLeft == null ? cm.doc.scrollLeft : cm.curOp.scrollLeft) + left;
    if (top != null)
      cm.curOp.scrollTop = (cm.curOp.scrollTop == null ? cm.doc.scrollTop : cm.curOp.scrollTop) + top;
  }

  // Make sure that at the end of the operation the current cursor is
  // shown.
  function ensureCursorVisible(cm) {
    resolveScrollToPos(cm);
    var cur = cm.getCursor(), from = cur, to = cur;
    if (!cm.options.lineWrapping) {
      from = cur.ch ? Pos(cur.line, cur.ch - 1) : cur;
      to = Pos(cur.line, cur.ch + 1);
    }
    cm.curOp.scrollToPos = {from: from, to: to, margin: cm.options.cursorScrollMargin, isCursor: true};
  }

  // When an operation has its scrollToPos property set, and another
  // scroll action is applied before the end of the operation, this
  // 'simulates' scrolling that position into view in a cheap way, so
  // that the effect of intermediate scroll commands is not ignored.
  function resolveScrollToPos(cm) {
    var range = cm.curOp.scrollToPos;
    if (range) {
      cm.curOp.scrollToPos = null;
      var from = estimateCoords(cm, range.from), to = estimateCoords(cm, range.to);
      var sPos = calculateScrollPos(cm, Math.min(from.left, to.left),
                                    Math.min(from.top, to.top) - range.margin,
                                    Math.max(from.right, to.right),
                                    Math.max(from.bottom, to.bottom) + range.margin);
      cm.scrollTo(sPos.scrollLeft, sPos.scrollTop);
    }
  }

  // API UTILITIES

  // Indent the given line. The how parameter can be "smart",
  // "add"/null, "subtract", or "prev". When aggressive is false
  // (typically set to true for forced single-line indents), empty
  // lines are not indented, and places where the mode returns Pass
  // are left alone.
  function indentLine(cm, n, how, aggressive) {
    var doc = cm.doc, state;
    if (how == null) how = "add";
    if (how == "smart") {
      // Fall back to "prev" when the mode doesn't have an indentation
      // method.
      if (!doc.mode.indent) how = "prev";
      else state = getStateBefore(cm, n);
    }

    var tabSize = cm.options.tabSize;
    var line = getLine(doc, n), curSpace = countColumn(line.text, null, tabSize);
    if (line.stateAfter) line.stateAfter = null;
    var curSpaceString = line.text.match(/^\s*/)[0], indentation;
    if (!aggressive && !/\S/.test(line.text)) {
      indentation = 0;
      how = "not";
    } else if (how == "smart") {
      indentation = doc.mode.indent(state, line.text.slice(curSpaceString.length), line.text);
      if (indentation == Pass || indentation > 150) {
        if (!aggressive) return;
        how = "prev";
      }
    }
    if (how == "prev") {
      if (n > doc.first) indentation = countColumn(getLine(doc, n-1).text, null, tabSize);
      else indentation = 0;
    } else if (how == "add") {
      indentation = curSpace + cm.options.indentUnit;
    } else if (how == "subtract") {
      indentation = curSpace - cm.options.indentUnit;
    } else if (typeof how == "number") {
      indentation = curSpace + how;
    }
    indentation = Math.max(0, indentation);

    var indentString = "", pos = 0;
    if (cm.options.indentWithTabs)
      for (var i = Math.floor(indentation / tabSize); i; --i) {pos += tabSize; indentString += "\t";}
    if (pos < indentation) indentString += spaceStr(indentation - pos);

    if (indentString != curSpaceString) {
      replaceRange(doc, indentString, Pos(n, 0), Pos(n, curSpaceString.length), "+input");
      line.stateAfter = null;
      return true;
    } else {
      // Ensure that, if the cursor was in the whitespace at the start
      // of the line, it is moved to the end of that space.
      for (var i = 0; i < doc.sel.ranges.length; i++) {
        var range = doc.sel.ranges[i];
        if (range.head.line == n && range.head.ch < curSpaceString.length) {
          var pos = Pos(n, curSpaceString.length);
          replaceOneSelection(doc, i, new Range(pos, pos));
          break;
        }
      }
    }
  }

  // Utility for applying a change to a line by handle or number,
  // returning the number and optionally registering the line as
  // changed.
  function changeLine(doc, handle, changeType, op) {
    var no = handle, line = handle;
    if (typeof handle == "number") line = getLine(doc, clipLine(doc, handle));
    else no = lineNo(handle);
    if (no == null) return null;
    if (op(line, no) && doc.cm) regLineChange(doc.cm, no, changeType);
    return line;
  }

  // Helper for deleting text near the selection(s), used to implement
  // backspace, delete, and similar functionality.
  function deleteNearSelection(cm, compute) {
    var ranges = cm.doc.sel.ranges, kill = [];
    // Build up a set of ranges to kill first, merging overlapping
    // ranges.
    for (var i = 0; i < ranges.length; i++) {
      var toKill = compute(ranges[i]);
      while (kill.length && cmp(toKill.from, lst(kill).to) <= 0) {
        var replaced = kill.pop();
        if (cmp(replaced.from, toKill.from) < 0) {
          toKill.from = replaced.from;
          break;
        }
      }
      kill.push(toKill);
    }
    // Next, remove those actual ranges.
    runInOp(cm, function() {
      for (var i = kill.length - 1; i >= 0; i--)
        replaceRange(cm.doc, "", kill[i].from, kill[i].to, "+delete");
      ensureCursorVisible(cm);
    });
  }

  // Used for horizontal relative motion. Dir is -1 or 1 (left or
  // right), unit can be "char", "column" (like char, but doesn't
  // cross line boundaries), "word" (across next word), or "group" (to
  // the start of next group of word or non-word-non-whitespace
  // chars). The visually param controls whether, in right-to-left
  // text, direction 1 means to move towards the next index in the
  // string, or towards the character to the right of the current
  // position. The resulting position will have a hitSide=true
  // property if it reached the end of the document.
  function findPosH(doc, pos, dir, unit, visually) {
    var line = pos.line, ch = pos.ch, origDir = dir;
    var lineObj = getLine(doc, line);
    var possible = true;
    function findNextLine() {
      var l = line + dir;
      if (l < doc.first || l >= doc.first + doc.size) return (possible = false);
      line = l;
      return lineObj = getLine(doc, l);
    }
    function moveOnce(boundToLine) {
      var next = (visually ? moveVisually : moveLogically)(lineObj, ch, dir, true);
      if (next == null) {
        if (!boundToLine && findNextLine()) {
          if (visually) ch = (dir < 0 ? lineRight : lineLeft)(lineObj);
          else ch = dir < 0 ? lineObj.text.length : 0;
        } else return (possible = false);
      } else ch = next;
      return true;
    }

    if (unit == "char") moveOnce();
    else if (unit == "column") moveOnce(true);
    else if (unit == "word" || unit == "group") {
      var sawType = null, group = unit == "group";
      var helper = doc.cm && doc.cm.getHelper(pos, "wordChars");
      for (var first = true;; first = false) {
        if (dir < 0 && !moveOnce(!first)) break;
        var cur = lineObj.text.charAt(ch) || "\n";
        var type = isWordChar(cur, helper) ? "w"
          : group && cur == "\n" ? "n"
          : !group || /\s/.test(cur) ? null
          : "p";
        if (group && !first && !type) type = "s";
        if (sawType && sawType != type) {
          if (dir < 0) {dir = 1; moveOnce();}
          break;
        }

        if (type) sawType = type;
        if (dir > 0 && !moveOnce(!first)) break;
      }
    }
    var result = skipAtomic(doc, Pos(line, ch), origDir, true);
    if (!possible) result.hitSide = true;
    return result;
  }

  // For relative vertical movement. Dir may be -1 or 1. Unit can be
  // "page" or "line". The resulting position will have a hitSide=true
  // property if it reached the end of the document.
  function findPosV(cm, pos, dir, unit) {
    var doc = cm.doc, x = pos.left, y;
    if (unit == "page") {
      var pageSize = Math.min(cm.display.wrapper.clientHeight, window.innerHeight || document.documentElement.clientHeight);
      y = pos.top + dir * (pageSize - (dir < 0 ? 1.5 : .5) * textHeight(cm.display));
    } else if (unit == "line") {
      y = dir > 0 ? pos.bottom + 3 : pos.top - 3;
    }
    for (;;) {
      var target = coordsChar(cm, x, y);
      if (!target.outside) break;
      if (dir < 0 ? y <= 0 : y >= doc.height) { target.hitSide = true; break; }
      y += dir * 5;
    }
    return target;
  }

  // EDITOR METHODS

  // The publicly visible API. Note that methodOp(f) means
  // 'wrap f in an operation, performed on its `this` parameter'.

  // This is not the complete set of editor methods. Most of the
  // methods defined on the Doc type are also injected into
  // CodeMirror.prototype, for backwards compatibility and
  // convenience.

  CodeMirror.prototype = {
    constructor: CodeMirror,
    focus: function(){window.focus(); this.display.input.focus();},

    setOption: function(option, value) {
      var options = this.options, old = options[option];
      if (options[option] == value && option != "mode") return;
      options[option] = value;
      if (optionHandlers.hasOwnProperty(option))
        operation(this, optionHandlers[option])(this, value, old);
    },

    getOption: function(option) {return this.options[option];},
    getDoc: function() {return this.doc;},

    addKeyMap: function(map, bottom) {
      this.state.keyMaps[bottom ? "push" : "unshift"](getKeyMap(map));
    },
    removeKeyMap: function(map) {
      var maps = this.state.keyMaps;
      for (var i = 0; i < maps.length; ++i)
        if (maps[i] == map || maps[i].name == map) {
          maps.splice(i, 1);
          return true;
        }
    },

    addOverlay: methodOp(function(spec, options) {
      var mode = spec.token ? spec : CodeMirror.getMode(this.options, spec);
      if (mode.startState) throw new Error("Overlays may not be stateful.");
      this.state.overlays.push({mode: mode, modeSpec: spec, opaque: options && options.opaque});
      this.state.modeGen++;
      regChange(this);
    }),
    removeOverlay: methodOp(function(spec) {
      var overlays = this.state.overlays;
      for (var i = 0; i < overlays.length; ++i) {
        var cur = overlays[i].modeSpec;
        if (cur == spec || typeof spec == "string" && cur.name == spec) {
          overlays.splice(i, 1);
          this.state.modeGen++;
          regChange(this);
          return;
        }
      }
    }),

    indentLine: methodOp(function(n, dir, aggressive) {
      if (typeof dir != "string" && typeof dir != "number") {
        if (dir == null) dir = this.options.smartIndent ? "smart" : "prev";
        else dir = dir ? "add" : "subtract";
      }
      if (isLine(this.doc, n)) indentLine(this, n, dir, aggressive);
    }),
    indentSelection: methodOp(function(how) {
      var ranges = this.doc.sel.ranges, end = -1;
      for (var i = 0; i < ranges.length; i++) {
        var range = ranges[i];
        if (!range.empty()) {
          var from = range.from(), to = range.to();
          var start = Math.max(end, from.line);
          end = Math.min(this.lastLine(), to.line - (to.ch ? 0 : 1)) + 1;
          for (var j = start; j < end; ++j)
            indentLine(this, j, how);
          var newRanges = this.doc.sel.ranges;
          if (from.ch == 0 && ranges.length == newRanges.length && newRanges[i].from().ch > 0)
            replaceOneSelection(this.doc, i, new Range(from, newRanges[i].to()), sel_dontScroll);
        } else if (range.head.line > end) {
          indentLine(this, range.head.line, how, true);
          end = range.head.line;
          if (i == this.doc.sel.primIndex) ensureCursorVisible(this);
        }
      }
    }),

    // Fetch the parser token for a given character. Useful for hacks
    // that want to inspect the mode state (say, for completion).
    getTokenAt: function(pos, precise) {
      return takeToken(this, pos, precise);
    },

    getLineTokens: function(line, precise) {
      return takeToken(this, Pos(line), precise, true);
    },

    getTokenTypeAt: function(pos) {
      pos = clipPos(this.doc, pos);
      var styles = getLineStyles(this, getLine(this.doc, pos.line));
      var before = 0, after = (styles.length - 1) / 2, ch = pos.ch;
      var type;
      if (ch == 0) type = styles[2];
      else for (;;) {
        var mid = (before + after) >> 1;
        if ((mid ? styles[mid * 2 - 1] : 0) >= ch) after = mid;
        else if (styles[mid * 2 + 1] < ch) before = mid + 1;
        else { type = styles[mid * 2 + 2]; break; }
      }
      var cut = type ? type.indexOf("cm-overlay ") : -1;
      return cut < 0 ? type : cut == 0 ? null : type.slice(0, cut - 1);
    },

    getModeAt: function(pos) {
      var mode = this.doc.mode;
      if (!mode.innerMode) return mode;
      return CodeMirror.innerMode(mode, this.getTokenAt(pos).state).mode;
    },

    getHelper: function(pos, type) {
      return this.getHelpers(pos, type)[0];
    },

    getHelpers: function(pos, type) {
      var found = [];
      if (!helpers.hasOwnProperty(type)) return found;
      var help = helpers[type], mode = this.getModeAt(pos);
      if (typeof mode[type] == "string") {
        if (help[mode[type]]) found.push(help[mode[type]]);
      } else if (mode[type]) {
        for (var i = 0; i < mode[type].length; i++) {
          var val = help[mode[type][i]];
          if (val) found.push(val);
        }
      } else if (mode.helperType && help[mode.helperType]) {
        found.push(help[mode.helperType]);
      } else if (help[mode.name]) {
        found.push(help[mode.name]);
      }
      for (var i = 0; i < help._global.length; i++) {
        var cur = help._global[i];
        if (cur.pred(mode, this) && indexOf(found, cur.val) == -1)
          found.push(cur.val);
      }
      return found;
    },

    getStateAfter: function(line, precise) {
      var doc = this.doc;
      line = clipLine(doc, line == null ? doc.first + doc.size - 1: line);
      return getStateBefore(this, line + 1, precise);
    },

    cursorCoords: function(start, mode) {
      var pos, range = this.doc.sel.primary();
      if (start == null) pos = range.head;
      else if (typeof start == "object") pos = clipPos(this.doc, start);
      else pos = start ? range.from() : range.to();
      return cursorCoords(this, pos, mode || "page");
    },

    charCoords: function(pos, mode) {
      return charCoords(this, clipPos(this.doc, pos), mode || "page");
    },

    coordsChar: function(coords, mode) {
      coords = fromCoordSystem(this, coords, mode || "page");
      return coordsChar(this, coords.left, coords.top);
    },

    lineAtHeight: function(height, mode) {
      height = fromCoordSystem(this, {top: height, left: 0}, mode || "page").top;
      return lineAtHeight(this.doc, height + this.display.viewOffset);
    },
    heightAtLine: function(line, mode) {
      var end = false, lineObj;
      if (typeof line == "number") {
        var last = this.doc.first + this.doc.size - 1;
        if (line < this.doc.first) line = this.doc.first;
        else if (line > last) { line = last; end = true; }
        lineObj = getLine(this.doc, line);
      } else {
        lineObj = line;
      }
      return intoCoordSystem(this, lineObj, {top: 0, left: 0}, mode || "page").top +
        (end ? this.doc.height - heightAtLine(lineObj) : 0);
    },

    defaultTextHeight: function() { return textHeight(this.display); },
    defaultCharWidth: function() { return charWidth(this.display); },

    setGutterMarker: methodOp(function(line, gutterID, value) {
      return changeLine(this.doc, line, "gutter", function(line) {
        var markers = line.gutterMarkers || (line.gutterMarkers = {});
        markers[gutterID] = value;
        if (!value && isEmpty(markers)) line.gutterMarkers = null;
        return true;
      });
    }),

    clearGutter: methodOp(function(gutterID) {
      var cm = this, doc = cm.doc, i = doc.first;
      doc.iter(function(line) {
        if (line.gutterMarkers && line.gutterMarkers[gutterID]) {
          line.gutterMarkers[gutterID] = null;
          regLineChange(cm, i, "gutter");
          if (isEmpty(line.gutterMarkers)) line.gutterMarkers = null;
        }
        ++i;
      });
    }),

    lineInfo: function(line) {
      if (typeof line == "number") {
        if (!isLine(this.doc, line)) return null;
        var n = line;
        line = getLine(this.doc, line);
        if (!line) return null;
      } else {
        var n = lineNo(line);
        if (n == null) return null;
      }
      return {line: n, handle: line, text: line.text, gutterMarkers: line.gutterMarkers,
              textClass: line.textClass, bgClass: line.bgClass, wrapClass: line.wrapClass,
              widgets: line.widgets};
    },

    getViewport: function() { return {from: this.display.viewFrom, to: this.display.viewTo};},

    addWidget: function(pos, node, scroll, vert, horiz) {
      var display = this.display;
      pos = cursorCoords(this, clipPos(this.doc, pos));
      var top = pos.bottom, left = pos.left;
      node.style.position = "absolute";
      node.setAttribute("cm-ignore-events", "true");
      this.display.input.setUneditable(node);
      display.sizer.appendChild(node);
      if (vert == "over") {
        top = pos.top;
      } else if (vert == "above" || vert == "near") {
        var vspace = Math.max(display.wrapper.clientHeight, this.doc.height),
        hspace = Math.max(display.sizer.clientWidth, display.lineSpace.clientWidth);
        // Default to positioning above (if specified and possible); otherwise default to positioning below
        if ((vert == 'above' || pos.bottom + node.offsetHeight > vspace) && pos.top > node.offsetHeight)
          top = pos.top - node.offsetHeight;
        else if (pos.bottom + node.offsetHeight <= vspace)
          top = pos.bottom;
        if (left + node.offsetWidth > hspace)
          left = hspace - node.offsetWidth;
      }
      node.style.top = top + "px";
      node.style.left = node.style.right = "";
      if (horiz == "right") {
        left = display.sizer.clientWidth - node.offsetWidth;
        node.style.right = "0px";
      } else {
        if (horiz == "left") left = 0;
        else if (horiz == "middle") left = (display.sizer.clientWidth - node.offsetWidth) / 2;
        node.style.left = left + "px";
      }
      if (scroll)
        scrollIntoView(this, left, top, left + node.offsetWidth, top + node.offsetHeight);
    },

    triggerOnKeyDown: methodOp(onKeyDown),
    triggerOnKeyPress: methodOp(onKeyPress),
    triggerOnKeyUp: onKeyUp,

    execCommand: function(cmd) {
      if (commands.hasOwnProperty(cmd))
        return commands[cmd](this);
    },

    triggerElectric: methodOp(function(text) { triggerElectric(this, text); }),

    findPosH: function(from, amount, unit, visually) {
      var dir = 1;
      if (amount < 0) { dir = -1; amount = -amount; }
      for (var i = 0, cur = clipPos(this.doc, from); i < amount; ++i) {
        cur = findPosH(this.doc, cur, dir, unit, visually);
        if (cur.hitSide) break;
      }
      return cur;
    },

    moveH: methodOp(function(dir, unit) {
      var cm = this;
      cm.extendSelectionsBy(function(range) {
        if (cm.display.shift || cm.doc.extend || range.empty())
          return findPosH(cm.doc, range.head, dir, unit, cm.options.rtlMoveVisually);
        else
          return dir < 0 ? range.from() : range.to();
      }, sel_move);
    }),

    deleteH: methodOp(function(dir, unit) {
      var sel = this.doc.sel, doc = this.doc;
      if (sel.somethingSelected())
        doc.replaceSelection("", null, "+delete");
      else
        deleteNearSelection(this, function(range) {
          var other = findPosH(doc, range.head, dir, unit, false);
          return dir < 0 ? {from: other, to: range.head} : {from: range.head, to: other};
        });
    }),

    findPosV: function(from, amount, unit, goalColumn) {
      var dir = 1, x = goalColumn;
      if (amount < 0) { dir = -1; amount = -amount; }
      for (var i = 0, cur = clipPos(this.doc, from); i < amount; ++i) {
        var coords = cursorCoords(this, cur, "div");
        if (x == null) x = coords.left;
        else coords.left = x;
        cur = findPosV(this, coords, dir, unit);
        if (cur.hitSide) break;
      }
      return cur;
    },

    moveV: methodOp(function(dir, unit) {
      var cm = this, doc = this.doc, goals = [];
      var collapse = !cm.display.shift && !doc.extend && doc.sel.somethingSelected();
      doc.extendSelectionsBy(function(range) {
        if (collapse)
          return dir < 0 ? range.from() : range.to();
        var headPos = cursorCoords(cm, range.head, "div");
        if (range.goalColumn != null) headPos.left = range.goalColumn;
        goals.push(headPos.left);
        var pos = findPosV(cm, headPos, dir, unit);
        if (unit == "page" && range == doc.sel.primary())
          addToScrollPos(cm, null, charCoords(cm, pos, "div").top - headPos.top);
        return pos;
      }, sel_move);
      if (goals.length) for (var i = 0; i < doc.sel.ranges.length; i++)
        doc.sel.ranges[i].goalColumn = goals[i];
    }),

    // Find the word at the given position (as returned by coordsChar).
    findWordAt: function(pos) {
      var doc = this.doc, line = getLine(doc, pos.line).text;
      var start = pos.ch, end = pos.ch;
      if (line) {
        var helper = this.getHelper(pos, "wordChars");
        if ((pos.xRel < 0 || end == line.length) && start) --start; else ++end;
        var startChar = line.charAt(start);
        var check = isWordChar(startChar, helper)
          ? function(ch) { return isWordChar(ch, helper); }
          : /\s/.test(startChar) ? function(ch) {return /\s/.test(ch);}
          : function(ch) {return !/\s/.test(ch) && !isWordChar(ch);};
        while (start > 0 && check(line.charAt(start - 1))) --start;
        while (end < line.length && check(line.charAt(end))) ++end;
      }
      return new Range(Pos(pos.line, start), Pos(pos.line, end));
    },

    toggleOverwrite: function(value) {
      if (value != null && value == this.state.overwrite) return;
      if (this.state.overwrite = !this.state.overwrite)
        addClass(this.display.cursorDiv, "CodeMirror-overwrite");
      else
        rmClass(this.display.cursorDiv, "CodeMirror-overwrite");

      signal(this, "overwriteToggle", this, this.state.overwrite);
    },
    hasFocus: function() { return this.display.input.getField() == activeElt(); },

    scrollTo: methodOp(function(x, y) {
      if (x != null || y != null) resolveScrollToPos(this);
      if (x != null) this.curOp.scrollLeft = x;
      if (y != null) this.curOp.scrollTop = y;
    }),
    getScrollInfo: function() {
      var scroller = this.display.scroller;
      return {left: scroller.scrollLeft, top: scroller.scrollTop,
              height: scroller.scrollHeight - scrollGap(this) - this.display.barHeight,
              width: scroller.scrollWidth - scrollGap(this) - this.display.barWidth,
              clientHeight: displayHeight(this), clientWidth: displayWidth(this)};
    },

    scrollIntoView: methodOp(function(range, margin) {
      if (range == null) {
        range = {from: this.doc.sel.primary().head, to: null};
        if (margin == null) margin = this.options.cursorScrollMargin;
      } else if (typeof range == "number") {
        range = {from: Pos(range, 0), to: null};
      } else if (range.from == null) {
        range = {from: range, to: null};
      }
      if (!range.to) range.to = range.from;
      range.margin = margin || 0;

      if (range.from.line != null) {
        resolveScrollToPos(this);
        this.curOp.scrollToPos = range;
      } else {
        var sPos = calculateScrollPos(this, Math.min(range.from.left, range.to.left),
                                      Math.min(range.from.top, range.to.top) - range.margin,
                                      Math.max(range.from.right, range.to.right),
                                      Math.max(range.from.bottom, range.to.bottom) + range.margin);
        this.scrollTo(sPos.scrollLeft, sPos.scrollTop);
      }
    }),

    setSize: methodOp(function(width, height) {
      var cm = this;
      function interpret(val) {
        return typeof val == "number" || /^\d+$/.test(String(val)) ? val + "px" : val;
      }
      if (width != null) cm.display.wrapper.style.width = interpret(width);
      if (height != null) cm.display.wrapper.style.height = interpret(height);
      if (cm.options.lineWrapping) clearLineMeasurementCache(this);
      var lineNo = cm.display.viewFrom;
      cm.doc.iter(lineNo, cm.display.viewTo, function(line) {
        if (line.widgets) for (var i = 0; i < line.widgets.length; i++)
          if (line.widgets[i].noHScroll) { regLineChange(cm, lineNo, "widget"); break; }
        ++lineNo;
      });
      cm.curOp.forceUpdate = true;
      signal(cm, "refresh", this);
    }),

    operation: function(f){return runInOp(this, f);},

    refresh: methodOp(function() {
      var oldHeight = this.display.cachedTextHeight;
      regChange(this);
      this.curOp.forceUpdate = true;
      clearCaches(this);
      this.scrollTo(this.doc.scrollLeft, this.doc.scrollTop);
      updateGutterSpace(this);
      if (oldHeight == null || Math.abs(oldHeight - textHeight(this.display)) > .5)
        estimateLineHeights(this);
      signal(this, "refresh", this);
    }),

    swapDoc: methodOp(function(doc) {
      var old = this.doc;
      old.cm = null;
      attachDoc(this, doc);
      clearCaches(this);
      this.display.input.reset();
      this.scrollTo(doc.scrollLeft, doc.scrollTop);
      this.curOp.forceScroll = true;
      signalLater(this, "swapDoc", this, old);
      return old;
    }),

    getInputField: function(){return this.display.input.getField();},
    getWrapperElement: function(){return this.display.wrapper;},
    getScrollerElement: function(){return this.display.scroller;},
    getGutterElement: function(){return this.display.gutters;}
  };
  eventMixin(CodeMirror);

  // OPTION DEFAULTS

  // The default configuration options.
  var defaults = CodeMirror.defaults = {};
  // Functions to run when options are changed.
  var optionHandlers = CodeMirror.optionHandlers = {};

  function option(name, deflt, handle, notOnInit) {
    CodeMirror.defaults[name] = deflt;
    if (handle) optionHandlers[name] =
      notOnInit ? function(cm, val, old) {if (old != Init) handle(cm, val, old);} : handle;
  }

  // Passed to option handlers when there is no old value.
  var Init = CodeMirror.Init = {toString: function(){return "CodeMirror.Init";}};

  // These two are, on init, called from the constructor because they
  // have to be initialized before the editor can start at all.
  option("value", "", function(cm, val) {
    cm.setValue(val);
  }, true);
  option("mode", null, function(cm, val) {
    cm.doc.modeOption = val;
    loadMode(cm);
  }, true);

  option("indentUnit", 2, loadMode, true);
  option("indentWithTabs", false);
  option("smartIndent", true);
  option("tabSize", 4, function(cm) {
    resetModeState(cm);
    clearCaches(cm);
    regChange(cm);
  }, true);
  option("specialChars", /[\t\u0000-\u0019\u00ad\u200b-\u200f\u2028\u2029\ufeff]/g, function(cm, val, old) {
    cm.state.specialChars = new RegExp(val.source + (val.test("\t") ? "" : "|\t"), "g");
    if (old != CodeMirror.Init) cm.refresh();
  });
  option("specialCharPlaceholder", defaultSpecialCharPlaceholder, function(cm) {cm.refresh();}, true);
  option("electricChars", true);
  option("inputStyle", mobile ? "contenteditable" : "textarea", function() {
    throw new Error("inputStyle can not (yet) be changed in a running editor"); // FIXME
  }, true);
  option("rtlMoveVisually", !windows);
  option("wholeLineUpdateBefore", true);

  option("theme", "default", function(cm) {
    themeChanged(cm);
    guttersChanged(cm);
  }, true);
  option("keyMap", "default", function(cm, val, old) {
    var next = getKeyMap(val);
    var prev = old != CodeMirror.Init && getKeyMap(old);
    if (prev && prev.detach) prev.detach(cm, next);
    if (next.attach) next.attach(cm, prev || null);
  });
  option("extraKeys", null);

  option("lineWrapping", false, wrappingChanged, true);
  option("gutters", [], function(cm) {
    setGuttersForLineNumbers(cm.options);
    guttersChanged(cm);
  }, true);
  option("fixedGutter", true, function(cm, val) {
    cm.display.gutters.style.left = val ? compensateForHScroll(cm.display) + "px" : "0";
    cm.refresh();
  }, true);
  option("coverGutterNextToScrollbar", false, function(cm) {updateScrollbars(cm);}, true);
  option("scrollbarStyle", "native", function(cm) {
    initScrollbars(cm);
    updateScrollbars(cm);
    cm.display.scrollbars.setScrollTop(cm.doc.scrollTop);
    cm.display.scrollbars.setScrollLeft(cm.doc.scrollLeft);
  }, true);
  option("lineNumbers", false, function(cm) {
    setGuttersForLineNumbers(cm.options);
    guttersChanged(cm);
  }, true);
  option("firstLineNumber", 1, guttersChanged, true);
  option("lineNumberFormatter", function(integer) {return integer;}, guttersChanged, true);
  option("showCursorWhenSelecting", false, updateSelection, true);

  option("resetSelectionOnContextMenu", true);
  option("lineWiseCopyCut", true);

  option("readOnly", false, function(cm, val) {
    if (val == "nocursor") {
      onBlur(cm);
      cm.display.input.blur();
      cm.display.disabled = true;
    } else {
      cm.display.disabled = false;
      if (!val) cm.display.input.reset();
    }
  });
  option("disableInput", false, function(cm, val) {if (!val) cm.display.input.reset();}, true);
  option("dragDrop", true, dragDropChanged);

  option("cursorBlinkRate", 530);
  option("cursorScrollMargin", 0);
  option("cursorHeight", 1, updateSelection, true);
  option("singleCursorHeightPerLine", true, updateSelection, true);
  option("workTime", 100);
  option("workDelay", 100);
  option("flattenSpans", true, resetModeState, true);
  option("addModeClass", false, resetModeState, true);
  option("pollInterval", 100);
  option("undoDepth", 200, function(cm, val){cm.doc.history.undoDepth = val;});
  option("historyEventDelay", 1250);
  option("viewportMargin", 10, function(cm){cm.refresh();}, true);
  option("maxHighlightLength", 10000, resetModeState, true);
  option("moveInputWithCursor", true, function(cm, val) {
    if (!val) cm.display.input.resetPosition();
  });

  option("tabindex", null, function(cm, val) {
    cm.display.input.getField().tabIndex = val || "";
  });
  option("autofocus", null);

  // MODE DEFINITION AND QUERYING

  // Known modes, by name and by MIME
  var modes = CodeMirror.modes = {}, mimeModes = CodeMirror.mimeModes = {};

  // Extra arguments are stored as the mode's dependencies, which is
  // used by (legacy) mechanisms like loadmode.js to automatically
  // load a mode. (Preferred mechanism is the require/define calls.)
  CodeMirror.defineMode = function(name, mode) {
    if (!CodeMirror.defaults.mode && name != "null") CodeMirror.defaults.mode = name;
    if (arguments.length > 2)
      mode.dependencies = Array.prototype.slice.call(arguments, 2);
    modes[name] = mode;
  };

  CodeMirror.defineMIME = function(mime, spec) {
    mimeModes[mime] = spec;
  };

  // Given a MIME type, a {name, ...options} config object, or a name
  // string, return a mode config object.
  CodeMirror.resolveMode = function(spec) {
    if (typeof spec == "string" && mimeModes.hasOwnProperty(spec)) {
      spec = mimeModes[spec];
    } else if (spec && typeof spec.name == "string" && mimeModes.hasOwnProperty(spec.name)) {
      var found = mimeModes[spec.name];
      if (typeof found == "string") found = {name: found};
      spec = createObj(found, spec);
      spec.name = found.name;
    } else if (typeof spec == "string" && /^[\w\-]+\/[\w\-]+\+xml$/.test(spec)) {
      return CodeMirror.resolveMode("application/xml");
    }
    if (typeof spec == "string") return {name: spec};
    else return spec || {name: "null"};
  };

  // Given a mode spec (anything that resolveMode accepts), find and
  // initialize an actual mode object.
  CodeMirror.getMode = function(options, spec) {
    var spec = CodeMirror.resolveMode(spec);
    var mfactory = modes[spec.name];
    if (!mfactory) return CodeMirror.getMode(options, "text/plain");
    var modeObj = mfactory(options, spec);
    if (modeExtensions.hasOwnProperty(spec.name)) {
      var exts = modeExtensions[spec.name];
      for (var prop in exts) {
        if (!exts.hasOwnProperty(prop)) continue;
        if (modeObj.hasOwnProperty(prop)) modeObj["_" + prop] = modeObj[prop];
        modeObj[prop] = exts[prop];
      }
    }
    modeObj.name = spec.name;
    if (spec.helperType) modeObj.helperType = spec.helperType;
    if (spec.modeProps) for (var prop in spec.modeProps)
      modeObj[prop] = spec.modeProps[prop];

    return modeObj;
  };

  // Minimal default mode.
  CodeMirror.defineMode("null", function() {
    return {token: function(stream) {stream.skipToEnd();}};
  });
  CodeMirror.defineMIME("text/plain", "null");

  // This can be used to attach properties to mode objects from
  // outside the actual mode definition.
  var modeExtensions = CodeMirror.modeExtensions = {};
  CodeMirror.extendMode = function(mode, properties) {
    var exts = modeExtensions.hasOwnProperty(mode) ? modeExtensions[mode] : (modeExtensions[mode] = {});
    copyObj(properties, exts);
  };

  // EXTENSIONS

  CodeMirror.defineExtension = function(name, func) {
    CodeMirror.prototype[name] = func;
  };
  CodeMirror.defineDocExtension = function(name, func) {
    Doc.prototype[name] = func;
  };
  CodeMirror.defineOption = option;

  var initHooks = [];
  CodeMirror.defineInitHook = function(f) {initHooks.push(f);};

  var helpers = CodeMirror.helpers = {};
  CodeMirror.registerHelper = function(type, name, value) {
    if (!helpers.hasOwnProperty(type)) helpers[type] = CodeMirror[type] = {_global: []};
    helpers[type][name] = value;
  };
  CodeMirror.registerGlobalHelper = function(type, name, predicate, value) {
    CodeMirror.registerHelper(type, name, value);
    helpers[type]._global.push({pred: predicate, val: value});
  };

  // MODE STATE HANDLING

  // Utility functions for working with state. Exported because nested
  // modes need to do this for their inner modes.

  var copyState = CodeMirror.copyState = function(mode, state) {
    if (state === true) return state;
    if (mode.copyState) return mode.copyState(state);
    var nstate = {};
    for (var n in state) {
      var val = state[n];
      if (val instanceof Array) val = val.concat([]);
      nstate[n] = val;
    }
    return nstate;
  };

  var startState = CodeMirror.startState = function(mode, a1, a2) {
    return mode.startState ? mode.startState(a1, a2) : true;
  };

  // Given a mode and a state (for that mode), find the inner mode and
  // state at the position that the state refers to.
  CodeMirror.innerMode = function(mode, state) {
    while (mode.innerMode) {
      var info = mode.innerMode(state);
      if (!info || info.mode == mode) break;
      state = info.state;
      mode = info.mode;
    }
    return info || {mode: mode, state: state};
  };

  // STANDARD COMMANDS

  // Commands are parameter-less actions that can be performed on an
  // editor, mostly used for keybindings.
  var commands = CodeMirror.commands = {
    selectAll: function(cm) {cm.setSelection(Pos(cm.firstLine(), 0), Pos(cm.lastLine()), sel_dontScroll);},
    singleSelection: function(cm) {
      cm.setSelection(cm.getCursor("anchor"), cm.getCursor("head"), sel_dontScroll);
    },
    killLine: function(cm) {
      deleteNearSelection(cm, function(range) {
        if (range.empty()) {
          var len = getLine(cm.doc, range.head.line).text.length;
          if (range.head.ch == len && range.head.line < cm.lastLine())
            return {from: range.head, to: Pos(range.head.line + 1, 0)};
          else
            return {from: range.head, to: Pos(range.head.line, len)};
        } else {
          return {from: range.from(), to: range.to()};
        }
      });
    },
    deleteLine: function(cm) {
      deleteNearSelection(cm, function(range) {
        return {from: Pos(range.from().line, 0),
                to: clipPos(cm.doc, Pos(range.to().line + 1, 0))};
      });
    },
    delLineLeft: function(cm) {
      deleteNearSelection(cm, function(range) {
        return {from: Pos(range.from().line, 0), to: range.from()};
      });
    },
    delWrappedLineLeft: function(cm) {
      deleteNearSelection(cm, function(range) {
        var top = cm.charCoords(range.head, "div").top + 5;
        var leftPos = cm.coordsChar({left: 0, top: top}, "div");
        return {from: leftPos, to: range.from()};
      });
    },
    delWrappedLineRight: function(cm) {
      deleteNearSelection(cm, function(range) {
        var top = cm.charCoords(range.head, "div").top + 5;
        var rightPos = cm.coordsChar({left: cm.display.lineDiv.offsetWidth + 100, top: top}, "div");
        return {from: range.from(), to: rightPos };
      });
    },
    undo: function(cm) {cm.undo();},
    redo: function(cm) {cm.redo();},
    undoSelection: function(cm) {cm.undoSelection();},
    redoSelection: function(cm) {cm.redoSelection();},
    goDocStart: function(cm) {cm.extendSelection(Pos(cm.firstLine(), 0));},
    goDocEnd: function(cm) {cm.extendSelection(Pos(cm.lastLine()));},
    goLineStart: function(cm) {
      cm.extendSelectionsBy(function(range) { return lineStart(cm, range.head.line); },
                            {origin: "+move", bias: 1});
    },
    goLineStartSmart: function(cm) {
      cm.extendSelectionsBy(function(range) {
        return lineStartSmart(cm, range.head);
      }, {origin: "+move", bias: 1});
    },
    goLineEnd: function(cm) {
      cm.extendSelectionsBy(function(range) { return lineEnd(cm, range.head.line); },
                            {origin: "+move", bias: -1});
    },
    goLineRight: function(cm) {
      cm.extendSelectionsBy(function(range) {
        var top = cm.charCoords(range.head, "div").top + 5;
        return cm.coordsChar({left: cm.display.lineDiv.offsetWidth + 100, top: top}, "div");
      }, sel_move);
    },
    goLineLeft: function(cm) {
      cm.extendSelectionsBy(function(range) {
        var top = cm.charCoords(range.head, "div").top + 5;
        return cm.coordsChar({left: 0, top: top}, "div");
      }, sel_move);
    },
    goLineLeftSmart: function(cm) {
      cm.extendSelectionsBy(function(range) {
        var top = cm.charCoords(range.head, "div").top + 5;
        var pos = cm.coordsChar({left: 0, top: top}, "div");
        if (pos.ch < cm.getLine(pos.line).search(/\S/)) return lineStartSmart(cm, range.head);
        return pos;
      }, sel_move);
    },
    goLineUp: function(cm) {cm.moveV(-1, "line");},
    goLineDown: function(cm) {cm.moveV(1, "line");},
    goPageUp: function(cm) {cm.moveV(-1, "page");},
    goPageDown: function(cm) {cm.moveV(1, "page");},
    goCharLeft: function(cm) {cm.moveH(-1, "char");},
    goCharRight: function(cm) {cm.moveH(1, "char");},
    goColumnLeft: function(cm) {cm.moveH(-1, "column");},
    goColumnRight: function(cm) {cm.moveH(1, "column");},
    goWordLeft: function(cm) {cm.moveH(-1, "word");},
    goGroupRight: function(cm) {cm.moveH(1, "group");},
    goGroupLeft: function(cm) {cm.moveH(-1, "group");},
    goWordRight: function(cm) {cm.moveH(1, "word");},
    delCharBefore: function(cm) {cm.deleteH(-1, "char");},
    delCharAfter: function(cm) {cm.deleteH(1, "char");},
    delWordBefore: function(cm) {cm.deleteH(-1, "word");},
    delWordAfter: function(cm) {cm.deleteH(1, "word");},
    delGroupBefore: function(cm) {cm.deleteH(-1, "group");},
    delGroupAfter: function(cm) {cm.deleteH(1, "group");},
    indentAuto: function(cm) {cm.indentSelection("smart");},
    indentMore: function(cm) {cm.indentSelection("add");},
    indentLess: function(cm) {cm.indentSelection("subtract");},
    insertTab: function(cm) {cm.replaceSelection("\t");},
    insertSoftTab: function(cm) {
      var spaces = [], ranges = cm.listSelections(), tabSize = cm.options.tabSize;
      for (var i = 0; i < ranges.length; i++) {
        var pos = ranges[i].from();
        var col = countColumn(cm.getLine(pos.line), pos.ch, tabSize);
        spaces.push(new Array(tabSize - col % tabSize + 1).join(" "));
      }
      cm.replaceSelections(spaces);
    },
    defaultTab: function(cm) {
      if (cm.somethingSelected()) cm.indentSelection("add");
      else cm.execCommand("insertTab");
    },
    transposeChars: function(cm) {
      runInOp(cm, function() {
        var ranges = cm.listSelections(), newSel = [];
        for (var i = 0; i < ranges.length; i++) {
          var cur = ranges[i].head, line = getLine(cm.doc, cur.line).text;
          if (line) {
            if (cur.ch == line.length) cur = new Pos(cur.line, cur.ch - 1);
            if (cur.ch > 0) {
              cur = new Pos(cur.line, cur.ch + 1);
              cm.replaceRange(line.charAt(cur.ch - 1) + line.charAt(cur.ch - 2),
                              Pos(cur.line, cur.ch - 2), cur, "+transpose");
            } else if (cur.line > cm.doc.first) {
              var prev = getLine(cm.doc, cur.line - 1).text;
              if (prev)
                cm.replaceRange(line.charAt(0) + "\n" + prev.charAt(prev.length - 1),
                                Pos(cur.line - 1, prev.length - 1), Pos(cur.line, 1), "+transpose");
            }
          }
          newSel.push(new Range(cur, cur));
        }
        cm.setSelections(newSel);
      });
    },
    newlineAndIndent: function(cm) {
      runInOp(cm, function() {
        var len = cm.listSelections().length;
        for (var i = 0; i < len; i++) {
          var range = cm.listSelections()[i];
          cm.replaceRange("\n", range.anchor, range.head, "+input");
          cm.indentLine(range.from().line + 1, null, true);
          ensureCursorVisible(cm);
        }
      });
    },
    toggleOverwrite: function(cm) {cm.toggleOverwrite();}
  };


  // STANDARD KEYMAPS

  var keyMap = CodeMirror.keyMap = {};

  keyMap.basic = {
    "Left": "goCharLeft", "Right": "goCharRight", "Up": "goLineUp", "Down": "goLineDown",
    "End": "goLineEnd", "Home": "goLineStartSmart", "PageUp": "goPageUp", "PageDown": "goPageDown",
    "Delete": "delCharAfter", "Backspace": "delCharBefore", "Shift-Backspace": "delCharBefore",
    "Tab": "defaultTab", "Shift-Tab": "indentAuto",
    "Enter": "newlineAndIndent", "Insert": "toggleOverwrite",
    "Esc": "singleSelection"
  };
  // Note that the save and find-related commands aren't defined by
  // default. User code or addons can define them. Unknown commands
  // are simply ignored.
  keyMap.pcDefault = {
    "Ctrl-A": "selectAll", "Ctrl-D": "deleteLine", "Ctrl-Z": "undo", "Shift-Ctrl-Z": "redo", "Ctrl-Y": "redo",
    "Ctrl-Home": "goDocStart", "Ctrl-End": "goDocEnd", "Ctrl-Up": "goLineUp", "Ctrl-Down": "goLineDown",
    "Ctrl-Left": "goGroupLeft", "Ctrl-Right": "goGroupRight", "Alt-Left": "goLineStart", "Alt-Right": "goLineEnd",
    "Ctrl-Backspace": "delGroupBefore", "Ctrl-Delete": "delGroupAfter", "Ctrl-S": "save", "Ctrl-F": "find",
    "Ctrl-G": "findNext", "Shift-Ctrl-G": "findPrev", "Shift-Ctrl-F": "replace", "Shift-Ctrl-R": "replaceAll",
    "Ctrl-[": "indentLess", "Ctrl-]": "indentMore",
    "Ctrl-U": "undoSelection", "Shift-Ctrl-U": "redoSelection", "Alt-U": "redoSelection",
    fallthrough: "basic"
  };
  // Very basic readline/emacs-style bindings, which are standard on Mac.
  keyMap.emacsy = {
    "Ctrl-F": "goCharRight", "Ctrl-B": "goCharLeft", "Ctrl-P": "goLineUp", "Ctrl-N": "goLineDown",
    "Alt-F": "goWordRight", "Alt-B": "goWordLeft", "Ctrl-A": "goLineStart", "Ctrl-E": "goLineEnd",
    "Ctrl-V": "goPageDown", "Shift-Ctrl-V": "goPageUp", "Ctrl-D": "delCharAfter", "Ctrl-H": "delCharBefore",
    "Alt-D": "delWordAfter", "Alt-Backspace": "delWordBefore", "Ctrl-K": "killLine", "Ctrl-T": "transposeChars"
  };
  keyMap.macDefault = {
    "Cmd-A": "selectAll", "Cmd-D": "deleteLine", "Cmd-Z": "undo", "Shift-Cmd-Z": "redo", "Cmd-Y": "redo",
    "Cmd-Home": "goDocStart", "Cmd-Up": "goDocStart", "Cmd-End": "goDocEnd", "Cmd-Down": "goDocEnd", "Alt-Left": "goGroupLeft",
    "Alt-Right": "goGroupRight", "Cmd-Left": "goLineLeft", "Cmd-Right": "goLineRight", "Alt-Backspace": "delGroupBefore",
    "Ctrl-Alt-Backspace": "delGroupAfter", "Alt-Delete": "delGroupAfter", "Cmd-S": "save", "Cmd-F": "find",
    "Cmd-G": "findNext", "Shift-Cmd-G": "findPrev", "Cmd-Alt-F": "replace", "Shift-Cmd-Alt-F": "replaceAll",
    "Cmd-[": "indentLess", "Cmd-]": "indentMore", "Cmd-Backspace": "delWrappedLineLeft", "Cmd-Delete": "delWrappedLineRight",
    "Cmd-U": "undoSelection", "Shift-Cmd-U": "redoSelection", "Ctrl-Up": "goDocStart", "Ctrl-Down": "goDocEnd",
    fallthrough: ["basic", "emacsy"]
  };
  keyMap["default"] = mac ? keyMap.macDefault : keyMap.pcDefault;

  // KEYMAP DISPATCH

  function normalizeKeyName(name) {
    var parts = name.split(/-(?!$)/), name = parts[parts.length - 1];
    var alt, ctrl, shift, cmd;
    for (var i = 0; i < parts.length - 1; i++) {
      var mod = parts[i];
      if (/^(cmd|meta|m)$/i.test(mod)) cmd = true;
      else if (/^a(lt)?$/i.test(mod)) alt = true;
      else if (/^(c|ctrl|control)$/i.test(mod)) ctrl = true;
      else if (/^s(hift)$/i.test(mod)) shift = true;
      else throw new Error("Unrecognized modifier name: " + mod);
    }
    if (alt) name = "Alt-" + name;
    if (ctrl) name = "Ctrl-" + name;
    if (cmd) name = "Cmd-" + name;
    if (shift) name = "Shift-" + name;
    return name;
  }

  // This is a kludge to keep keymaps mostly working as raw objects
  // (backwards compatibility) while at the same time support features
  // like normalization and multi-stroke key bindings. It compiles a
  // new normalized keymap, and then updates the old object to reflect
  // this.
  CodeMirror.normalizeKeyMap = function(keymap) {
    var copy = {};
    for (var keyname in keymap) if (keymap.hasOwnProperty(keyname)) {
      var value = keymap[keyname];
      if (/^(name|fallthrough|(de|at)tach)$/.test(keyname)) continue;
      if (value == "...") { delete keymap[keyname]; continue; }

      var keys = map(keyname.split(" "), normalizeKeyName);
      for (var i = 0; i < keys.length; i++) {
        var val, name;
        if (i == keys.length - 1) {
          name = keys.join(" ");
          val = value;
        } else {
          name = keys.slice(0, i + 1).join(" ");
          val = "...";
        }
        var prev = copy[name];
        if (!prev) copy[name] = val;
        else if (prev != val) throw new Error("Inconsistent bindings for " + name);
      }
      delete keymap[keyname];
    }
    for (var prop in copy) keymap[prop] = copy[prop];
    return keymap;
  };

  var lookupKey = CodeMirror.lookupKey = function(key, map, handle, context) {
    map = getKeyMap(map);
    var found = map.call ? map.call(key, context) : map[key];
    if (found === false) return "nothing";
    if (found === "...") return "multi";
    if (found != null && handle(found)) return "handled";

    if (map.fallthrough) {
      if (Object.prototype.toString.call(map.fallthrough) != "[object Array]")
        return lookupKey(key, map.fallthrough, handle, context);
      for (var i = 0; i < map.fallthrough.length; i++) {
        var result = lookupKey(key, map.fallthrough[i], handle, context);
        if (result) return result;
      }
    }
  };

  // Modifier key presses don't count as 'real' key presses for the
  // purpose of keymap fallthrough.
  var isModifierKey = CodeMirror.isModifierKey = function(value) {
    var name = typeof value == "string" ? value : keyNames[value.keyCode];
    return name == "Ctrl" || name == "Alt" || name == "Shift" || name == "Mod";
  };

  // Look up the name of a key as indicated by an event object.
  var keyName = CodeMirror.keyName = function(event, noShift) {
    if (presto && event.keyCode == 34 && event["char"]) return false;
    var base = keyNames[event.keyCode], name = base;
    if (name == null || event.altGraphKey) return false;
    if (event.altKey && base != "Alt") name = "Alt-" + name;
    if ((flipCtrlCmd ? event.metaKey : event.ctrlKey) && base != "Ctrl") name = "Ctrl-" + name;
    if ((flipCtrlCmd ? event.ctrlKey : event.metaKey) && base != "Cmd") name = "Cmd-" + name;
    if (!noShift && event.shiftKey && base != "Shift") name = "Shift-" + name;
    return name;
  };

  function getKeyMap(val) {
    return typeof val == "string" ? keyMap[val] : val;
  }

  // FROMTEXTAREA

  CodeMirror.fromTextArea = function(textarea, options) {
    options = options ? copyObj(options) : {};
    options.value = textarea.value;
    if (!options.tabindex && textarea.tabIndex)
      options.tabindex = textarea.tabIndex;
    if (!options.placeholder && textarea.placeholder)
      options.placeholder = textarea.placeholder;
    // Set autofocus to true if this textarea is focused, or if it has
    // autofocus and no other element is focused.
    if (options.autofocus == null) {
      var hasFocus = activeElt();
      options.autofocus = hasFocus == textarea ||
        textarea.getAttribute("autofocus") != null && hasFocus == document.body;
    }

    function save() {textarea.value = cm.getValue();}
    if (textarea.form) {
      on(textarea.form, "submit", save);
      // Deplorable hack to make the submit method do the right thing.
      if (!options.leaveSubmitMethodAlone) {
        var form = textarea.form, realSubmit = form.submit;
        try {
          var wrappedSubmit = form.submit = function() {
            save();
            form.submit = realSubmit;
            form.submit();
            form.submit = wrappedSubmit;
          };
        } catch(e) {}
      }
    }

    options.finishInit = function(cm) {
      cm.save = save;
      cm.getTextArea = function() { return textarea; };
      cm.toTextArea = function() {
        cm.toTextArea = isNaN; // Prevent this from being ran twice
        save();
        textarea.parentNode.removeChild(cm.getWrapperElement());
        textarea.style.display = "";
        if (textarea.form) {
          off(textarea.form, "submit", save);
          if (typeof textarea.form.submit == "function")
            textarea.form.submit = realSubmit;
        }
      };
    };

    textarea.style.display = "none";
    var cm = CodeMirror(function(node) {
      textarea.parentNode.insertBefore(node, textarea.nextSibling);
    }, options);
    return cm;
  };

  // STRING STREAM

  // Fed to the mode parsers, provides helper functions to make
  // parsers more succinct.

  var StringStream = CodeMirror.StringStream = function(string, tabSize) {
    this.pos = this.start = 0;
    this.string = string;
    this.tabSize = tabSize || 8;
    this.lastColumnPos = this.lastColumnValue = 0;
    this.lineStart = 0;
  };

  StringStream.prototype = {
    eol: function() {return this.pos >= this.string.length;},
    sol: function() {return this.pos == this.lineStart;},
    peek: function() {return this.string.charAt(this.pos) || undefined;},
    next: function() {
      if (this.pos < this.string.length)
        return this.string.charAt(this.pos++);
    },
    eat: function(match) {
      var ch = this.string.charAt(this.pos);
      if (typeof match == "string") var ok = ch == match;
      else var ok = ch && (match.test ? match.test(ch) : match(ch));
      if (ok) {++this.pos; return ch;}
    },
    eatWhile: function(match) {
      var start = this.pos;
      while (this.eat(match)){}
      return this.pos > start;
    },
    eatSpace: function() {
      var start = this.pos;
      while (/[\s\u00a0]/.test(this.string.charAt(this.pos))) ++this.pos;
      return this.pos > start;
    },
    skipToEnd: function() {this.pos = this.string.length;},
    skipTo: function(ch) {
      var found = this.string.indexOf(ch, this.pos);
      if (found > -1) {this.pos = found; return true;}
    },
    backUp: function(n) {this.pos -= n;},
    column: function() {
      if (this.lastColumnPos < this.start) {
        this.lastColumnValue = countColumn(this.string, this.start, this.tabSize, this.lastColumnPos, this.lastColumnValue);
        this.lastColumnPos = this.start;
      }
      return this.lastColumnValue - (this.lineStart ? countColumn(this.string, this.lineStart, this.tabSize) : 0);
    },
    indentation: function() {
      return countColumn(this.string, null, this.tabSize) -
        (this.lineStart ? countColumn(this.string, this.lineStart, this.tabSize) : 0);
    },
    match: function(pattern, consume, caseInsensitive) {
      if (typeof pattern == "string") {
        var cased = function(str) {return caseInsensitive ? str.toLowerCase() : str;};
        var substr = this.string.substr(this.pos, pattern.length);
        if (cased(substr) == cased(pattern)) {
          if (consume !== false) this.pos += pattern.length;
          return true;
        }
      } else {
        var match = this.string.slice(this.pos).match(pattern);
        if (match && match.index > 0) return null;
        if (match && consume !== false) this.pos += match[0].length;
        return match;
      }
    },
    current: function(){return this.string.slice(this.start, this.pos);},
    hideFirstChars: function(n, inner) {
      this.lineStart += n;
      try { return inner(); }
      finally { this.lineStart -= n; }
    }
  };

  // TEXTMARKERS

  // Created with markText and setBookmark methods. A TextMarker is a
  // handle that can be used to clear or find a marked position in the
  // document. Line objects hold arrays (markedSpans) containing
  // {from, to, marker} object pointing to such marker objects, and
  // indicating that such a marker is present on that line. Multiple
  // lines may point to the same marker when it spans across lines.
  // The spans will have null for their from/to properties when the
  // marker continues beyond the start/end of the line. Markers have
  // links back to the lines they currently touch.

  var nextMarkerId = 0;

  var TextMarker = CodeMirror.TextMarker = function(doc, type) {
    this.lines = [];
    this.type = type;
    this.doc = doc;
    this.id = ++nextMarkerId;
  };
  eventMixin(TextMarker);

  // Clear the marker.
  TextMarker.prototype.clear = function() {
    if (this.explicitlyCleared) return;
    var cm = this.doc.cm, withOp = cm && !cm.curOp;
    if (withOp) startOperation(cm);
    if (hasHandler(this, "clear")) {
      var found = this.find();
      if (found) signalLater(this, "clear", found.from, found.to);
    }
    var min = null, max = null;
    for (var i = 0; i < this.lines.length; ++i) {
      var line = this.lines[i];
      var span = getMarkedSpanFor(line.markedSpans, this);
      if (cm && !this.collapsed) regLineChange(cm, lineNo(line), "text");
      else if (cm) {
        if (span.to != null) max = lineNo(line);
        if (span.from != null) min = lineNo(line);
      }
      line.markedSpans = removeMarkedSpan(line.markedSpans, span);
      if (span.from == null && this.collapsed && !lineIsHidden(this.doc, line) && cm)
        updateLineHeight(line, textHeight(cm.display));
    }
    if (cm && this.collapsed && !cm.options.lineWrapping) for (var i = 0; i < this.lines.length; ++i) {
      var visual = visualLine(this.lines[i]), len = lineLength(visual);
      if (len > cm.display.maxLineLength) {
        cm.display.maxLine = visual;
        cm.display.maxLineLength = len;
        cm.display.maxLineChanged = true;
      }
    }

    if (min != null && cm && this.collapsed) regChange(cm, min, max + 1);
    this.lines.length = 0;
    this.explicitlyCleared = true;
    if (this.atomic && this.doc.cantEdit) {
      this.doc.cantEdit = false;
      if (cm) reCheckSelection(cm.doc);
    }
    if (cm) signalLater(cm, "markerCleared", cm, this);
    if (withOp) endOperation(cm);
    if (this.parent) this.parent.clear();
  };

  // Find the position of the marker in the document. Returns a {from,
  // to} object by default. Side can be passed to get a specific side
  // -- 0 (both), -1 (left), or 1 (right). When lineObj is true, the
  // Pos objects returned contain a line object, rather than a line
  // number (used to prevent looking up the same line twice).
  TextMarker.prototype.find = function(side, lineObj) {
    if (side == null && this.type == "bookmark") side = 1;
    var from, to;
    for (var i = 0; i < this.lines.length; ++i) {
      var line = this.lines[i];
      var span = getMarkedSpanFor(line.markedSpans, this);
      if (span.from != null) {
        from = Pos(lineObj ? line : lineNo(line), span.from);
        if (side == -1) return from;
      }
      if (span.to != null) {
        to = Pos(lineObj ? line : lineNo(line), span.to);
        if (side == 1) return to;
      }
    }
    return from && {from: from, to: to};
  };

  // Signals that the marker's widget changed, and surrounding layout
  // should be recomputed.
  TextMarker.prototype.changed = function() {
    var pos = this.find(-1, true), widget = this, cm = this.doc.cm;
    if (!pos || !cm) return;
    runInOp(cm, function() {
      var line = pos.line, lineN = lineNo(pos.line);
      var view = findViewForLine(cm, lineN);
      if (view) {
        clearLineMeasurementCacheFor(view);
        cm.curOp.selectionChanged = cm.curOp.forceUpdate = true;
      }
      cm.curOp.updateMaxLine = true;
      if (!lineIsHidden(widget.doc, line) && widget.height != null) {
        var oldHeight = widget.height;
        widget.height = null;
        var dHeight = widgetHeight(widget) - oldHeight;
        if (dHeight)
          updateLineHeight(line, line.height + dHeight);
      }
    });
  };

  TextMarker.prototype.attachLine = function(line) {
    if (!this.lines.length && this.doc.cm) {
      var op = this.doc.cm.curOp;
      if (!op.maybeHiddenMarkers || indexOf(op.maybeHiddenMarkers, this) == -1)
        (op.maybeUnhiddenMarkers || (op.maybeUnhiddenMarkers = [])).push(this);
    }
    this.lines.push(line);
  };
  TextMarker.prototype.detachLine = function(line) {
    this.lines.splice(indexOf(this.lines, line), 1);
    if (!this.lines.length && this.doc.cm) {
      var op = this.doc.cm.curOp;
      (op.maybeHiddenMarkers || (op.maybeHiddenMarkers = [])).push(this);
    }
  };

  // Collapsed markers have unique ids, in order to be able to order
  // them, which is needed for uniquely determining an outer marker
  // when they overlap (they may nest, but not partially overlap).
  var nextMarkerId = 0;

  // Create a marker, wire it up to the right lines, and
  function markText(doc, from, to, options, type) {
    // Shared markers (across linked documents) are handled separately
    // (markTextShared will call out to this again, once per
    // document).
    if (options && options.shared) return markTextShared(doc, from, to, options, type);
    // Ensure we are in an operation.
    if (doc.cm && !doc.cm.curOp) return operation(doc.cm, markText)(doc, from, to, options, type);

    var marker = new TextMarker(doc, type), diff = cmp(from, to);
    if (options) copyObj(options, marker, false);
    // Don't connect empty markers unless clearWhenEmpty is false
    if (diff > 0 || diff == 0 && marker.clearWhenEmpty !== false)
      return marker;
    if (marker.replacedWith) {
      // Showing up as a widget implies collapsed (widget replaces text)
      marker.collapsed = true;
      marker.widgetNode = elt("span", [marker.replacedWith], "CodeMirror-widget");
      if (!options.handleMouseEvents) marker.widgetNode.setAttribute("cm-ignore-events", "true");
      if (options.insertLeft) marker.widgetNode.insertLeft = true;
    }
    if (marker.collapsed) {
      if (conflictingCollapsedRange(doc, from.line, from, to, marker) ||
          from.line != to.line && conflictingCollapsedRange(doc, to.line, from, to, marker))
        throw new Error("Inserting collapsed marker partially overlapping an existing one");
      sawCollapsedSpans = true;
    }

    if (marker.addToHistory)
      addChangeToHistory(doc, {from: from, to: to, origin: "markText"}, doc.sel, NaN);

    var curLine = from.line, cm = doc.cm, updateMaxLine;
    doc.iter(curLine, to.line + 1, function(line) {
      if (cm && marker.collapsed && !cm.options.lineWrapping && visualLine(line) == cm.display.maxLine)
        updateMaxLine = true;
      if (marker.collapsed && curLine != from.line) updateLineHeight(line, 0);
      addMarkedSpan(line, new MarkedSpan(marker,
                                         curLine == from.line ? from.ch : null,
                                         curLine == to.line ? to.ch : null));
      ++curLine;
    });
    // lineIsHidden depends on the presence of the spans, so needs a second pass
    if (marker.collapsed) doc.iter(from.line, to.line + 1, function(line) {
      if (lineIsHidden(doc, line)) updateLineHeight(line, 0);
    });

    if (marker.clearOnEnter) on(marker, "beforeCursorEnter", function() { marker.clear(); });

    if (marker.readOnly) {
      sawReadOnlySpans = true;
      if (doc.history.done.length || doc.history.undone.length)
        doc.clearHistory();
    }
    if (marker.collapsed) {
      marker.id = ++nextMarkerId;
      marker.atomic = true;
    }
    if (cm) {
      // Sync editor state
      if (updateMaxLine) cm.curOp.updateMaxLine = true;
      if (marker.collapsed)
        regChange(cm, from.line, to.line + 1);
      else if (marker.className || marker.title || marker.startStyle || marker.endStyle || marker.css)
        for (var i = from.line; i <= to.line; i++) regLineChange(cm, i, "text");
      if (marker.atomic) reCheckSelection(cm.doc);
      signalLater(cm, "markerAdded", cm, marker);
    }
    return marker;
  }

  // SHARED TEXTMARKERS

  // A shared marker spans multiple linked documents. It is
  // implemented as a meta-marker-object controlling multiple normal
  // markers.
  var SharedTextMarker = CodeMirror.SharedTextMarker = function(markers, primary) {
    this.markers = markers;
    this.primary = primary;
    for (var i = 0; i < markers.length; ++i)
      markers[i].parent = this;
  };
  eventMixin(SharedTextMarker);

  SharedTextMarker.prototype.clear = function() {
    if (this.explicitlyCleared) return;
    this.explicitlyCleared = true;
    for (var i = 0; i < this.markers.length; ++i)
      this.markers[i].clear();
    signalLater(this, "clear");
  };
  SharedTextMarker.prototype.find = function(side, lineObj) {
    return this.primary.find(side, lineObj);
  };

  function markTextShared(doc, from, to, options, type) {
    options = copyObj(options);
    options.shared = false;
    var markers = [markText(doc, from, to, options, type)], primary = markers[0];
    var widget = options.widgetNode;
    linkedDocs(doc, function(doc) {
      if (widget) options.widgetNode = widget.cloneNode(true);
      markers.push(markText(doc, clipPos(doc, from), clipPos(doc, to), options, type));
      for (var i = 0; i < doc.linked.length; ++i)
        if (doc.linked[i].isParent) return;
      primary = lst(markers);
    });
    return new SharedTextMarker(markers, primary);
  }

  function findSharedMarkers(doc) {
    return doc.findMarks(Pos(doc.first, 0), doc.clipPos(Pos(doc.lastLine())),
                         function(m) { return m.parent; });
  }

  function copySharedMarkers(doc, markers) {
    for (var i = 0; i < markers.length; i++) {
      var marker = markers[i], pos = marker.find();
      var mFrom = doc.clipPos(pos.from), mTo = doc.clipPos(pos.to);
      if (cmp(mFrom, mTo)) {
        var subMark = markText(doc, mFrom, mTo, marker.primary, marker.primary.type);
        marker.markers.push(subMark);
        subMark.parent = marker;
      }
    }
  }

  function detachSharedMarkers(markers) {
    for (var i = 0; i < markers.length; i++) {
      var marker = markers[i], linked = [marker.primary.doc];;
      linkedDocs(marker.primary.doc, function(d) { linked.push(d); });
      for (var j = 0; j < marker.markers.length; j++) {
        var subMarker = marker.markers[j];
        if (indexOf(linked, subMarker.doc) == -1) {
          subMarker.parent = null;
          marker.markers.splice(j--, 1);
        }
      }
    }
  }

  // TEXTMARKER SPANS

  function MarkedSpan(marker, from, to) {
    this.marker = marker;
    this.from = from; this.to = to;
  }

  // Search an array of spans for a span matching the given marker.
  function getMarkedSpanFor(spans, marker) {
    if (spans) for (var i = 0; i < spans.length; ++i) {
      var span = spans[i];
      if (span.marker == marker) return span;
    }
  }
  // Remove a span from an array, returning undefined if no spans are
  // left (we don't store arrays for lines without spans).
  function removeMarkedSpan(spans, span) {
    for (var r, i = 0; i < spans.length; ++i)
      if (spans[i] != span) (r || (r = [])).push(spans[i]);
    return r;
  }
  // Add a span to a line.
  function addMarkedSpan(line, span) {
    line.markedSpans = line.markedSpans ? line.markedSpans.concat([span]) : [span];
    span.marker.attachLine(line);
  }

  // Used for the algorithm that adjusts markers for a change in the
  // document. These functions cut an array of spans at a given
  // character position, returning an array of remaining chunks (or
  // undefined if nothing remains).
  function markedSpansBefore(old, startCh, isInsert) {
    if (old) for (var i = 0, nw; i < old.length; ++i) {
      var span = old[i], marker = span.marker;
      var startsBefore = span.from == null || (marker.inclusiveLeft ? span.from <= startCh : span.from < startCh);
      if (startsBefore || span.from == startCh && marker.type == "bookmark" && (!isInsert || !span.marker.insertLeft)) {
        var endsAfter = span.to == null || (marker.inclusiveRight ? span.to >= startCh : span.to > startCh);
        (nw || (nw = [])).push(new MarkedSpan(marker, span.from, endsAfter ? null : span.to));
      }
    }
    return nw;
  }
  function markedSpansAfter(old, endCh, isInsert) {
    if (old) for (var i = 0, nw; i < old.length; ++i) {
      var span = old[i], marker = span.marker;
      var endsAfter = span.to == null || (marker.inclusiveRight ? span.to >= endCh : span.to > endCh);
      if (endsAfter || span.from == endCh && marker.type == "bookmark" && (!isInsert || span.marker.insertLeft)) {
        var startsBefore = span.from == null || (marker.inclusiveLeft ? span.from <= endCh : span.from < endCh);
        (nw || (nw = [])).push(new MarkedSpan(marker, startsBefore ? null : span.from - endCh,
                                              span.to == null ? null : span.to - endCh));
      }
    }
    return nw;
  }

  // Given a change object, compute the new set of marker spans that
  // cover the line in which the change took place. Removes spans
  // entirely within the change, reconnects spans belonging to the
  // same marker that appear on both sides of the change, and cuts off
  // spans partially within the change. Returns an array of span
  // arrays with one element for each line in (after) the change.
  function stretchSpansOverChange(doc, change) {
    if (change.full) return null;
    var oldFirst = isLine(doc, change.from.line) && getLine(doc, change.from.line).markedSpans;
    var oldLast = isLine(doc, change.to.line) && getLine(doc, change.to.line).markedSpans;
    if (!oldFirst && !oldLast) return null;

    var startCh = change.from.ch, endCh = change.to.ch, isInsert = cmp(change.from, change.to) == 0;
    // Get the spans that 'stick out' on both sides
    var first = markedSpansBefore(oldFirst, startCh, isInsert);
    var last = markedSpansAfter(oldLast, endCh, isInsert);

    // Next, merge those two ends
    var sameLine = change.text.length == 1, offset = lst(change.text).length + (sameLine ? startCh : 0);
    if (first) {
      // Fix up .to properties of first
      for (var i = 0; i < first.length; ++i) {
        var span = first[i];
        if (span.to == null) {
          var found = getMarkedSpanFor(last, span.marker);
          if (!found) span.to = startCh;
          else if (sameLine) span.to = found.to == null ? null : found.to + offset;
        }
      }
    }
    if (last) {
      // Fix up .from in last (or move them into first in case of sameLine)
      for (var i = 0; i < last.length; ++i) {
        var span = last[i];
        if (span.to != null) span.to += offset;
        if (span.from == null) {
          var found = getMarkedSpanFor(first, span.marker);
          if (!found) {
            span.from = offset;
            if (sameLine) (first || (first = [])).push(span);
          }
        } else {
          span.from += offset;
          if (sameLine) (first || (first = [])).push(span);
        }
      }
    }
    // Make sure we didn't create any zero-length spans
    if (first) first = clearEmptySpans(first);
    if (last && last != first) last = clearEmptySpans(last);

    var newMarkers = [first];
    if (!sameLine) {
      // Fill gap with whole-line-spans
      var gap = change.text.length - 2, gapMarkers;
      if (gap > 0 && first)
        for (var i = 0; i < first.length; ++i)
          if (first[i].to == null)
            (gapMarkers || (gapMarkers = [])).push(new MarkedSpan(first[i].marker, null, null));
      for (var i = 0; i < gap; ++i)
        newMarkers.push(gapMarkers);
      newMarkers.push(last);
    }
    return newMarkers;
  }

  // Remove spans that are empty and don't have a clearWhenEmpty
  // option of false.
  function clearEmptySpans(spans) {
    for (var i = 0; i < spans.length; ++i) {
      var span = spans[i];
      if (span.from != null && span.from == span.to && span.marker.clearWhenEmpty !== false)
        spans.splice(i--, 1);
    }
    if (!spans.length) return null;
    return spans;
  }

  // Used for un/re-doing changes from the history. Combines the
  // result of computing the existing spans with the set of spans that
  // existed in the history (so that deleting around a span and then
  // undoing brings back the span).
  function mergeOldSpans(doc, change) {
    var old = getOldSpans(doc, change);
    var stretched = stretchSpansOverChange(doc, change);
    if (!old) return stretched;
    if (!stretched) return old;

    for (var i = 0; i < old.length; ++i) {
      var oldCur = old[i], stretchCur = stretched[i];
      if (oldCur && stretchCur) {
        spans: for (var j = 0; j < stretchCur.length; ++j) {
          var span = stretchCur[j];
          for (var k = 0; k < oldCur.length; ++k)
            if (oldCur[k].marker == span.marker) continue spans;
          oldCur.push(span);
        }
      } else if (stretchCur) {
        old[i] = stretchCur;
      }
    }
    return old;
  }

  // Used to 'clip' out readOnly ranges when making a change.
  function removeReadOnlyRanges(doc, from, to) {
    var markers = null;
    doc.iter(from.line, to.line + 1, function(line) {
      if (line.markedSpans) for (var i = 0; i < line.markedSpans.length; ++i) {
        var mark = line.markedSpans[i].marker;
        if (mark.readOnly && (!markers || indexOf(markers, mark) == -1))
          (markers || (markers = [])).push(mark);
      }
    });
    if (!markers) return null;
    var parts = [{from: from, to: to}];
    for (var i = 0; i < markers.length; ++i) {
      var mk = markers[i], m = mk.find(0);
      for (var j = 0; j < parts.length; ++j) {
        var p = parts[j];
        if (cmp(p.to, m.from) < 0 || cmp(p.from, m.to) > 0) continue;
        var newParts = [j, 1], dfrom = cmp(p.from, m.from), dto = cmp(p.to, m.to);
        if (dfrom < 0 || !mk.inclusiveLeft && !dfrom)
          newParts.push({from: p.from, to: m.from});
        if (dto > 0 || !mk.inclusiveRight && !dto)
          newParts.push({from: m.to, to: p.to});
        parts.splice.apply(parts, newParts);
        j += newParts.length - 1;
      }
    }
    return parts;
  }

  // Connect or disconnect spans from a line.
  function detachMarkedSpans(line) {
    var spans = line.markedSpans;
    if (!spans) return;
    for (var i = 0; i < spans.length; ++i)
      spans[i].marker.detachLine(line);
    line.markedSpans = null;
  }
  function attachMarkedSpans(line, spans) {
    if (!spans) return;
    for (var i = 0; i < spans.length; ++i)
      spans[i].marker.attachLine(line);
    line.markedSpans = spans;
  }

  // Helpers used when computing which overlapping collapsed span
  // counts as the larger one.
  function extraLeft(marker) { return marker.inclusiveLeft ? -1 : 0; }
  function extraRight(marker) { return marker.inclusiveRight ? 1 : 0; }

  // Returns a number indicating which of two overlapping collapsed
  // spans is larger (and thus includes the other). Falls back to
  // comparing ids when the spans cover exactly the same range.
  function compareCollapsedMarkers(a, b) {
    var lenDiff = a.lines.length - b.lines.length;
    if (lenDiff != 0) return lenDiff;
    var aPos = a.find(), bPos = b.find();
    var fromCmp = cmp(aPos.from, bPos.from) || extraLeft(a) - extraLeft(b);
    if (fromCmp) return -fromCmp;
    var toCmp = cmp(aPos.to, bPos.to) || extraRight(a) - extraRight(b);
    if (toCmp) return toCmp;
    return b.id - a.id;
  }

  // Find out whether a line ends or starts in a collapsed span. If
  // so, return the marker for that span.
  function collapsedSpanAtSide(line, start) {
    var sps = sawCollapsedSpans && line.markedSpans, found;
    if (sps) for (var sp, i = 0; i < sps.length; ++i) {
      sp = sps[i];
      if (sp.marker.collapsed && (start ? sp.from : sp.to) == null &&
          (!found || compareCollapsedMarkers(found, sp.marker) < 0))
        found = sp.marker;
    }
    return found;
  }
  function collapsedSpanAtStart(line) { return collapsedSpanAtSide(line, true); }
  function collapsedSpanAtEnd(line) { return collapsedSpanAtSide(line, false); }

  // Test whether there exists a collapsed span that partially
  // overlaps (covers the start or end, but not both) of a new span.
  // Such overlap is not allowed.
  function conflictingCollapsedRange(doc, lineNo, from, to, marker) {
    var line = getLine(doc, lineNo);
    var sps = sawCollapsedSpans && line.markedSpans;
    if (sps) for (var i = 0; i < sps.length; ++i) {
      var sp = sps[i];
      if (!sp.marker.collapsed) continue;
      var found = sp.marker.find(0);
      var fromCmp = cmp(found.from, from) || extraLeft(sp.marker) - extraLeft(marker);
      var toCmp = cmp(found.to, to) || extraRight(sp.marker) - extraRight(marker);
      if (fromCmp >= 0 && toCmp <= 0 || fromCmp <= 0 && toCmp >= 0) continue;
      if (fromCmp <= 0 && (cmp(found.to, from) > 0 || (sp.marker.inclusiveRight && marker.inclusiveLeft)) ||
          fromCmp >= 0 && (cmp(found.from, to) < 0 || (sp.marker.inclusiveLeft && marker.inclusiveRight)))
        return true;
    }
  }

  // A visual line is a line as drawn on the screen. Folding, for
  // example, can cause multiple logical lines to appear on the same
  // visual line. This finds the start of the visual line that the
  // given line is part of (usually that is the line itself).
  function visualLine(line) {
    var merged;
    while (merged = collapsedSpanAtStart(line))
      line = merged.find(-1, true).line;
    return line;
  }

  // Returns an array of logical lines that continue the visual line
  // started by the argument, or undefined if there are no such lines.
  function visualLineContinued(line) {
    var merged, lines;
    while (merged = collapsedSpanAtEnd(line)) {
      line = merged.find(1, true).line;
      (lines || (lines = [])).push(line);
    }
    return lines;
  }

  // Get the line number of the start of the visual line that the
  // given line number is part of.
  function visualLineNo(doc, lineN) {
    var line = getLine(doc, lineN), vis = visualLine(line);
    if (line == vis) return lineN;
    return lineNo(vis);
  }
  // Get the line number of the start of the next visual line after
  // the given line.
  function visualLineEndNo(doc, lineN) {
    if (lineN > doc.lastLine()) return lineN;
    var line = getLine(doc, lineN), merged;
    if (!lineIsHidden(doc, line)) return lineN;
    while (merged = collapsedSpanAtEnd(line))
      line = merged.find(1, true).line;
    return lineNo(line) + 1;
  }

  // Compute whether a line is hidden. Lines count as hidden when they
  // are part of a visual line that starts with another line, or when
  // they are entirely covered by collapsed, non-widget span.
  function lineIsHidden(doc, line) {
    var sps = sawCollapsedSpans && line.markedSpans;
    if (sps) for (var sp, i = 0; i < sps.length; ++i) {
      sp = sps[i];
      if (!sp.marker.collapsed) continue;
      if (sp.from == null) return true;
      if (sp.marker.widgetNode) continue;
      if (sp.from == 0 && sp.marker.inclusiveLeft && lineIsHiddenInner(doc, line, sp))
        return true;
    }
  }
  function lineIsHiddenInner(doc, line, span) {
    if (span.to == null) {
      var end = span.marker.find(1, true);
      return lineIsHiddenInner(doc, end.line, getMarkedSpanFor(end.line.markedSpans, span.marker));
    }
    if (span.marker.inclusiveRight && span.to == line.text.length)
      return true;
    for (var sp, i = 0; i < line.markedSpans.length; ++i) {
      sp = line.markedSpans[i];
      if (sp.marker.collapsed && !sp.marker.widgetNode && sp.from == span.to &&
          (sp.to == null || sp.to != span.from) &&
          (sp.marker.inclusiveLeft || span.marker.inclusiveRight) &&
          lineIsHiddenInner(doc, line, sp)) return true;
    }
  }

  // LINE WIDGETS

  // Line widgets are block elements displayed above or below a line.

  var LineWidget = CodeMirror.LineWidget = function(doc, node, options) {
    if (options) for (var opt in options) if (options.hasOwnProperty(opt))
      this[opt] = options[opt];
    this.doc = doc;
    this.node = node;
  };
  eventMixin(LineWidget);

  function adjustScrollWhenAboveVisible(cm, line, diff) {
    if (heightAtLine(line) < ((cm.curOp && cm.curOp.scrollTop) || cm.doc.scrollTop))
      addToScrollPos(cm, null, diff);
  }

  LineWidget.prototype.clear = function() {
    var cm = this.doc.cm, ws = this.line.widgets, line = this.line, no = lineNo(line);
    if (no == null || !ws) return;
    for (var i = 0; i < ws.length; ++i) if (ws[i] == this) ws.splice(i--, 1);
    if (!ws.length) line.widgets = null;
    var height = widgetHeight(this);
    updateLineHeight(line, Math.max(0, line.height - height));
    if (cm) runInOp(cm, function() {
      adjustScrollWhenAboveVisible(cm, line, -height);
      regLineChange(cm, no, "widget");
    });
  };
  LineWidget.prototype.changed = function() {
    var oldH = this.height, cm = this.doc.cm, line = this.line;
    this.height = null;
    var diff = widgetHeight(this) - oldH;
    if (!diff) return;
    updateLineHeight(line, line.height + diff);
    if (cm) runInOp(cm, function() {
      cm.curOp.forceUpdate = true;
      adjustScrollWhenAboveVisible(cm, line, diff);
    });
  };

  function widgetHeight(widget) {
    if (widget.height != null) return widget.height;
    var cm = widget.doc.cm;
    if (!cm) return 0;
    if (!contains(document.body, widget.node)) {
      var parentStyle = "position: relative;";
      if (widget.coverGutter)
        parentStyle += "margin-left: -" + cm.display.gutters.offsetWidth + "px;";
      if (widget.noHScroll)
        parentStyle += "width: " + cm.display.wrapper.clientWidth + "px;";
      removeChildrenAndAdd(cm.display.measure, elt("div", [widget.node], null, parentStyle));
    }
    return widget.height = widget.node.offsetHeight;
  }

  function addLineWidget(doc, handle, node, options) {
    var widget = new LineWidget(doc, node, options);
    var cm = doc.cm;
    if (cm && widget.noHScroll) cm.display.alignWidgets = true;
    changeLine(doc, handle, "widget", function(line) {
      var widgets = line.widgets || (line.widgets = []);
      if (widget.insertAt == null) widgets.push(widget);
      else widgets.splice(Math.min(widgets.length - 1, Math.max(0, widget.insertAt)), 0, widget);
      widget.line = line;
      if (cm && !lineIsHidden(doc, line)) {
        var aboveVisible = heightAtLine(line) < doc.scrollTop;
        updateLineHeight(line, line.height + widgetHeight(widget));
        if (aboveVisible) addToScrollPos(cm, null, widget.height);
        cm.curOp.forceUpdate = true;
      }
      return true;
    });
    return widget;
  }

  // LINE DATA STRUCTURE

  // Line objects. These hold state related to a line, including
  // highlighting info (the styles array).
  var Line = CodeMirror.Line = function(text, markedSpans, estimateHeight) {
    this.text = text;
    attachMarkedSpans(this, markedSpans);
    this.height = estimateHeight ? estimateHeight(this) : 1;
  };
  eventMixin(Line);
  Line.prototype.lineNo = function() { return lineNo(this); };

  // Change the content (text, markers) of a line. Automatically
  // invalidates cached information and tries to re-estimate the
  // line's height.
  function updateLine(line, text, markedSpans, estimateHeight) {
    line.text = text;
    if (line.stateAfter) line.stateAfter = null;
    if (line.styles) line.styles = null;
    if (line.order != null) line.order = null;
    detachMarkedSpans(line);
    attachMarkedSpans(line, markedSpans);
    var estHeight = estimateHeight ? estimateHeight(line) : 1;
    if (estHeight != line.height) updateLineHeight(line, estHeight);
  }

  // Detach a line from the document tree and its markers.
  function cleanUpLine(line) {
    line.parent = null;
    detachMarkedSpans(line);
  }

  function extractLineClasses(type, output) {
    if (type) for (;;) {
      var lineClass = type.match(/(?:^|\s+)line-(background-)?(\S+)/);
      if (!lineClass) break;
      type = type.slice(0, lineClass.index) + type.slice(lineClass.index + lineClass[0].length);
      var prop = lineClass[1] ? "bgClass" : "textClass";
      if (output[prop] == null)
        output[prop] = lineClass[2];
      else if (!(new RegExp("(?:^|\s)" + lineClass[2] + "(?:$|\s)")).test(output[prop]))
        output[prop] += " " + lineClass[2];
    }
    return type;
  }

  function callBlankLine(mode, state) {
    if (mode.blankLine) return mode.blankLine(state);
    if (!mode.innerMode) return;
    var inner = CodeMirror.innerMode(mode, state);
    if (inner.mode.blankLine) return inner.mode.blankLine(inner.state);
  }

  function readToken(mode, stream, state, inner) {
    for (var i = 0; i < 10; i++) {
      if (inner) inner[0] = CodeMirror.innerMode(mode, state).mode;
      var style = mode.token(stream, state);
      if (stream.pos > stream.start) return style;
    }
    throw new Error("Mode " + mode.name + " failed to advance stream.");
  }

  // Utility for getTokenAt and getLineTokens
  function takeToken(cm, pos, precise, asArray) {
    function getObj(copy) {
      return {start: stream.start, end: stream.pos,
              string: stream.current(),
              type: style || null,
              state: copy ? copyState(doc.mode, state) : state};
    }

    var doc = cm.doc, mode = doc.mode, style;
    pos = clipPos(doc, pos);
    var line = getLine(doc, pos.line), state = getStateBefore(cm, pos.line, precise);
    var stream = new StringStream(line.text, cm.options.tabSize), tokens;
    if (asArray) tokens = [];
    while ((asArray || stream.pos < pos.ch) && !stream.eol()) {
      stream.start = stream.pos;
      style = readToken(mode, stream, state);
      if (asArray) tokens.push(getObj(true));
    }
    return asArray ? tokens : getObj();
  }

  // Run the given mode's parser over a line, calling f for each token.
  function runMode(cm, text, mode, state, f, lineClasses, forceToEnd) {
    var flattenSpans = mode.flattenSpans;
    if (flattenSpans == null) flattenSpans = cm.options.flattenSpans;
    var curStart = 0, curStyle = null;
    var stream = new StringStream(text, cm.options.tabSize), style;
    var inner = cm.options.addModeClass && [null];
    if (text == "") extractLineClasses(callBlankLine(mode, state), lineClasses);
    while (!stream.eol()) {
      if (stream.pos > cm.options.maxHighlightLength) {
        flattenSpans = false;
        if (forceToEnd) processLine(cm, text, state, stream.pos);
        stream.pos = text.length;
        style = null;
      } else {
        style = extractLineClasses(readToken(mode, stream, state, inner), lineClasses);
      }
      if (inner) {
        var mName = inner[0].name;
        if (mName) style = "m-" + (style ? mName + " " + style : mName);
      }
      if (!flattenSpans || curStyle != style) {
        while (curStart < stream.start) {
          curStart = Math.min(stream.start, curStart + 50000);
          f(curStart, curStyle);
        }
        curStyle = style;
      }
      stream.start = stream.pos;
    }
    while (curStart < stream.pos) {
      // Webkit seems to refuse to render text nodes longer than 57444 characters
      var pos = Math.min(stream.pos, curStart + 50000);
      f(pos, curStyle);
      curStart = pos;
    }
  }

  // Compute a style array (an array starting with a mode generation
  // -- for invalidation -- followed by pairs of end positions and
  // style strings), which is used to highlight the tokens on the
  // line.
  function highlightLine(cm, line, state, forceToEnd) {
    // A styles array always starts with a number identifying the
    // mode/overlays that it is based on (for easy invalidation).
    var st = [cm.state.modeGen], lineClasses = {};
    // Compute the base array of styles
    runMode(cm, line.text, cm.doc.mode, state, function(end, style) {
      st.push(end, style);
    }, lineClasses, forceToEnd);

    // Run overlays, adjust style array.
    for (var o = 0; o < cm.state.overlays.length; ++o) {
      var overlay = cm.state.overlays[o], i = 1, at = 0;
      runMode(cm, line.text, overlay.mode, true, function(end, style) {
        var start = i;
        // Ensure there's a token end at the current position, and that i points at it
        while (at < end) {
          var i_end = st[i];
          if (i_end > end)
            st.splice(i, 1, end, st[i+1], i_end);
          i += 2;
          at = Math.min(end, i_end);
        }
        if (!style) return;
        if (overlay.opaque) {
          st.splice(start, i - start, end, "cm-overlay " + style);
          i = start + 2;
        } else {
          for (; start < i; start += 2) {
            var cur = st[start+1];
            st[start+1] = (cur ? cur + " " : "") + "cm-overlay " + style;
          }
        }
      }, lineClasses);
    }

    return {styles: st, classes: lineClasses.bgClass || lineClasses.textClass ? lineClasses : null};
  }

  function getLineStyles(cm, line, updateFrontier) {
    if (!line.styles || line.styles[0] != cm.state.modeGen) {
      var result = highlightLine(cm, line, line.stateAfter = getStateBefore(cm, lineNo(line)));
      line.styles = result.styles;
      if (result.classes) line.styleClasses = result.classes;
      else if (line.styleClasses) line.styleClasses = null;
      if (updateFrontier === cm.doc.frontier) cm.doc.frontier++;
    }
    return line.styles;
  }

  // Lightweight form of highlight -- proceed over this line and
  // update state, but don't save a style array. Used for lines that
  // aren't currently visible.
  function processLine(cm, text, state, startAt) {
    var mode = cm.doc.mode;
    var stream = new StringStream(text, cm.options.tabSize);
    stream.start = stream.pos = startAt || 0;
    if (text == "") callBlankLine(mode, state);
    while (!stream.eol() && stream.pos <= cm.options.maxHighlightLength) {
      readToken(mode, stream, state);
      stream.start = stream.pos;
    }
  }

  // Convert a style as returned by a mode (either null, or a string
  // containing one or more styles) to a CSS style. This is cached,
  // and also looks for line-wide styles.
  var styleToClassCache = {}, styleToClassCacheWithMode = {};
  function interpretTokenStyle(style, options) {
    if (!style || /^\s*$/.test(style)) return null;
    var cache = options.addModeClass ? styleToClassCacheWithMode : styleToClassCache;
    return cache[style] ||
      (cache[style] = style.replace(/\S+/g, "cm-$&"));
  }

  // Render the DOM representation of the text of a line. Also builds
  // up a 'line map', which points at the DOM nodes that represent
  // specific stretches of text, and is used by the measuring code.
  // The returned object contains the DOM node, this map, and
  // information about line-wide styles that were set by the mode.
  function buildLineContent(cm, lineView) {
    // The padding-right forces the element to have a 'border', which
    // is needed on Webkit to be able to get line-level bounding
    // rectangles for it (in measureChar).
    var content = elt("span", null, null, webkit ? "padding-right: .1px" : null);
    var builder = {pre: elt("pre", [content]), content: content,
                   col: 0, pos: 0, cm: cm,
                   splitSpaces: (ie || webkit) && cm.getOption("lineWrapping")};
    lineView.measure = {};

    // Iterate over the logical lines that make up this visual line.
    for (var i = 0; i <= (lineView.rest ? lineView.rest.length : 0); i++) {
      var line = i ? lineView.rest[i - 1] : lineView.line, order;
      builder.pos = 0;
      builder.addToken = buildToken;
      // Optionally wire in some hacks into the token-rendering
      // algorithm, to deal with browser quirks.
      if (hasBadBidiRects(cm.display.measure) && (order = getOrder(line)))
        builder.addToken = buildTokenBadBidi(builder.addToken, order);
      builder.map = [];
      var allowFrontierUpdate = lineView != cm.display.externalMeasured && lineNo(line);
      insertLineContent(line, builder, getLineStyles(cm, line, allowFrontierUpdate));
      if (line.styleClasses) {
        if (line.styleClasses.bgClass)
          builder.bgClass = joinClasses(line.styleClasses.bgClass, builder.bgClass || "");
        if (line.styleClasses.textClass)
          builder.textClass = joinClasses(line.styleClasses.textClass, builder.textClass || "");
      }

      // Ensure at least a single node is present, for measuring.
      if (builder.map.length == 0)
        builder.map.push(0, 0, builder.content.appendChild(zeroWidthElement(cm.display.measure)));

      // Store the map and a cache object for the current logical line
      if (i == 0) {
        lineView.measure.map = builder.map;
        lineView.measure.cache = {};
      } else {
        (lineView.measure.maps || (lineView.measure.maps = [])).push(builder.map);
        (lineView.measure.caches || (lineView.measure.caches = [])).push({});
      }
    }

    // See issue #2901
    if (webkit && /\bcm-tab\b/.test(builder.content.lastChild.className))
      builder.content.className = "cm-tab-wrap-hack";

    signal(cm, "renderLine", cm, lineView.line, builder.pre);
    if (builder.pre.className)
      builder.textClass = joinClasses(builder.pre.className, builder.textClass || "");

    return builder;
  }

  function defaultSpecialCharPlaceholder(ch) {
    var token = elt("span", "\u2022", "cm-invalidchar");
    token.title = "\\u" + ch.charCodeAt(0).toString(16);
    token.setAttribute("aria-label", token.title);
    return token;
  }

  // Build up the DOM representation for a single token, and add it to
  // the line map. Takes care to render special characters separately.
  function buildToken(builder, text, style, startStyle, endStyle, title, css) {
    if (!text) return;
    var displayText = builder.splitSpaces ? text.replace(/ {3,}/g, splitSpaces) : text;
    var special = builder.cm.state.specialChars, mustWrap = false;
    if (!special.test(text)) {
      builder.col += text.length;
      var content = document.createTextNode(displayText);
      builder.map.push(builder.pos, builder.pos + text.length, content);
      if (ie && ie_version < 9) mustWrap = true;
      builder.pos += text.length;
    } else {
      var content = document.createDocumentFragment(), pos = 0;
      while (true) {
        special.lastIndex = pos;
        var m = special.exec(text);
        var skipped = m ? m.index - pos : text.length - pos;
        if (skipped) {
          var txt = document.createTextNode(displayText.slice(pos, pos + skipped));
          if (ie && ie_version < 9) content.appendChild(elt("span", [txt]));
          else content.appendChild(txt);
          builder.map.push(builder.pos, builder.pos + skipped, txt);
          builder.col += skipped;
          builder.pos += skipped;
        }
        if (!m) break;
        pos += skipped + 1;
        if (m[0] == "\t") {
          var tabSize = builder.cm.options.tabSize, tabWidth = tabSize - builder.col % tabSize;
          var txt = content.appendChild(elt("span", spaceStr(tabWidth), "cm-tab"));
          txt.setAttribute("role", "presentation");
          txt.setAttribute("cm-text", "\t");
          builder.col += tabWidth;
        } else {
          var txt = builder.cm.options.specialCharPlaceholder(m[0]);
          txt.setAttribute("cm-text", m[0]);
          if (ie && ie_version < 9) content.appendChild(elt("span", [txt]));
          else content.appendChild(txt);
          builder.col += 1;
        }
        builder.map.push(builder.pos, builder.pos + 1, txt);
        builder.pos++;
      }
    }
    if (style || startStyle || endStyle || mustWrap || css) {
      var fullStyle = style || "";
      if (startStyle) fullStyle += startStyle;
      if (endStyle) fullStyle += endStyle;
      var token = elt("span", [content], fullStyle, css);
      if (title) token.title = title;
      return builder.content.appendChild(token);
    }
    builder.content.appendChild(content);
  }

  function splitSpaces(old) {
    var out = " ";
    for (var i = 0; i < old.length - 2; ++i) out += i % 2 ? " " : "\u00a0";
    out += " ";
    return out;
  }

  // Work around nonsense dimensions being reported for stretches of
  // right-to-left text.
  function buildTokenBadBidi(inner, order) {
    return function(builder, text, style, startStyle, endStyle, title, css) {
      style = style ? style + " cm-force-border" : "cm-force-border";
      var start = builder.pos, end = start + text.length;
      for (;;) {
        // Find the part that overlaps with the start of this text
        for (var i = 0; i < order.length; i++) {
          var part = order[i];
          if (part.to > start && part.from <= start) break;
        }
        if (part.to >= end) return inner(builder, text, style, startStyle, endStyle, title, css);
        inner(builder, text.slice(0, part.to - start), style, startStyle, null, title, css);
        startStyle = null;
        text = text.slice(part.to - start);
        start = part.to;
      }
    };
  }

  function buildCollapsedSpan(builder, size, marker, ignoreWidget) {
    var widget = !ignoreWidget && marker.widgetNode;
    if (widget) builder.map.push(builder.pos, builder.pos + size, widget);
    if (!ignoreWidget && builder.cm.display.input.needsContentAttribute) {
      if (!widget)
        widget = builder.content.appendChild(document.createElement("span"));
      widget.setAttribute("cm-marker", marker.id);
    }
    if (widget) {
      builder.cm.display.input.setUneditable(widget);
      builder.content.appendChild(widget);
    }
    builder.pos += size;
  }

  // Outputs a number of spans to make up a line, taking highlighting
  // and marked text into account.
  function insertLineContent(line, builder, styles) {
    var spans = line.markedSpans, allText = line.text, at = 0;
    if (!spans) {
      for (var i = 1; i < styles.length; i+=2)
        builder.addToken(builder, allText.slice(at, at = styles[i]), interpretTokenStyle(styles[i+1], builder.cm.options));
      return;
    }

    var len = allText.length, pos = 0, i = 1, text = "", style, css;
    var nextChange = 0, spanStyle, spanEndStyle, spanStartStyle, title, collapsed;
    for (;;) {
      if (nextChange == pos) { // Update current marker set
        spanStyle = spanEndStyle = spanStartStyle = title = css = "";
        collapsed = null; nextChange = Infinity;
        var foundBookmarks = [];
        for (var j = 0; j < spans.length; ++j) {
          var sp = spans[j], m = sp.marker;
          if (m.type == "bookmark" && sp.from == pos && m.widgetNode) {
            foundBookmarks.push(m);
          } else if (sp.from <= pos && (sp.to == null || sp.to > pos || m.collapsed && sp.to == pos && sp.from == pos)) {
            if (sp.to != null && sp.to != pos && nextChange > sp.to) {
              nextChange = sp.to;
              spanEndStyle = "";
            }
            if (m.className) spanStyle += " " + m.className;
            if (m.css) css = m.css;
            if (m.startStyle && sp.from == pos) spanStartStyle += " " + m.startStyle;
            if (m.endStyle && sp.to == nextChange) spanEndStyle += " " + m.endStyle;
            if (m.title && !title) title = m.title;
            if (m.collapsed && (!collapsed || compareCollapsedMarkers(collapsed.marker, m) < 0))
              collapsed = sp;
          } else if (sp.from > pos && nextChange > sp.from) {
            nextChange = sp.from;
          }
        }
        if (collapsed && (collapsed.from || 0) == pos) {
          buildCollapsedSpan(builder, (collapsed.to == null ? len + 1 : collapsed.to) - pos,
                             collapsed.marker, collapsed.from == null);
          if (collapsed.to == null) return;
          if (collapsed.to == pos) collapsed = false;
        }
        if (!collapsed && foundBookmarks.length) for (var j = 0; j < foundBookmarks.length; ++j)
          buildCollapsedSpan(builder, 0, foundBookmarks[j]);
      }
      if (pos >= len) break;

      var upto = Math.min(len, nextChange);
      while (true) {
        if (text) {
          var end = pos + text.length;
          if (!collapsed) {
            var tokenText = end > upto ? text.slice(0, upto - pos) : text;
            builder.addToken(builder, tokenText, style ? style + spanStyle : spanStyle,
                             spanStartStyle, pos + tokenText.length == nextChange ? spanEndStyle : "", title, css);
          }
          if (end >= upto) {text = text.slice(upto - pos); pos = upto; break;}
          pos = end;
          spanStartStyle = "";
        }
        text = allText.slice(at, at = styles[i++]);
        style = interpretTokenStyle(styles[i++], builder.cm.options);
      }
    }
  }

  // DOCUMENT DATA STRUCTURE

  // By default, updates that start and end at the beginning of a line
  // are treated specially, in order to make the association of line
  // widgets and marker elements with the text behave more intuitive.
  function isWholeLineUpdate(doc, change) {
    return change.from.ch == 0 && change.to.ch == 0 && lst(change.text) == "" &&
      (!doc.cm || doc.cm.options.wholeLineUpdateBefore);
  }

  // Perform a change on the document data structure.
  function updateDoc(doc, change, markedSpans, estimateHeight) {
    function spansFor(n) {return markedSpans ? markedSpans[n] : null;}
    function update(line, text, spans) {
      updateLine(line, text, spans, estimateHeight);
      signalLater(line, "change", line, change);
    }
    function linesFor(start, end) {
      for (var i = start, result = []; i < end; ++i)
        result.push(new Line(text[i], spansFor(i), estimateHeight));
      return result;
    }

    var from = change.from, to = change.to, text = change.text;
    var firstLine = getLine(doc, from.line), lastLine = getLine(doc, to.line);
    var lastText = lst(text), lastSpans = spansFor(text.length - 1), nlines = to.line - from.line;

    // Adjust the line structure
    if (change.full) {
      doc.insert(0, linesFor(0, text.length));
      doc.remove(text.length, doc.size - text.length);
    } else if (isWholeLineUpdate(doc, change)) {
      // This is a whole-line replace. Treated specially to make
      // sure line objects move the way they are supposed to.
      var added = linesFor(0, text.length - 1);
      update(lastLine, lastLine.text, lastSpans);
      if (nlines) doc.remove(from.line, nlines);
      if (added.length) doc.insert(from.line, added);
    } else if (firstLine == lastLine) {
      if (text.length == 1) {
        update(firstLine, firstLine.text.slice(0, from.ch) + lastText + firstLine.text.slice(to.ch), lastSpans);
      } else {
        var added = linesFor(1, text.length - 1);
        added.push(new Line(lastText + firstLine.text.slice(to.ch), lastSpans, estimateHeight));
        update(firstLine, firstLine.text.slice(0, from.ch) + text[0], spansFor(0));
        doc.insert(from.line + 1, added);
      }
    } else if (text.length == 1) {
      update(firstLine, firstLine.text.slice(0, from.ch) + text[0] + lastLine.text.slice(to.ch), spansFor(0));
      doc.remove(from.line + 1, nlines);
    } else {
      update(firstLine, firstLine.text.slice(0, from.ch) + text[0], spansFor(0));
      update(lastLine, lastText + lastLine.text.slice(to.ch), lastSpans);
      var added = linesFor(1, text.length - 1);
      if (nlines > 1) doc.remove(from.line + 1, nlines - 1);
      doc.insert(from.line + 1, added);
    }

    signalLater(doc, "change", doc, change);
  }

  // The document is represented as a BTree consisting of leaves, with
  // chunk of lines in them, and branches, with up to ten leaves or
  // other branch nodes below them. The top node is always a branch
  // node, and is the document object itself (meaning it has
  // additional methods and properties).
  //
  // All nodes have parent links. The tree is used both to go from
  // line numbers to line objects, and to go from objects to numbers.
  // It also indexes by height, and is used to convert between height
  // and line object, and to find the total height of the document.
  //
  // See also http://marijnhaverbeke.nl/blog/codemirror-line-tree.html

  function LeafChunk(lines) {
    this.lines = lines;
    this.parent = null;
    for (var i = 0, height = 0; i < lines.length; ++i) {
      lines[i].parent = this;
      height += lines[i].height;
    }
    this.height = height;
  }

  LeafChunk.prototype = {
    chunkSize: function() { return this.lines.length; },
    // Remove the n lines at offset 'at'.
    removeInner: function(at, n) {
      for (var i = at, e = at + n; i < e; ++i) {
        var line = this.lines[i];
        this.height -= line.height;
        cleanUpLine(line);
        signalLater(line, "delete");
      }
      this.lines.splice(at, n);
    },
    // Helper used to collapse a small branch into a single leaf.
    collapse: function(lines) {
      lines.push.apply(lines, this.lines);
    },
    // Insert the given array of lines at offset 'at', count them as
    // having the given height.
    insertInner: function(at, lines, height) {
      this.height += height;
      this.lines = this.lines.slice(0, at).concat(lines).concat(this.lines.slice(at));
      for (var i = 0; i < lines.length; ++i) lines[i].parent = this;
    },
    // Used to iterate over a part of the tree.
    iterN: function(at, n, op) {
      for (var e = at + n; at < e; ++at)
        if (op(this.lines[at])) return true;
    }
  };

  function BranchChunk(children) {
    this.children = children;
    var size = 0, height = 0;
    for (var i = 0; i < children.length; ++i) {
      var ch = children[i];
      size += ch.chunkSize(); height += ch.height;
      ch.parent = this;
    }
    this.size = size;
    this.height = height;
    this.parent = null;
  }

  BranchChunk.prototype = {
    chunkSize: function() { return this.size; },
    removeInner: function(at, n) {
      this.size -= n;
      for (var i = 0; i < this.children.length; ++i) {
        var child = this.children[i], sz = child.chunkSize();
        if (at < sz) {
          var rm = Math.min(n, sz - at), oldHeight = child.height;
          child.removeInner(at, rm);
          this.height -= oldHeight - child.height;
          if (sz == rm) { this.children.splice(i--, 1); child.parent = null; }
          if ((n -= rm) == 0) break;
          at = 0;
        } else at -= sz;
      }
      // If the result is smaller than 25 lines, ensure that it is a
      // single leaf node.
      if (this.size - n < 25 &&
          (this.children.length > 1 || !(this.children[0] instanceof LeafChunk))) {
        var lines = [];
        this.collapse(lines);
        this.children = [new LeafChunk(lines)];
        this.children[0].parent = this;
      }
    },
    collapse: function(lines) {
      for (var i = 0; i < this.children.length; ++i) this.children[i].collapse(lines);
    },
    insertInner: function(at, lines, height) {
      this.size += lines.length;
      this.height += height;
      for (var i = 0; i < this.children.length; ++i) {
        var child = this.children[i], sz = child.chunkSize();
        if (at <= sz) {
          child.insertInner(at, lines, height);
          if (child.lines && child.lines.length > 50) {
            while (child.lines.length > 50) {
              var spilled = child.lines.splice(child.lines.length - 25, 25);
              var newleaf = new LeafChunk(spilled);
              child.height -= newleaf.height;
              this.children.splice(i + 1, 0, newleaf);
              newleaf.parent = this;
            }
            this.maybeSpill();
          }
          break;
        }
        at -= sz;
      }
    },
    // When a node has grown, check whether it should be split.
    maybeSpill: function() {
      if (this.children.length <= 10) return;
      var me = this;
      do {
        var spilled = me.children.splice(me.children.length - 5, 5);
        var sibling = new BranchChunk(spilled);
        if (!me.parent) { // Become the parent node
          var copy = new BranchChunk(me.children);
          copy.parent = me;
          me.children = [copy, sibling];
          me = copy;
        } else {
          me.size -= sibling.size;
          me.height -= sibling.height;
          var myIndex = indexOf(me.parent.children, me);
          me.parent.children.splice(myIndex + 1, 0, sibling);
        }
        sibling.parent = me.parent;
      } while (me.children.length > 10);
      me.parent.maybeSpill();
    },
    iterN: function(at, n, op) {
      for (var i = 0; i < this.children.length; ++i) {
        var child = this.children[i], sz = child.chunkSize();
        if (at < sz) {
          var used = Math.min(n, sz - at);
          if (child.iterN(at, used, op)) return true;
          if ((n -= used) == 0) break;
          at = 0;
        } else at -= sz;
      }
    }
  };

  var nextDocId = 0;
  var Doc = CodeMirror.Doc = function(text, mode, firstLine) {
    if (!(this instanceof Doc)) return new Doc(text, mode, firstLine);
    if (firstLine == null) firstLine = 0;

    BranchChunk.call(this, [new LeafChunk([new Line("", null)])]);
    this.first = firstLine;
    this.scrollTop = this.scrollLeft = 0;
    this.cantEdit = false;
    this.cleanGeneration = 1;
    this.frontier = firstLine;
    var start = Pos(firstLine, 0);
    this.sel = simpleSelection(start);
    this.history = new History(null);
    this.id = ++nextDocId;
    this.modeOption = mode;

    if (typeof text == "string") text = splitLines(text);
    updateDoc(this, {from: start, to: start, text: text});
    setSelection(this, simpleSelection(start), sel_dontScroll);
  };

  Doc.prototype = createObj(BranchChunk.prototype, {
    constructor: Doc,
    // Iterate over the document. Supports two forms -- with only one
    // argument, it calls that for each line in the document. With
    // three, it iterates over the range given by the first two (with
    // the second being non-inclusive).
    iter: function(from, to, op) {
      if (op) this.iterN(from - this.first, to - from, op);
      else this.iterN(this.first, this.first + this.size, from);
    },

    // Non-public interface for adding and removing lines.
    insert: function(at, lines) {
      var height = 0;
      for (var i = 0; i < lines.length; ++i) height += lines[i].height;
      this.insertInner(at - this.first, lines, height);
    },
    remove: function(at, n) { this.removeInner(at - this.first, n); },

    // From here, the methods are part of the public interface. Most
    // are also available from CodeMirror (editor) instances.

    getValue: function(lineSep) {
      var lines = getLines(this, this.first, this.first + this.size);
      if (lineSep === false) return lines;
      return lines.join(lineSep || "\n");
    },
    setValue: docMethodOp(function(code) {
      var top = Pos(this.first, 0), last = this.first + this.size - 1;
      makeChange(this, {from: top, to: Pos(last, getLine(this, last).text.length),
                        text: splitLines(code), origin: "setValue", full: true}, true);
      setSelection(this, simpleSelection(top));
    }),
    replaceRange: function(code, from, to, origin) {
      from = clipPos(this, from);
      to = to ? clipPos(this, to) : from;
      replaceRange(this, code, from, to, origin);
    },
    getRange: function(from, to, lineSep) {
      var lines = getBetween(this, clipPos(this, from), clipPos(this, to));
      if (lineSep === false) return lines;
      return lines.join(lineSep || "\n");
    },

    getLine: function(line) {var l = this.getLineHandle(line); return l && l.text;},

    getLineHandle: function(line) {if (isLine(this, line)) return getLine(this, line);},
    getLineNumber: function(line) {return lineNo(line);},

    getLineHandleVisualStart: function(line) {
      if (typeof line == "number") line = getLine(this, line);
      return visualLine(line);
    },

    lineCount: function() {return this.size;},
    firstLine: function() {return this.first;},
    lastLine: function() {return this.first + this.size - 1;},

    clipPos: function(pos) {return clipPos(this, pos);},

    getCursor: function(start) {
      var range = this.sel.primary(), pos;
      if (start == null || start == "head") pos = range.head;
      else if (start == "anchor") pos = range.anchor;
      else if (start == "end" || start == "to" || start === false) pos = range.to();
      else pos = range.from();
      return pos;
    },
    listSelections: function() { return this.sel.ranges; },
    somethingSelected: function() {return this.sel.somethingSelected();},

    setCursor: docMethodOp(function(line, ch, options) {
      setSimpleSelection(this, clipPos(this, typeof line == "number" ? Pos(line, ch || 0) : line), null, options);
    }),
    setSelection: docMethodOp(function(anchor, head, options) {
      setSimpleSelection(this, clipPos(this, anchor), clipPos(this, head || anchor), options);
    }),
    extendSelection: docMethodOp(function(head, other, options) {
      extendSelection(this, clipPos(this, head), other && clipPos(this, other), options);
    }),
    extendSelections: docMethodOp(function(heads, options) {
      extendSelections(this, clipPosArray(this, heads, options));
    }),
    extendSelectionsBy: docMethodOp(function(f, options) {
      extendSelections(this, map(this.sel.ranges, f), options);
    }),
    setSelections: docMethodOp(function(ranges, primary, options) {
      if (!ranges.length) return;
      for (var i = 0, out = []; i < ranges.length; i++)
        out[i] = new Range(clipPos(this, ranges[i].anchor),
                           clipPos(this, ranges[i].head));
      if (primary == null) primary = Math.min(ranges.length - 1, this.sel.primIndex);
      setSelection(this, normalizeSelection(out, primary), options);
    }),
    addSelection: docMethodOp(function(anchor, head, options) {
      var ranges = this.sel.ranges.slice(0);
      ranges.push(new Range(clipPos(this, anchor), clipPos(this, head || anchor)));
      setSelection(this, normalizeSelection(ranges, ranges.length - 1), options);
    }),

    getSelection: function(lineSep) {
      var ranges = this.sel.ranges, lines;
      for (var i = 0; i < ranges.length; i++) {
        var sel = getBetween(this, ranges[i].from(), ranges[i].to());
        lines = lines ? lines.concat(sel) : sel;
      }
      if (lineSep === false) return lines;
      else return lines.join(lineSep || "\n");
    },
    getSelections: function(lineSep) {
      var parts = [], ranges = this.sel.ranges;
      for (var i = 0; i < ranges.length; i++) {
        var sel = getBetween(this, ranges[i].from(), ranges[i].to());
        if (lineSep !== false) sel = sel.join(lineSep || "\n");
        parts[i] = sel;
      }
      return parts;
    },
    replaceSelection: function(code, collapse, origin) {
      var dup = [];
      for (var i = 0; i < this.sel.ranges.length; i++)
        dup[i] = code;
      this.replaceSelections(dup, collapse, origin || "+input");
    },
    replaceSelections: docMethodOp(function(code, collapse, origin) {
      var changes = [], sel = this.sel;
      for (var i = 0; i < sel.ranges.length; i++) {
        var range = sel.ranges[i];
        changes[i] = {from: range.from(), to: range.to(), text: splitLines(code[i]), origin: origin};
      }
      var newSel = collapse && collapse != "end" && computeReplacedSel(this, changes, collapse);
      for (var i = changes.length - 1; i >= 0; i--)
        makeChange(this, changes[i]);
      if (newSel) setSelectionReplaceHistory(this, newSel);
      else if (this.cm) ensureCursorVisible(this.cm);
    }),
    undo: docMethodOp(function() {makeChangeFromHistory(this, "undo");}),
    redo: docMethodOp(function() {makeChangeFromHistory(this, "redo");}),
    undoSelection: docMethodOp(function() {makeChangeFromHistory(this, "undo", true);}),
    redoSelection: docMethodOp(function() {makeChangeFromHistory(this, "redo", true);}),

    setExtending: function(val) {this.extend = val;},
    getExtending: function() {return this.extend;},

    historySize: function() {
      var hist = this.history, done = 0, undone = 0;
      for (var i = 0; i < hist.done.length; i++) if (!hist.done[i].ranges) ++done;
      for (var i = 0; i < hist.undone.length; i++) if (!hist.undone[i].ranges) ++undone;
      return {undo: done, redo: undone};
    },
    clearHistory: function() {this.history = new History(this.history.maxGeneration);},

    markClean: function() {
      this.cleanGeneration = this.changeGeneration(true);
    },
    changeGeneration: function(forceSplit) {
      if (forceSplit)
        this.history.lastOp = this.history.lastSelOp = this.history.lastOrigin = null;
      return this.history.generation;
    },
    isClean: function (gen) {
      return this.history.generation == (gen || this.cleanGeneration);
    },

    getHistory: function() {
      return {done: copyHistoryArray(this.history.done),
              undone: copyHistoryArray(this.history.undone)};
    },
    setHistory: function(histData) {
      var hist = this.history = new History(this.history.maxGeneration);
      hist.done = copyHistoryArray(histData.done.slice(0), null, true);
      hist.undone = copyHistoryArray(histData.undone.slice(0), null, true);
    },

    addLineClass: docMethodOp(function(handle, where, cls) {
      return changeLine(this, handle, where == "gutter" ? "gutter" : "class", function(line) {
        var prop = where == "text" ? "textClass"
                 : where == "background" ? "bgClass"
                 : where == "gutter" ? "gutterClass" : "wrapClass";
        if (!line[prop]) line[prop] = cls;
        else if (classTest(cls).test(line[prop])) return false;
        else line[prop] += " " + cls;
        return true;
      });
    }),
    removeLineClass: docMethodOp(function(handle, where, cls) {
      return changeLine(this, handle, where == "gutter" ? "gutter" : "class", function(line) {
        var prop = where == "text" ? "textClass"
                 : where == "background" ? "bgClass"
                 : where == "gutter" ? "gutterClass" : "wrapClass";
        var cur = line[prop];
        if (!cur) return false;
        else if (cls == null) line[prop] = null;
        else {
          var found = cur.match(classTest(cls));
          if (!found) return false;
          var end = found.index + found[0].length;
          line[prop] = cur.slice(0, found.index) + (!found.index || end == cur.length ? "" : " ") + cur.slice(end) || null;
        }
        return true;
      });
    }),

    addLineWidget: docMethodOp(function(handle, node, options) {
      return addLineWidget(this, handle, node, options);
    }),
    removeLineWidget: function(widget) { widget.clear(); },

    markText: function(from, to, options) {
      return markText(this, clipPos(this, from), clipPos(this, to), options, "range");
    },
    setBookmark: function(pos, options) {
      var realOpts = {replacedWith: options && (options.nodeType == null ? options.widget : options),
                      insertLeft: options && options.insertLeft,
                      clearWhenEmpty: false, shared: options && options.shared,
                      handleMouseEvents: options && options.handleMouseEvents};
      pos = clipPos(this, pos);
      return markText(this, pos, pos, realOpts, "bookmark");
    },
    findMarksAt: function(pos) {
      pos = clipPos(this, pos);
      var markers = [], spans = getLine(this, pos.line).markedSpans;
      if (spans) for (var i = 0; i < spans.length; ++i) {
        var span = spans[i];
        if ((span.from == null || span.from <= pos.ch) &&
            (span.to == null || span.to >= pos.ch))
          markers.push(span.marker.parent || span.marker);
      }
      return markers;
    },
    findMarks: function(from, to, filter) {
      from = clipPos(this, from); to = clipPos(this, to);
      var found = [], lineNo = from.line;
      this.iter(from.line, to.line + 1, function(line) {
        var spans = line.markedSpans;
        if (spans) for (var i = 0; i < spans.length; i++) {
          var span = spans[i];
          if (!(lineNo == from.line && from.ch > span.to ||
                span.from == null && lineNo != from.line||
                lineNo == to.line && span.from > to.ch) &&
              (!filter || filter(span.marker)))
            found.push(span.marker.parent || span.marker);
        }
        ++lineNo;
      });
      return found;
    },
    getAllMarks: function() {
      var markers = [];
      this.iter(function(line) {
        var sps = line.markedSpans;
        if (sps) for (var i = 0; i < sps.length; ++i)
          if (sps[i].from != null) markers.push(sps[i].marker);
      });
      return markers;
    },

    posFromIndex: function(off) {
      var ch, lineNo = this.first;
      this.iter(function(line) {
        var sz = line.text.length + 1;
        if (sz > off) { ch = off; return true; }
        off -= sz;
        ++lineNo;
      });
      return clipPos(this, Pos(lineNo, ch));
    },
    indexFromPos: function (coords) {
      coords = clipPos(this, coords);
      var index = coords.ch;
      if (coords.line < this.first || coords.ch < 0) return 0;
      this.iter(this.first, coords.line, function (line) {
        index += line.text.length + 1;
      });
      return index;
    },

    copy: function(copyHistory) {
      var doc = new Doc(getLines(this, this.first, this.first + this.size), this.modeOption, this.first);
      doc.scrollTop = this.scrollTop; doc.scrollLeft = this.scrollLeft;
      doc.sel = this.sel;
      doc.extend = false;
      if (copyHistory) {
        doc.history.undoDepth = this.history.undoDepth;
        doc.setHistory(this.getHistory());
      }
      return doc;
    },

    linkedDoc: function(options) {
      if (!options) options = {};
      var from = this.first, to = this.first + this.size;
      if (options.from != null && options.from > from) from = options.from;
      if (options.to != null && options.to < to) to = options.to;
      var copy = new Doc(getLines(this, from, to), options.mode || this.modeOption, from);
      if (options.sharedHist) copy.history = this.history;
      (this.linked || (this.linked = [])).push({doc: copy, sharedHist: options.sharedHist});
      copy.linked = [{doc: this, isParent: true, sharedHist: options.sharedHist}];
      copySharedMarkers(copy, findSharedMarkers(this));
      return copy;
    },
    unlinkDoc: function(other) {
      if (other instanceof CodeMirror) other = other.doc;
      if (this.linked) for (var i = 0; i < this.linked.length; ++i) {
        var link = this.linked[i];
        if (link.doc != other) continue;
        this.linked.splice(i, 1);
        other.unlinkDoc(this);
        detachSharedMarkers(findSharedMarkers(this));
        break;
      }
      // If the histories were shared, split them again
      if (other.history == this.history) {
        var splitIds = [other.id];
        linkedDocs(other, function(doc) {splitIds.push(doc.id);}, true);
        other.history = new History(null);
        other.history.done = copyHistoryArray(this.history.done, splitIds);
        other.history.undone = copyHistoryArray(this.history.undone, splitIds);
      }
    },
    iterLinkedDocs: function(f) {linkedDocs(this, f);},

    getMode: function() {return this.mode;},
    getEditor: function() {return this.cm;}
  });

  // Public alias.
  Doc.prototype.eachLine = Doc.prototype.iter;

  // Set up methods on CodeMirror's prototype to redirect to the editor's document.
  var dontDelegate = "iter insert remove copy getEditor".split(" ");
  for (var prop in Doc.prototype) if (Doc.prototype.hasOwnProperty(prop) && indexOf(dontDelegate, prop) < 0)
    CodeMirror.prototype[prop] = (function(method) {
      return function() {return method.apply(this.doc, arguments);};
    })(Doc.prototype[prop]);

  eventMixin(Doc);

  // Call f for all linked documents.
  function linkedDocs(doc, f, sharedHistOnly) {
    function propagate(doc, skip, sharedHist) {
      if (doc.linked) for (var i = 0; i < doc.linked.length; ++i) {
        var rel = doc.linked[i];
        if (rel.doc == skip) continue;
        var shared = sharedHist && rel.sharedHist;
        if (sharedHistOnly && !shared) continue;
        f(rel.doc, shared);
        propagate(rel.doc, doc, shared);
      }
    }
    propagate(doc, null, true);
  }

  // Attach a document to an editor.
  function attachDoc(cm, doc) {
    if (doc.cm) throw new Error("This document is already in use.");
    cm.doc = doc;
    doc.cm = cm;
    estimateLineHeights(cm);
    loadMode(cm);
    if (!cm.options.lineWrapping) findMaxLine(cm);
    cm.options.mode = doc.modeOption;
    regChange(cm);
  }

  // LINE UTILITIES

  // Find the line object corresponding to the given line number.
  function getLine(doc, n) {
    n -= doc.first;
    if (n < 0 || n >= doc.size) throw new Error("There is no line " + (n + doc.first) + " in the document.");
    for (var chunk = doc; !chunk.lines;) {
      for (var i = 0;; ++i) {
        var child = chunk.children[i], sz = child.chunkSize();
        if (n < sz) { chunk = child; break; }
        n -= sz;
      }
    }
    return chunk.lines[n];
  }

  // Get the part of a document between two positions, as an array of
  // strings.
  function getBetween(doc, start, end) {
    var out = [], n = start.line;
    doc.iter(start.line, end.line + 1, function(line) {
      var text = line.text;
      if (n == end.line) text = text.slice(0, end.ch);
      if (n == start.line) text = text.slice(start.ch);
      out.push(text);
      ++n;
    });
    return out;
  }
  // Get the lines between from and to, as array of strings.
  function getLines(doc, from, to) {
    var out = [];
    doc.iter(from, to, function(line) { out.push(line.text); });
    return out;
  }

  // Update the height of a line, propagating the height change
  // upwards to parent nodes.
  function updateLineHeight(line, height) {
    var diff = height - line.height;
    if (diff) for (var n = line; n; n = n.parent) n.height += diff;
  }

  // Given a line object, find its line number by walking up through
  // its parent links.
  function lineNo(line) {
    if (line.parent == null) return null;
    var cur = line.parent, no = indexOf(cur.lines, line);
    for (var chunk = cur.parent; chunk; cur = chunk, chunk = chunk.parent) {
      for (var i = 0;; ++i) {
        if (chunk.children[i] == cur) break;
        no += chunk.children[i].chunkSize();
      }
    }
    return no + cur.first;
  }

  // Find the line at the given vertical position, using the height
  // information in the document tree.
  function lineAtHeight(chunk, h) {
    var n = chunk.first;
    outer: do {
      for (var i = 0; i < chunk.children.length; ++i) {
        var child = chunk.children[i], ch = child.height;
        if (h < ch) { chunk = child; continue outer; }
        h -= ch;
        n += child.chunkSize();
      }
      return n;
    } while (!chunk.lines);
    for (var i = 0; i < chunk.lines.length; ++i) {
      var line = chunk.lines[i], lh = line.height;
      if (h < lh) break;
      h -= lh;
    }
    return n + i;
  }


  // Find the height above the given line.
  function heightAtLine(lineObj) {
    lineObj = visualLine(lineObj);

    var h = 0, chunk = lineObj.parent;
    for (var i = 0; i < chunk.lines.length; ++i) {
      var line = chunk.lines[i];
      if (line == lineObj) break;
      else h += line.height;
    }
    for (var p = chunk.parent; p; chunk = p, p = chunk.parent) {
      for (var i = 0; i < p.children.length; ++i) {
        var cur = p.children[i];
        if (cur == chunk) break;
        else h += cur.height;
      }
    }
    return h;
  }

  // Get the bidi ordering for the given line (and cache it). Returns
  // false for lines that are fully left-to-right, and an array of
  // BidiSpan objects otherwise.
  function getOrder(line) {
    var order = line.order;
    if (order == null) order = line.order = bidiOrdering(line.text);
    return order;
  }

  // HISTORY

  function History(startGen) {
    // Arrays of change events and selections. Doing something adds an
    // event to done and clears undo. Undoing moves events from done
    // to undone, redoing moves them in the other direction.
    this.done = []; this.undone = [];
    this.undoDepth = Infinity;
    // Used to track when changes can be merged into a single undo
    // event
    this.lastModTime = this.lastSelTime = 0;
    this.lastOp = this.lastSelOp = null;
    this.lastOrigin = this.lastSelOrigin = null;
    // Used by the isClean() method
    this.generation = this.maxGeneration = startGen || 1;
  }

  // Create a history change event from an updateDoc-style change
  // object.
  function historyChangeFromChange(doc, change) {
    var histChange = {from: copyPos(change.from), to: changeEnd(change), text: getBetween(doc, change.from, change.to)};
    attachLocalSpans(doc, histChange, change.from.line, change.to.line + 1);
    linkedDocs(doc, function(doc) {attachLocalSpans(doc, histChange, change.from.line, change.to.line + 1);}, true);
    return histChange;
  }

  // Pop all selection events off the end of a history array. Stop at
  // a change event.
  function clearSelectionEvents(array) {
    while (array.length) {
      var last = lst(array);
      if (last.ranges) array.pop();
      else break;
    }
  }

  // Find the top change event in the history. Pop off selection
  // events that are in the way.
  function lastChangeEvent(hist, force) {
    if (force) {
      clearSelectionEvents(hist.done);
      return lst(hist.done);
    } else if (hist.done.length && !lst(hist.done).ranges) {
      return lst(hist.done);
    } else if (hist.done.length > 1 && !hist.done[hist.done.length - 2].ranges) {
      hist.done.pop();
      return lst(hist.done);
    }
  }

  // Register a change in the history. Merges changes that are within
  // a single operation, ore are close together with an origin that
  // allows merging (starting with "+") into a single event.
  function addChangeToHistory(doc, change, selAfter, opId) {
    var hist = doc.history;
    hist.undone.length = 0;
    var time = +new Date, cur;

    if ((hist.lastOp == opId ||
         hist.lastOrigin == change.origin && change.origin &&
         ((change.origin.charAt(0) == "+" && doc.cm && hist.lastModTime > time - doc.cm.options.historyEventDelay) ||
          change.origin.charAt(0) == "*")) &&
        (cur = lastChangeEvent(hist, hist.lastOp == opId))) {
      // Merge this change into the last event
      var last = lst(cur.changes);
      if (cmp(change.from, change.to) == 0 && cmp(change.from, last.to) == 0) {
        // Optimized case for simple insertion -- don't want to add
        // new changesets for every character typed
        last.to = changeEnd(change);
      } else {
        // Add new sub-event
        cur.changes.push(historyChangeFromChange(doc, change));
      }
    } else {
      // Can not be merged, start a new event.
      var before = lst(hist.done);
      if (!before || !before.ranges)
        pushSelectionToHistory(doc.sel, hist.done);
      cur = {changes: [historyChangeFromChange(doc, change)],
             generation: hist.generation};
      hist.done.push(cur);
      while (hist.done.length > hist.undoDepth) {
        hist.done.shift();
        if (!hist.done[0].ranges) hist.done.shift();
      }
    }
    hist.done.push(selAfter);
    hist.generation = ++hist.maxGeneration;
    hist.lastModTime = hist.lastSelTime = time;
    hist.lastOp = hist.lastSelOp = opId;
    hist.lastOrigin = hist.lastSelOrigin = change.origin;

    if (!last) signal(doc, "historyAdded");
  }

  function selectionEventCanBeMerged(doc, origin, prev, sel) {
    var ch = origin.charAt(0);
    return ch == "*" ||
      ch == "+" &&
      prev.ranges.length == sel.ranges.length &&
      prev.somethingSelected() == sel.somethingSelected() &&
      new Date - doc.history.lastSelTime <= (doc.cm ? doc.cm.options.historyEventDelay : 500);
  }

  // Called whenever the selection changes, sets the new selection as
  // the pending selection in the history, and pushes the old pending
  // selection into the 'done' array when it was significantly
  // different (in number of selected ranges, emptiness, or time).
  function addSelectionToHistory(doc, sel, opId, options) {
    var hist = doc.history, origin = options && options.origin;

    // A new event is started when the previous origin does not match
    // the current, or the origins don't allow matching. Origins
    // starting with * are always merged, those starting with + are
    // merged when similar and close together in time.
    if (opId == hist.lastSelOp ||
        (origin && hist.lastSelOrigin == origin &&
         (hist.lastModTime == hist.lastSelTime && hist.lastOrigin == origin ||
          selectionEventCanBeMerged(doc, origin, lst(hist.done), sel))))
      hist.done[hist.done.length - 1] = sel;
    else
      pushSelectionToHistory(sel, hist.done);

    hist.lastSelTime = +new Date;
    hist.lastSelOrigin = origin;
    hist.lastSelOp = opId;
    if (options && options.clearRedo !== false)
      clearSelectionEvents(hist.undone);
  }

  function pushSelectionToHistory(sel, dest) {
    var top = lst(dest);
    if (!(top && top.ranges && top.equals(sel)))
      dest.push(sel);
  }

  // Used to store marked span information in the history.
  function attachLocalSpans(doc, change, from, to) {
    var existing = change["spans_" + doc.id], n = 0;
    doc.iter(Math.max(doc.first, from), Math.min(doc.first + doc.size, to), function(line) {
      if (line.markedSpans)
        (existing || (existing = change["spans_" + doc.id] = {}))[n] = line.markedSpans;
      ++n;
    });
  }

  // When un/re-doing restores text containing marked spans, those
  // that have been explicitly cleared should not be restored.
  function removeClearedSpans(spans) {
    if (!spans) return null;
    for (var i = 0, out; i < spans.length; ++i) {
      if (spans[i].marker.explicitlyCleared) { if (!out) out = spans.slice(0, i); }
      else if (out) out.push(spans[i]);
    }
    return !out ? spans : out.length ? out : null;
  }

  // Retrieve and filter the old marked spans stored in a change event.
  function getOldSpans(doc, change) {
    var found = change["spans_" + doc.id];
    if (!found) return null;
    for (var i = 0, nw = []; i < change.text.length; ++i)
      nw.push(removeClearedSpans(found[i]));
    return nw;
  }

  // Used both to provide a JSON-safe object in .getHistory, and, when
  // detaching a document, to split the history in two
  function copyHistoryArray(events, newGroup, instantiateSel) {
    for (var i = 0, copy = []; i < events.length; ++i) {
      var event = events[i];
      if (event.ranges) {
        copy.push(instantiateSel ? Selection.prototype.deepCopy.call(event) : event);
        continue;
      }
      var changes = event.changes, newChanges = [];
      copy.push({changes: newChanges});
      for (var j = 0; j < changes.length; ++j) {
        var change = changes[j], m;
        newChanges.push({from: change.from, to: change.to, text: change.text});
        if (newGroup) for (var prop in change) if (m = prop.match(/^spans_(\d+)$/)) {
          if (indexOf(newGroup, Number(m[1])) > -1) {
            lst(newChanges)[prop] = change[prop];
            delete change[prop];
          }
        }
      }
    }
    return copy;
  }

  // Rebasing/resetting history to deal with externally-sourced changes

  function rebaseHistSelSingle(pos, from, to, diff) {
    if (to < pos.line) {
      pos.line += diff;
    } else if (from < pos.line) {
      pos.line = from;
      pos.ch = 0;
    }
  }

  // Tries to rebase an array of history events given a change in the
  // document. If the change touches the same lines as the event, the
  // event, and everything 'behind' it, is discarded. If the change is
  // before the event, the event's positions are updated. Uses a
  // copy-on-write scheme for the positions, to avoid having to
  // reallocate them all on every rebase, but also avoid problems with
  // shared position objects being unsafely updated.
  function rebaseHistArray(array, from, to, diff) {
    for (var i = 0; i < array.length; ++i) {
      var sub = array[i], ok = true;
      if (sub.ranges) {
        if (!sub.copied) { sub = array[i] = sub.deepCopy(); sub.copied = true; }
        for (var j = 0; j < sub.ranges.length; j++) {
          rebaseHistSelSingle(sub.ranges[j].anchor, from, to, diff);
          rebaseHistSelSingle(sub.ranges[j].head, from, to, diff);
        }
        continue;
      }
      for (var j = 0; j < sub.changes.length; ++j) {
        var cur = sub.changes[j];
        if (to < cur.from.line) {
          cur.from = Pos(cur.from.line + diff, cur.from.ch);
          cur.to = Pos(cur.to.line + diff, cur.to.ch);
        } else if (from <= cur.to.line) {
          ok = false;
          break;
        }
      }
      if (!ok) {
        array.splice(0, i + 1);
        i = 0;
      }
    }
  }

  function rebaseHist(hist, change) {
    var from = change.from.line, to = change.to.line, diff = change.text.length - (to - from) - 1;
    rebaseHistArray(hist.done, from, to, diff);
    rebaseHistArray(hist.undone, from, to, diff);
  }

  // EVENT UTILITIES

  // Due to the fact that we still support jurassic IE versions, some
  // compatibility wrappers are needed.

  var e_preventDefault = CodeMirror.e_preventDefault = function(e) {
    if (e.preventDefault) e.preventDefault();
    else e.returnValue = false;
  };
  var e_stopPropagation = CodeMirror.e_stopPropagation = function(e) {
    if (e.stopPropagation) e.stopPropagation();
    else e.cancelBubble = true;
  };
  function e_defaultPrevented(e) {
    return e.defaultPrevented != null ? e.defaultPrevented : e.returnValue == false;
  }
  var e_stop = CodeMirror.e_stop = function(e) {e_preventDefault(e); e_stopPropagation(e);};

  function e_target(e) {return e.target || e.srcElement;}
  function e_button(e) {
    var b = e.which;
    if (b == null) {
      if (e.button & 1) b = 1;
      else if (e.button & 2) b = 3;
      else if (e.button & 4) b = 2;
    }
    if (mac && e.ctrlKey && b == 1) b = 3;
    return b;
  }

  // EVENT HANDLING

  // Lightweight event framework. on/off also work on DOM nodes,
  // registering native DOM handlers.

  var on = CodeMirror.on = function(emitter, type, f) {
    if (emitter.addEventListener)
      emitter.addEventListener(type, f, false);
    else if (emitter.attachEvent)
      emitter.attachEvent("on" + type, f);
    else {
      var map = emitter._handlers || (emitter._handlers = {});
      var arr = map[type] || (map[type] = []);
      arr.push(f);
    }
  };

  var off = CodeMirror.off = function(emitter, type, f) {
    if (emitter.removeEventListener)
      emitter.removeEventListener(type, f, false);
    else if (emitter.detachEvent)
      emitter.detachEvent("on" + type, f);
    else {
      var arr = emitter._handlers && emitter._handlers[type];
      if (!arr) return;
      for (var i = 0; i < arr.length; ++i)
        if (arr[i] == f) { arr.splice(i, 1); break; }
    }
  };

  var signal = CodeMirror.signal = function(emitter, type /*, values...*/) {
    var arr = emitter._handlers && emitter._handlers[type];
    if (!arr) return;
    var args = Array.prototype.slice.call(arguments, 2);
    for (var i = 0; i < arr.length; ++i) arr[i].apply(null, args);
  };

  var orphanDelayedCallbacks = null;

  // Often, we want to signal events at a point where we are in the
  // middle of some work, but don't want the handler to start calling
  // other methods on the editor, which might be in an inconsistent
  // state or simply not expect any other events to happen.
  // signalLater looks whether there are any handlers, and schedules
  // them to be executed when the last operation ends, or, if no
  // operation is active, when a timeout fires.
  function signalLater(emitter, type /*, values...*/) {
    var arr = emitter._handlers && emitter._handlers[type];
    if (!arr) return;
    var args = Array.prototype.slice.call(arguments, 2), list;
    if (operationGroup) {
      list = operationGroup.delayedCallbacks;
    } else if (orphanDelayedCallbacks) {
      list = orphanDelayedCallbacks;
    } else {
      list = orphanDelayedCallbacks = [];
      setTimeout(fireOrphanDelayed, 0);
    }
    function bnd(f) {return function(){f.apply(null, args);};};
    for (var i = 0; i < arr.length; ++i)
      list.push(bnd(arr[i]));
  }

  function fireOrphanDelayed() {
    var delayed = orphanDelayedCallbacks;
    orphanDelayedCallbacks = null;
    for (var i = 0; i < delayed.length; ++i) delayed[i]();
  }

  // The DOM events that CodeMirror handles can be overridden by
  // registering a (non-DOM) handler on the editor for the event name,
  // and preventDefault-ing the event in that handler.
  function signalDOMEvent(cm, e, override) {
    if (typeof e == "string")
      e = {type: e, preventDefault: function() { this.defaultPrevented = true; }};
    signal(cm, override || e.type, cm, e);
    return e_defaultPrevented(e) || e.codemirrorIgnore;
  }

  function signalCursorActivity(cm) {
    var arr = cm._handlers && cm._handlers.cursorActivity;
    if (!arr) return;
    var set = cm.curOp.cursorActivityHandlers || (cm.curOp.cursorActivityHandlers = []);
    for (var i = 0; i < arr.length; ++i) if (indexOf(set, arr[i]) == -1)
      set.push(arr[i]);
  }

  function hasHandler(emitter, type) {
    var arr = emitter._handlers && emitter._handlers[type];
    return arr && arr.length > 0;
  }

  // Add on and off methods to a constructor's prototype, to make
  // registering events on such objects more convenient.
  function eventMixin(ctor) {
    ctor.prototype.on = function(type, f) {on(this, type, f);};
    ctor.prototype.off = function(type, f) {off(this, type, f);};
  }

  // MISC UTILITIES

  // Number of pixels added to scroller and sizer to hide scrollbar
  var scrollerGap = 30;

  // Returned or thrown by various protocols to signal 'I'm not
  // handling this'.
  var Pass = CodeMirror.Pass = {toString: function(){return "CodeMirror.Pass";}};

  // Reused option objects for setSelection & friends
  var sel_dontScroll = {scroll: false}, sel_mouse = {origin: "*mouse"}, sel_move = {origin: "+move"};

  function Delayed() {this.id = null;}
  Delayed.prototype.set = function(ms, f) {
    clearTimeout(this.id);
    this.id = setTimeout(f, ms);
  };

  // Counts the column offset in a string, taking tabs into account.
  // Used mostly to find indentation.
  var countColumn = CodeMirror.countColumn = function(string, end, tabSize, startIndex, startValue) {
    if (end == null) {
      end = string.search(/[^\s\u00a0]/);
      if (end == -1) end = string.length;
    }
    for (var i = startIndex || 0, n = startValue || 0;;) {
      var nextTab = string.indexOf("\t", i);
      if (nextTab < 0 || nextTab >= end)
        return n + (end - i);
      n += nextTab - i;
      n += tabSize - (n % tabSize);
      i = nextTab + 1;
    }
  };

  // The inverse of countColumn -- find the offset that corresponds to
  // a particular column.
  function findColumn(string, goal, tabSize) {
    for (var pos = 0, col = 0;;) {
      var nextTab = string.indexOf("\t", pos);
      if (nextTab == -1) nextTab = string.length;
      var skipped = nextTab - pos;
      if (nextTab == string.length || col + skipped >= goal)
        return pos + Math.min(skipped, goal - col);
      col += nextTab - pos;
      col += tabSize - (col % tabSize);
      pos = nextTab + 1;
      if (col >= goal) return pos;
    }
  }

  var spaceStrs = [""];
  function spaceStr(n) {
    while (spaceStrs.length <= n)
      spaceStrs.push(lst(spaceStrs) + " ");
    return spaceStrs[n];
  }

  function lst(arr) { return arr[arr.length-1]; }

  var selectInput = function(node) { node.select(); };
  if (ios) // Mobile Safari apparently has a bug where select() is broken.
    selectInput = function(node) { node.selectionStart = 0; node.selectionEnd = node.value.length; };
  else if (ie) // Suppress mysterious IE10 errors
    selectInput = function(node) { try { node.select(); } catch(_e) {} };

  function indexOf(array, elt) {
    for (var i = 0; i < array.length; ++i)
      if (array[i] == elt) return i;
    return -1;
  }
  function map(array, f) {
    var out = [];
    for (var i = 0; i < array.length; i++) out[i] = f(array[i], i);
    return out;
  }

  function nothing() {}

  function createObj(base, props) {
    var inst;
    if (Object.create) {
      inst = Object.create(base);
    } else {
      nothing.prototype = base;
      inst = new nothing();
    }
    if (props) copyObj(props, inst);
    return inst;
  };

  function copyObj(obj, target, overwrite) {
    if (!target) target = {};
    for (var prop in obj)
      if (obj.hasOwnProperty(prop) && (overwrite !== false || !target.hasOwnProperty(prop)))
        target[prop] = obj[prop];
    return target;
  }

  function bind(f) {
    var args = Array.prototype.slice.call(arguments, 1);
    return function(){return f.apply(null, args);};
  }

  var nonASCIISingleCaseWordChar = /[\u00df\u0587\u0590-\u05f4\u0600-\u06ff\u3040-\u309f\u30a0-\u30ff\u3400-\u4db5\u4e00-\u9fcc\uac00-\ud7af]/;
  var isWordCharBasic = CodeMirror.isWordChar = function(ch) {
    return /\w/.test(ch) || ch > "\x80" &&
      (ch.toUpperCase() != ch.toLowerCase() || nonASCIISingleCaseWordChar.test(ch));
  };
  function isWordChar(ch, helper) {
    if (!helper) return isWordCharBasic(ch);
    if (helper.source.indexOf("\\w") > -1 && isWordCharBasic(ch)) return true;
    return helper.test(ch);
  }

  function isEmpty(obj) {
    for (var n in obj) if (obj.hasOwnProperty(n) && obj[n]) return false;
    return true;
  }

  // Extending unicode characters. A series of a non-extending char +
  // any number of extending chars is treated as a single unit as far
  // as editing and measuring is concerned. This is not fully correct,
  // since some scripts/fonts/browsers also treat other configurations
  // of code points as a group.
  var extendingChars = /[\u0300-\u036f\u0483-\u0489\u0591-\u05bd\u05bf\u05c1\u05c2\u05c4\u05c5\u05c7\u0610-\u061a\u064b-\u065e\u0670\u06d6-\u06dc\u06de-\u06e4\u06e7\u06e8\u06ea-\u06ed\u0711\u0730-\u074a\u07a6-\u07b0\u07eb-\u07f3\u0816-\u0819\u081b-\u0823\u0825-\u0827\u0829-\u082d\u0900-\u0902\u093c\u0941-\u0948\u094d\u0951-\u0955\u0962\u0963\u0981\u09bc\u09be\u09c1-\u09c4\u09cd\u09d7\u09e2\u09e3\u0a01\u0a02\u0a3c\u0a41\u0a42\u0a47\u0a48\u0a4b-\u0a4d\u0a51\u0a70\u0a71\u0a75\u0a81\u0a82\u0abc\u0ac1-\u0ac5\u0ac7\u0ac8\u0acd\u0ae2\u0ae3\u0b01\u0b3c\u0b3e\u0b3f\u0b41-\u0b44\u0b4d\u0b56\u0b57\u0b62\u0b63\u0b82\u0bbe\u0bc0\u0bcd\u0bd7\u0c3e-\u0c40\u0c46-\u0c48\u0c4a-\u0c4d\u0c55\u0c56\u0c62\u0c63\u0cbc\u0cbf\u0cc2\u0cc6\u0ccc\u0ccd\u0cd5\u0cd6\u0ce2\u0ce3\u0d3e\u0d41-\u0d44\u0d4d\u0d57\u0d62\u0d63\u0dca\u0dcf\u0dd2-\u0dd4\u0dd6\u0ddf\u0e31\u0e34-\u0e3a\u0e47-\u0e4e\u0eb1\u0eb4-\u0eb9\u0ebb\u0ebc\u0ec8-\u0ecd\u0f18\u0f19\u0f35\u0f37\u0f39\u0f71-\u0f7e\u0f80-\u0f84\u0f86\u0f87\u0f90-\u0f97\u0f99-\u0fbc\u0fc6\u102d-\u1030\u1032-\u1037\u1039\u103a\u103d\u103e\u1058\u1059\u105e-\u1060\u1071-\u1074\u1082\u1085\u1086\u108d\u109d\u135f\u1712-\u1714\u1732-\u1734\u1752\u1753\u1772\u1773\u17b7-\u17bd\u17c6\u17c9-\u17d3\u17dd\u180b-\u180d\u18a9\u1920-\u1922\u1927\u1928\u1932\u1939-\u193b\u1a17\u1a18\u1a56\u1a58-\u1a5e\u1a60\u1a62\u1a65-\u1a6c\u1a73-\u1a7c\u1a7f\u1b00-\u1b03\u1b34\u1b36-\u1b3a\u1b3c\u1b42\u1b6b-\u1b73\u1b80\u1b81\u1ba2-\u1ba5\u1ba8\u1ba9\u1c2c-\u1c33\u1c36\u1c37\u1cd0-\u1cd2\u1cd4-\u1ce0\u1ce2-\u1ce8\u1ced\u1dc0-\u1de6\u1dfd-\u1dff\u200c\u200d\u20d0-\u20f0\u2cef-\u2cf1\u2de0-\u2dff\u302a-\u302f\u3099\u309a\ua66f-\ua672\ua67c\ua67d\ua6f0\ua6f1\ua802\ua806\ua80b\ua825\ua826\ua8c4\ua8e0-\ua8f1\ua926-\ua92d\ua947-\ua951\ua980-\ua982\ua9b3\ua9b6-\ua9b9\ua9bc\uaa29-\uaa2e\uaa31\uaa32\uaa35\uaa36\uaa43\uaa4c\uaab0\uaab2-\uaab4\uaab7\uaab8\uaabe\uaabf\uaac1\uabe5\uabe8\uabed\udc00-\udfff\ufb1e\ufe00-\ufe0f\ufe20-\ufe26\uff9e\uff9f]/;
  function isExtendingChar(ch) { return ch.charCodeAt(0) >= 768 && extendingChars.test(ch); }

  // DOM UTILITIES

  function elt(tag, content, className, style) {
    var e = document.createElement(tag);
    if (className) e.className = className;
    if (style) e.style.cssText = style;
    if (typeof content == "string") e.appendChild(document.createTextNode(content));
    else if (content) for (var i = 0; i < content.length; ++i) e.appendChild(content[i]);
    return e;
  }

  var range;
  if (document.createRange) range = function(node, start, end, endNode) {
    var r = document.createRange();
    r.setEnd(endNode || node, end);
    r.setStart(node, start);
    return r;
  };
  else range = function(node, start, end) {
    var r = document.body.createTextRange();
    try { r.moveToElementText(node.parentNode); }
    catch(e) { return r; }
    r.collapse(true);
    r.moveEnd("character", end);
    r.moveStart("character", start);
    return r;
  };

  function removeChildren(e) {
    for (var count = e.childNodes.length; count > 0; --count)
      e.removeChild(e.firstChild);
    return e;
  }

  function removeChildrenAndAdd(parent, e) {
    return removeChildren(parent).appendChild(e);
  }

  var contains = CodeMirror.contains = function(parent, child) {
    if (child.nodeType == 3) // Android browser always returns false when child is a textnode
      child = child.parentNode;
    if (parent.contains)
      return parent.contains(child);
    do {
      if (child.nodeType == 11) child = child.host;
      if (child == parent) return true;
    } while (child = child.parentNode);
  };

  function activeElt() { return document.activeElement; }
  // Older versions of IE throws unspecified error when touching
  // document.activeElement in some cases (during loading, in iframe)
  if (ie && ie_version < 11) activeElt = function() {
    try { return document.activeElement; }
    catch(e) { return document.body; }
  };

  function classTest(cls) { return new RegExp("(^|\\s)" + cls + "(?:$|\\s)\\s*"); }
  var rmClass = CodeMirror.rmClass = function(node, cls) {
    var current = node.className;
    var match = classTest(cls).exec(current);
    if (match) {
      var after = current.slice(match.index + match[0].length);
      node.className = current.slice(0, match.index) + (after ? match[1] + after : "");
    }
  };
  var addClass = CodeMirror.addClass = function(node, cls) {
    var current = node.className;
    if (!classTest(cls).test(current)) node.className += (current ? " " : "") + cls;
  };
  function joinClasses(a, b) {
    var as = a.split(" ");
    for (var i = 0; i < as.length; i++)
      if (as[i] && !classTest(as[i]).test(b)) b += " " + as[i];
    return b;
  }

  // WINDOW-WIDE EVENTS

  // These must be handled carefully, because naively registering a
  // handler for each editor will cause the editors to never be
  // garbage collected.

  function forEachCodeMirror(f) {
    if (!document.body.getElementsByClassName) return;
    var byClass = document.body.getElementsByClassName("CodeMirror");
    for (var i = 0; i < byClass.length; i++) {
      var cm = byClass[i].CodeMirror;
      if (cm) f(cm);
    }
  }

  var globalsRegistered = false;
  function ensureGlobalHandlers() {
    if (globalsRegistered) return;
    registerGlobalHandlers();
    globalsRegistered = true;
  }
  function registerGlobalHandlers() {
    // When the window resizes, we need to refresh active editors.
    var resizeTimer;
    on(window, "resize", function() {
      if (resizeTimer == null) resizeTimer = setTimeout(function() {
        resizeTimer = null;
        forEachCodeMirror(onResize);
      }, 100);
    });
    // When the window loses focus, we want to show the editor as blurred
    on(window, "blur", function() {
      forEachCodeMirror(onBlur);
    });
  }

  // FEATURE DETECTION

  // Detect drag-and-drop
  var dragAndDrop = function() {
    // There is *some* kind of drag-and-drop support in IE6-8, but I
    // couldn't get it to work yet.
    if (ie && ie_version < 9) return false;
    var div = elt('div');
    return "draggable" in div || "dragDrop" in div;
  }();

  var zwspSupported;
  function zeroWidthElement(measure) {
    if (zwspSupported == null) {
      var test = elt("span", "\u200b");
      removeChildrenAndAdd(measure, elt("span", [test, document.createTextNode("x")]));
      if (measure.firstChild.offsetHeight != 0)
        zwspSupported = test.offsetWidth <= 1 && test.offsetHeight > 2 && !(ie && ie_version < 8);
    }
    var node = zwspSupported ? elt("span", "\u200b") :
      elt("span", "\u00a0", null, "display: inline-block; width: 1px; margin-right: -1px");
    node.setAttribute("cm-text", "");
    return node;
  }

  // Feature-detect IE's crummy client rect reporting for bidi text
  var badBidiRects;
  function hasBadBidiRects(measure) {
    if (badBidiRects != null) return badBidiRects;
    var txt = removeChildrenAndAdd(measure, document.createTextNode("A\u062eA"));
    var r0 = range(txt, 0, 1).getBoundingClientRect();
    if (!r0 || r0.left == r0.right) return false; // Safari returns null in some cases (#2780)
    var r1 = range(txt, 1, 2).getBoundingClientRect();
    return badBidiRects = (r1.right - r0.right < 3);
  }

  // See if "".split is the broken IE version, if so, provide an
  // alternative way to split lines.
  var splitLines = CodeMirror.splitLines = "\n\nb".split(/\n/).length != 3 ? function(string) {
    var pos = 0, result = [], l = string.length;
    while (pos <= l) {
      var nl = string.indexOf("\n", pos);
      if (nl == -1) nl = string.length;
      var line = string.slice(pos, string.charAt(nl - 1) == "\r" ? nl - 1 : nl);
      var rt = line.indexOf("\r");
      if (rt != -1) {
        result.push(line.slice(0, rt));
        pos += rt + 1;
      } else {
        result.push(line);
        pos = nl + 1;
      }
    }
    return result;
  } : function(string){return string.split(/\r\n?|\n/);};

  var hasSelection = window.getSelection ? function(te) {
    try { return te.selectionStart != te.selectionEnd; }
    catch(e) { return false; }
  } : function(te) {
    try {var range = te.ownerDocument.selection.createRange();}
    catch(e) {}
    if (!range || range.parentElement() != te) return false;
    return range.compareEndPoints("StartToEnd", range) != 0;
  };

  var hasCopyEvent = (function() {
    var e = elt("div");
    if ("oncopy" in e) return true;
    e.setAttribute("oncopy", "return;");
    return typeof e.oncopy == "function";
  })();

  var badZoomedRects = null;
  function hasBadZoomedRects(measure) {
    if (badZoomedRects != null) return badZoomedRects;
    var node = removeChildrenAndAdd(measure, elt("span", "x"));
    var normal = node.getBoundingClientRect();
    var fromRange = range(node, 0, 1).getBoundingClientRect();
    return badZoomedRects = Math.abs(normal.left - fromRange.left) > 1;
  }

  // KEY NAMES

  var keyNames = {3: "Enter", 8: "Backspace", 9: "Tab", 13: "Enter", 16: "Shift", 17: "Ctrl", 18: "Alt",
                  19: "Pause", 20: "CapsLock", 27: "Esc", 32: "Space", 33: "PageUp", 34: "PageDown", 35: "End",
                  36: "Home", 37: "Left", 38: "Up", 39: "Right", 40: "Down", 44: "PrintScrn", 45: "Insert",
                  46: "Delete", 59: ";", 61: "=", 91: "Mod", 92: "Mod", 93: "Mod", 107: "=", 109: "-", 127: "Delete",
                  173: "-", 186: ";", 187: "=", 188: ",", 189: "-", 190: ".", 191: "/", 192: "`", 219: "[", 220: "\\",
                  221: "]", 222: "'", 63232: "Up", 63233: "Down", 63234: "Left", 63235: "Right", 63272: "Delete",
                  63273: "Home", 63275: "End", 63276: "PageUp", 63277: "PageDown", 63302: "Insert"};
  CodeMirror.keyNames = keyNames;
  (function() {
    // Number keys
    for (var i = 0; i < 10; i++) keyNames[i + 48] = keyNames[i + 96] = String(i);
    // Alphabetic keys
    for (var i = 65; i <= 90; i++) keyNames[i] = String.fromCharCode(i);
    // Function keys
    for (var i = 1; i <= 12; i++) keyNames[i + 111] = keyNames[i + 63235] = "F" + i;
  })();

  // BIDI HELPERS

  function iterateBidiSections(order, from, to, f) {
    if (!order) return f(from, to, "ltr");
    var found = false;
    for (var i = 0; i < order.length; ++i) {
      var part = order[i];
      if (part.from < to && part.to > from || from == to && part.to == from) {
        f(Math.max(part.from, from), Math.min(part.to, to), part.level == 1 ? "rtl" : "ltr");
        found = true;
      }
    }
    if (!found) f(from, to, "ltr");
  }

  function bidiLeft(part) { return part.level % 2 ? part.to : part.from; }
  function bidiRight(part) { return part.level % 2 ? part.from : part.to; }

  function lineLeft(line) { var order = getOrder(line); return order ? bidiLeft(order[0]) : 0; }
  function lineRight(line) {
    var order = getOrder(line);
    if (!order) return line.text.length;
    return bidiRight(lst(order));
  }

  function lineStart(cm, lineN) {
    var line = getLine(cm.doc, lineN);
    var visual = visualLine(line);
    if (visual != line) lineN = lineNo(visual);
    var order = getOrder(visual);
    var ch = !order ? 0 : order[0].level % 2 ? lineRight(visual) : lineLeft(visual);
    return Pos(lineN, ch);
  }
  function lineEnd(cm, lineN) {
    var merged, line = getLine(cm.doc, lineN);
    while (merged = collapsedSpanAtEnd(line)) {
      line = merged.find(1, true).line;
      lineN = null;
    }
    var order = getOrder(line);
    var ch = !order ? line.text.length : order[0].level % 2 ? lineLeft(line) : lineRight(line);
    return Pos(lineN == null ? lineNo(line) : lineN, ch);
  }
  function lineStartSmart(cm, pos) {
    var start = lineStart(cm, pos.line);
    var line = getLine(cm.doc, start.line);
    var order = getOrder(line);
    if (!order || order[0].level == 0) {
      var firstNonWS = Math.max(0, line.text.search(/\S/));
      var inWS = pos.line == start.line && pos.ch <= firstNonWS && pos.ch;
      return Pos(start.line, inWS ? 0 : firstNonWS);
    }
    return start;
  }

  function compareBidiLevel(order, a, b) {
    var linedir = order[0].level;
    if (a == linedir) return true;
    if (b == linedir) return false;
    return a < b;
  }
  var bidiOther;
  function getBidiPartAt(order, pos) {
    bidiOther = null;
    for (var i = 0, found; i < order.length; ++i) {
      var cur = order[i];
      if (cur.from < pos && cur.to > pos) return i;
      if ((cur.from == pos || cur.to == pos)) {
        if (found == null) {
          found = i;
        } else if (compareBidiLevel(order, cur.level, order[found].level)) {
          if (cur.from != cur.to) bidiOther = found;
          return i;
        } else {
          if (cur.from != cur.to) bidiOther = i;
          return found;
        }
      }
    }
    return found;
  }

  function moveInLine(line, pos, dir, byUnit) {
    if (!byUnit) return pos + dir;
    do pos += dir;
    while (pos > 0 && isExtendingChar(line.text.charAt(pos)));
    return pos;
  }

  // This is needed in order to move 'visually' through bi-directional
  // text -- i.e., pressing left should make the cursor go left, even
  // when in RTL text. The tricky part is the 'jumps', where RTL and
  // LTR text touch each other. This often requires the cursor offset
  // to move more than one unit, in order to visually move one unit.
  function moveVisually(line, start, dir, byUnit) {
    var bidi = getOrder(line);
    if (!bidi) return moveLogically(line, start, dir, byUnit);
    var pos = getBidiPartAt(bidi, start), part = bidi[pos];
    var target = moveInLine(line, start, part.level % 2 ? -dir : dir, byUnit);

    for (;;) {
      if (target > part.from && target < part.to) return target;
      if (target == part.from || target == part.to) {
        if (getBidiPartAt(bidi, target) == pos) return target;
        part = bidi[pos += dir];
        return (dir > 0) == part.level % 2 ? part.to : part.from;
      } else {
        part = bidi[pos += dir];
        if (!part) return null;
        if ((dir > 0) == part.level % 2)
          target = moveInLine(line, part.to, -1, byUnit);
        else
          target = moveInLine(line, part.from, 1, byUnit);
      }
    }
  }

  function moveLogically(line, start, dir, byUnit) {
    var target = start + dir;
    if (byUnit) while (target > 0 && isExtendingChar(line.text.charAt(target))) target += dir;
    return target < 0 || target > line.text.length ? null : target;
  }

  // Bidirectional ordering algorithm
  // See http://unicode.org/reports/tr9/tr9-13.html for the algorithm
  // that this (partially) implements.

  // One-char codes used for character types:
  // L (L):   Left-to-Right
  // R (R):   Right-to-Left
  // r (AL):  Right-to-Left Arabic
  // 1 (EN):  European Number
  // + (ES):  European Number Separator
  // % (ET):  European Number Terminator
  // n (AN):  Arabic Number
  // , (CS):  Common Number Separator
  // m (NSM): Non-Spacing Mark
  // b (BN):  Boundary Neutral
  // s (B):   Paragraph Separator
  // t (S):   Segment Separator
  // w (WS):  Whitespace
  // N (ON):  Other Neutrals

  // Returns null if characters are ordered as they appear
  // (left-to-right), or an array of sections ({from, to, level}
  // objects) in the order in which they occur visually.
  var bidiOrdering = (function() {
    // Character types for codepoints 0 to 0xff
    var lowTypes = "bbbbbbbbbtstwsbbbbbbbbbbbbbbssstwNN%%%NNNNNN,N,N1111111111NNNNNNNLLLLLLLLLLLLLLLLLLLLLLLLLLNNNNNNLLLLLLLLLLLLLLLLLLLLLLLLLLNNNNbbbbbbsbbbbbbbbbbbbbbbbbbbbbbbbbb,N%%%%NNNNLNNNNN%%11NLNNN1LNNNNNLLLLLLLLLLLLLLLLLLLLLLLNLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLN";
    // Character types for codepoints 0x600 to 0x6ff
    var arabicTypes = "rrrrrrrrrrrr,rNNmmmmmmrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrmmmmmmmmmmmmmmrrrrrrrnnnnnnnnnn%nnrrrmrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrmmmmmmmmmmmmmmmmmmmNmmmm";
    function charType(code) {
      if (code <= 0xf7) return lowTypes.charAt(code);
      else if (0x590 <= code && code <= 0x5f4) return "R";
      else if (0x600 <= code && code <= 0x6ed) return arabicTypes.charAt(code - 0x600);
      else if (0x6ee <= code && code <= 0x8ac) return "r";
      else if (0x2000 <= code && code <= 0x200b) return "w";
      else if (code == 0x200c) return "b";
      else return "L";
    }

    var bidiRE = /[\u0590-\u05f4\u0600-\u06ff\u0700-\u08ac]/;
    var isNeutral = /[stwN]/, isStrong = /[LRr]/, countsAsLeft = /[Lb1n]/, countsAsNum = /[1n]/;
    // Browsers seem to always treat the boundaries of block elements as being L.
    var outerType = "L";

    function BidiSpan(level, from, to) {
      this.level = level;
      this.from = from; this.to = to;
    }

    return function(str) {
      if (!bidiRE.test(str)) return false;
      var len = str.length, types = [];
      for (var i = 0, type; i < len; ++i)
        types.push(type = charType(str.charCodeAt(i)));

      // W1. Examine each non-spacing mark (NSM) in the level run, and
      // change the type of the NSM to the type of the previous
      // character. If the NSM is at the start of the level run, it will
      // get the type of sor.
      for (var i = 0, prev = outerType; i < len; ++i) {
        var type = types[i];
        if (type == "m") types[i] = prev;
        else prev = type;
      }

      // W2. Search backwards from each instance of a European number
      // until the first strong type (R, L, AL, or sor) is found. If an
      // AL is found, change the type of the European number to Arabic
      // number.
      // W3. Change all ALs to R.
      for (var i = 0, cur = outerType; i < len; ++i) {
        var type = types[i];
        if (type == "1" && cur == "r") types[i] = "n";
        else if (isStrong.test(type)) { cur = type; if (type == "r") types[i] = "R"; }
      }

      // W4. A single European separator between two European numbers
      // changes to a European number. A single common separator between
      // two numbers of the same type changes to that type.
      for (var i = 1, prev = types[0]; i < len - 1; ++i) {
        var type = types[i];
        if (type == "+" && prev == "1" && types[i+1] == "1") types[i] = "1";
        else if (type == "," && prev == types[i+1] &&
                 (prev == "1" || prev == "n")) types[i] = prev;
        prev = type;
      }

      // W5. A sequence of European terminators adjacent to European
      // numbers changes to all European numbers.
      // W6. Otherwise, separators and terminators change to Other
      // Neutral.
      for (var i = 0; i < len; ++i) {
        var type = types[i];
        if (type == ",") types[i] = "N";
        else if (type == "%") {
          for (var end = i + 1; end < len && types[end] == "%"; ++end) {}
          var replace = (i && types[i-1] == "!") || (end < len && types[end] == "1") ? "1" : "N";
          for (var j = i; j < end; ++j) types[j] = replace;
          i = end - 1;
        }
      }

      // W7. Search backwards from each instance of a European number
      // until the first strong type (R, L, or sor) is found. If an L is
      // found, then change the type of the European number to L.
      for (var i = 0, cur = outerType; i < len; ++i) {
        var type = types[i];
        if (cur == "L" && type == "1") types[i] = "L";
        else if (isStrong.test(type)) cur = type;
      }

      // N1. A sequence of neutrals takes the direction of the
      // surrounding strong text if the text on both sides has the same
      // direction. European and Arabic numbers act as if they were R in
      // terms of their influence on neutrals. Start-of-level-run (sor)
      // and end-of-level-run (eor) are used at level run boundaries.
      // N2. Any remaining neutrals take the embedding direction.
      for (var i = 0; i < len; ++i) {
        if (isNeutral.test(types[i])) {
          for (var end = i + 1; end < len && isNeutral.test(types[end]); ++end) {}
          var before = (i ? types[i-1] : outerType) == "L";
          var after = (end < len ? types[end] : outerType) == "L";
          var replace = before || after ? "L" : "R";
          for (var j = i; j < end; ++j) types[j] = replace;
          i = end - 1;
        }
      }

      // Here we depart from the documented algorithm, in order to avoid
      // building up an actual levels array. Since there are only three
      // levels (0, 1, 2) in an implementation that doesn't take
      // explicit embedding into account, we can build up the order on
      // the fly, without following the level-based algorithm.
      var order = [], m;
      for (var i = 0; i < len;) {
        if (countsAsLeft.test(types[i])) {
          var start = i;
          for (++i; i < len && countsAsLeft.test(types[i]); ++i) {}
          order.push(new BidiSpan(0, start, i));
        } else {
          var pos = i, at = order.length;
          for (++i; i < len && types[i] != "L"; ++i) {}
          for (var j = pos; j < i;) {
            if (countsAsNum.test(types[j])) {
              if (pos < j) order.splice(at, 0, new BidiSpan(1, pos, j));
              var nstart = j;
              for (++j; j < i && countsAsNum.test(types[j]); ++j) {}
              order.splice(at, 0, new BidiSpan(2, nstart, j));
              pos = j;
            } else ++j;
          }
          if (pos < i) order.splice(at, 0, new BidiSpan(1, pos, i));
        }
      }
      if (order[0].level == 1 && (m = str.match(/^\s+/))) {
        order[0].from = m[0].length;
        order.unshift(new BidiSpan(0, 0, m[0].length));
      }
      if (lst(order).level == 1 && (m = str.match(/\s+$/))) {
        lst(order).to -= m[0].length;
        order.push(new BidiSpan(0, len - m[0].length, len));
      }
      if (order[0].level == 2)
        order.unshift(new BidiSpan(1, order[0].to, order[0].to));
      if (order[0].level != lst(order).level)
        order.push(new BidiSpan(order[0].level, len, len));

      return order;
    };
  })();

  // THE END

  CodeMirror.version = "5.3.0";

  return CodeMirror;
});

},{}],12:[function(require,module,exports){
module.exports = require('./lib/transformer').transform;

},{"./lib/transformer":19}],13:[function(require,module,exports){
// from esprima-fb/esprima.js

var XHTMLEntities = {
  quot: '\u0022',
  amp: '&',
  apos: "\u0027",
  lt: "<",
  gt: ">",
  nbsp: "\u00A0",
  iexcl: "\u00A1",
  cent: "\u00A2",
  pound: "\u00A3",
  curren: "\u00A4",
  yen: "\u00A5",
  brvbar: "\u00A6",
  sect: "\u00A7",
  uml: "\u00A8",
  copy: "\u00A9",
  ordf: "\u00AA",
  laquo: "\u00AB",
  not: "\u00AC",
  shy: "\u00AD",
  reg: "\u00AE",
  macr: "\u00AF",
  deg: "\u00B0",
  plusmn: "\u00B1",
  sup2: "\u00B2",
  sup3: "\u00B3",
  acute: "\u00B4",
  micro: "\u00B5",
  para: "\u00B6",
  middot: "\u00B7",
  cedil: "\u00B8",
  sup1: "\u00B9",
  ordm: "\u00BA",
  raquo: "\u00BB",
  frac14: "\u00BC",
  frac12: "\u00BD",
  frac34: "\u00BE",
  iquest: "\u00BF",
  Agrave: "\u00C0",
  Aacute: "\u00C1",
  Acirc: "\u00C2",
  Atilde: "\u00C3",
  Auml: "\u00C4",
  Aring: "\u00C5",
  AElig: "\u00C6",
  Ccedil: "\u00C7",
  Egrave: "\u00C8",
  Eacute: "\u00C9",
  Ecirc: "\u00CA",
  Euml: "\u00CB",
  Igrave: "\u00CC",
  Iacute: "\u00CD",
  Icirc: "\u00CE",
  Iuml: "\u00CF",
  ETH: "\u00D0",
  Ntilde: "\u00D1",
  Ograve: "\u00D2",
  Oacute: "\u00D3",
  Ocirc: "\u00D4",
  Otilde: "\u00D5",
  Ouml: "\u00D6",
  times: "\u00D7",
  Oslash: "\u00D8",
  Ugrave: "\u00D9",
  Uacute: "\u00DA",
  Ucirc: "\u00DB",
  Uuml: "\u00DC",
  Yacute: "\u00DD",
  THORN: "\u00DE",
  szlig: "\u00DF",
  agrave: "\u00E0",
  aacute: "\u00E1",
  acirc: "\u00E2",
  atilde: "\u00E3",
  auml: "\u00E4",
  aring: "\u00E5",
  aelig: "\u00E6",
  ccedil: "\u00E7",
  egrave: "\u00E8",
  eacute: "\u00E9",
  ecirc: "\u00EA",
  euml: "\u00EB",
  igrave: "\u00EC",
  iacute: "\u00ED",
  icirc: "\u00EE",
  iuml: "\u00EF",
  eth: "\u00F0",
  ntilde: "\u00F1",
  ograve: "\u00F2",
  oacute: "\u00F3",
  ocirc: "\u00F4",
  otilde: "\u00F5",
  ouml: "\u00F6",
  divide: "\u00F7",
  oslash: "\u00F8",
  ugrave: "\u00F9",
  uacute: "\u00FA",
  ucirc: "\u00FB",
  uuml: "\u00FC",
  yacute: "\u00FD",
  thorn: "\u00FE",
  yuml: "\u00FF",
  OElig: "\u0152",
  oelig: "\u0153",
  Scaron: "\u0160",
  scaron: "\u0161",
  Yuml: "\u0178",
  fnof: "\u0192",
  circ: "\u02C6",
  tilde: "\u02DC",
  Alpha: "\u0391",
  Beta: "\u0392",
  Gamma: "\u0393",
  Delta: "\u0394",
  Epsilon: "\u0395",
  Zeta: "\u0396",
  Eta: "\u0397",
  Theta: "\u0398",
  Iota: "\u0399",
  Kappa: "\u039A",
  Lambda: "\u039B",
  Mu: "\u039C",
  Nu: "\u039D",
  Xi: "\u039E",
  Omicron: "\u039F",
  Pi: "\u03A0",
  Rho: "\u03A1",
  Sigma: "\u03A3",
  Tau: "\u03A4",
  Upsilon: "\u03A5",
  Phi: "\u03A6",
  Chi: "\u03A7",
  Psi: "\u03A8",
  Omega: "\u03A9",
  alpha: "\u03B1",
  beta: "\u03B2",
  gamma: "\u03B3",
  delta: "\u03B4",
  epsilon: "\u03B5",
  zeta: "\u03B6",
  eta: "\u03B7",
  theta: "\u03B8",
  iota: "\u03B9",
  kappa: "\u03BA",
  lambda: "\u03BB",
  mu: "\u03BC",
  nu: "\u03BD",
  xi: "\u03BE",
  omicron: "\u03BF",
  pi: "\u03C0",
  rho: "\u03C1",
  sigmaf: "\u03C2",
  sigma: "\u03C3",
  tau: "\u03C4",
  upsilon: "\u03C5",
  phi: "\u03C6",
  chi: "\u03C7",
  psi: "\u03C8",
  omega: "\u03C9",
  thetasym: "\u03D1",
  upsih: "\u03D2",
  piv: "\u03D6",
  ensp: "\u2002",
  emsp: "\u2003",
  thinsp: "\u2009",
  zwnj: "\u200C",
  zwj: "\u200D",
  lrm: "\u200E",
  rlm: "\u200F",
  ndash: "\u2013",
  mdash: "\u2014",
  lsquo: "\u2018",
  rsquo: "\u2019",
  sbquo: "\u201A",
  ldquo: "\u201C",
  rdquo: "\u201D",
  bdquo: "\u201E",
  dagger: "\u2020",
  Dagger: "\u2021",
  bull: "\u2022",
  hellip: "\u2026",
  permil: "\u2030",
  prime: "\u2032",
  Prime: "\u2033",
  lsaquo: "\u2039",
  rsaquo: "\u203A",
  oline: "\u203E",
  frasl: "\u2044",
  euro: "\u20AC",
  image: "\u2111",
  weierp: "\u2118",
  real: "\u211C",
  trade: "\u2122",
  alefsym: "\u2135",
  larr: "\u2190",
  uarr: "\u2191",
  rarr: "\u2192",
  darr: "\u2193",
  harr: "\u2194",
  crarr: "\u21B5",
  lArr: "\u21D0",
  uArr: "\u21D1",
  rArr: "\u21D2",
  dArr: "\u21D3",
  hArr: "\u21D4",
  forall: "\u2200",
  part: "\u2202",
  exist: "\u2203",
  empty: "\u2205",
  nabla: "\u2207",
  isin: "\u2208",
  notin: "\u2209",
  ni: "\u220B",
  prod: "\u220F",
  sum: "\u2211",
  minus: "\u2212",
  lowast: "\u2217",
  radic: "\u221A",
  prop: "\u221D",
  infin: "\u221E",
  ang: "\u2220",
  and: "\u2227",
  or: "\u2228",
  cap: "\u2229",
  cup: "\u222A",
  "int": "\u222B",
  there4: "\u2234",
  sim: "\u223C",
  cong: "\u2245",
  asymp: "\u2248",
  ne: "\u2260",
  equiv: "\u2261",
  le: "\u2264",
  ge: "\u2265",
  sub: "\u2282",
  sup: "\u2283",
  nsub: "\u2284",
  sube: "\u2286",
  supe: "\u2287",
  oplus: "\u2295",
  otimes: "\u2297",
  perp: "\u22A5",
  sdot: "\u22C5",
  lceil: "\u2308",
  rceil: "\u2309",
  lfloor: "\u230A",
  rfloor: "\u230B",
  lang: "\u2329",
  rang: "\u232A",
  loz: "\u25CA",
  spades: "\u2660",
  clubs: "\u2663",
  hearts: "\u2665",
  diams: "\u2666"
};

module.exports = function decode(str) {
  return str
    .replace(/&#(\d+);?/g, function (_, code) {
      return String.fromCharCode(parseInt(code, 10));
    })
    .replace(/&#[xX]([A-Fa-f0-9]+);?/g, function (_, hex) {
      return String.fromCharCode(parseInt(hex, 16));
    })
    .replace(/&([^;\W]+;?)/g, function (m, e) {
      var ee = e.replace(/;$/, '');
      var entity = XHTMLEntities[e]
        || (e.match(/;$/) && XHTMLEntities[ee])
      ;
      
      if (entity) {
        return entity;
      }
      else {
        return m;
      }
    })
}

},{}],14:[function(require,module,exports){
(function (process){
// Generated by CoffeeScript 1.9.1
var extend, flatten, last, ref, ref1, repeat, syntaxErrorToString;

exports.starts = function(string, literal, start) {
  return literal === string.substr(start, literal.length);
};

exports.ends = function(string, literal, back) {
  var len;
  len = literal.length;
  return literal === string.substr(string.length - len - (back || 0), len);
};

exports.repeat = repeat = function(str, n) {
  var res;
  res = '';
  while (n > 0) {
    if (n & 1) {
      res += str;
    }
    n >>>= 1;
    str += str;
  }
  return res;
};

exports.compact = function(array) {
  var i, item, len1, results;
  results = [];
  for (i = 0, len1 = array.length; i < len1; i++) {
    item = array[i];
    if (item) {
      results.push(item);
    }
  }
  return results;
};

exports.count = function(string, substr) {
  var num, pos;
  num = pos = 0;
  if (!substr.length) {
    return 1 / 0;
  }
  while (pos = 1 + string.indexOf(substr, pos)) {
    num++;
  }
  return num;
};

exports.merge = function(options, overrides) {
  return extend(extend({}, options), overrides);
};

extend = exports.extend = function(object, properties) {
  var key, val;
  for (key in properties) {
    val = properties[key];
    object[key] = val;
  }
  return object;
};

exports.flatten = flatten = function(array) {
  var element, flattened, i, len1;
  flattened = [];
  for (i = 0, len1 = array.length; i < len1; i++) {
    element = array[i];
    if (element instanceof Array) {
      flattened = flattened.concat(flatten(element));
    } else {
      flattened.push(element);
    }
  }
  return flattened;
};

exports.del = function(obj, key) {
  var val;
  val = obj[key];
  delete obj[key];
  return val;
};

exports.last = last = function(array, back) {
  return array[array.length - (back || 0) - 1];
};

exports.some = (ref = Array.prototype.some) != null ? ref : function(fn) {
  var e, i, len1;
  for (i = 0, len1 = this.length; i < len1; i++) {
    e = this[i];
    if (fn(e)) {
      return true;
    }
  }
  return false;
};

exports.find = (ref1 = Array.prototype.find) != null ? ref1 : function(fn) {
  var e, i, len1;
  for (i = 0, len1 = this.length; i < len1; i++) {
    e = this[i];
    if (fn(e)) {
      return e;
    }
  }
};

exports.throwSyntaxError = function(message, location) {
  var error;
  error = new SyntaxError(message);
  error.location = location;
  error.toString = syntaxErrorToString;
  error.stack = error.toString();
  throw error;
};

exports.updateSyntaxError = function(error, code, filename) {
  if (error.toString === syntaxErrorToString) {
    error.code || (error.code = code);
    error.filename || (error.filename = filename);
    error.stack = error.toString();
  }
  return error;
};

syntaxErrorToString = function() {
  var codeLine, colorize, colorsEnabled, end, filename, first_column, first_line, last_column, last_line, marker, ref2, ref3, start;
  if (!(this.code && this.location)) {
    return Error.prototype.toString.call(this);
  }
  ref2 = this.location, first_line = ref2.first_line, first_column = ref2.first_column, last_line = ref2.last_line, last_column = ref2.last_column;
  if (last_line == null) {
    last_line = first_line;
  }
  if (last_column == null) {
    last_column = first_column;
  }
  filename = this.filename || '[stdin]';
  codeLine = this.code.split('\n')[first_line];
  start = first_column;
  end = first_line === last_line ? last_column + 1 : codeLine.length;
  marker = repeat(' ', start) + repeat('^', end - start);
  if (typeof process !== "undefined" && process !== null) {
    colorsEnabled = process.stdout.isTTY && !process.env.NODE_DISABLE_COLORS;
  }
  if ((ref3 = this.colorful) != null ? ref3 : colorsEnabled) {
    colorize = function(str) {
      return "\x1B[1;31m" + str + "\x1B[0m";
    };
    codeLine = codeLine.slice(0, start) + colorize(codeLine.slice(start, end)) + codeLine.slice(end);
    marker = colorize(marker);
  }
  return filename + ":" + (first_line + 1) + ":" + (first_column + 1) + ": error: " + this.message + "\n" + codeLine + "\n" + marker;
};

exports.nameWhitespaceCharacter = function(string) {
  switch (string) {
    case ' ':
      return 'space';
    case '\n':
      return 'newline';
    case '\r':
      return 'carriage return';
    case '\t':
      return 'tab';
    default:
      return string;
  }
};

exports.invertLiterate = function(code) {
  var line, lines, maybe_code;
  maybe_code = true;
  lines = (function() {
    var i, len1, ref2, results;
    ref2 = code.split('\n');
    results = [];
    for (i = 0, len1 = ref2.length; i < len1; i++) {
      line = ref2[i];
      if (maybe_code && /^([ ]{4}|[ ]{0,3}\t)/.test(line)) {
        results.push(line);
      } else if (maybe_code = /^\s*$/.test(line)) {
        results.push(line);
      } else {
        results.push('# ' + line);
      }
    }
    return results;
  })();
  return lines.join('\n');
};

}).call(this,require('_process'))
},{"_process":8}],15:[function(require,module,exports){
// Generated by CoffeeScript 1.9.1
var $, BOM, CJSX_ESC_COMMENT, CLOSING_TAG, COMMENT, HEREDOC, HEREGEX, JSTOKEN, OPENING_TAG, PRAGMA, ParseTreeBranchNode, ParseTreeLeafNode, Parser, REGEX, SIMPLESTR, TAG_ATTRIBUTES, TRAILING_SPACES, WHITESPACE, compact, count, invertLiterate, last, ref, repeat, starts, throwSyntaxError;

ref = require('./helpers'), count = ref.count, starts = ref.starts, compact = ref.compact, last = ref.last, repeat = ref.repeat, throwSyntaxError = ref.throwSyntaxError, invertLiterate = ref.invertLiterate;

$ = require('./symbols');

ParseTreeLeafNode = function(type, value) {
  if (value == null) {
    value = null;
  }
  return {
    type: type,
    value: value
  };
};

ParseTreeBranchNode = function(type, value, children) {
  if (value == null) {
    value = null;
  }
  if (children == null) {
    children = [];
  }
  return {
    type: type,
    value: value,
    children: children
  };
};

module.exports = Parser = (function() {
  function Parser() {}

  Parser.prototype.parse = function(code, opts) {
    var consumed, i, message, ref1, ref2;
    this.opts = opts != null ? opts : {};
    this.parseTree = ParseTreeBranchNode(this.opts.root || $.ROOT);
    this.activeStates = [this.parseTree];
    this.chunkLine = 0;
    this.chunkColumn = 0;
    this.cjsxPragmaChecked = false;
    code = this.clean(code);
    i = 0;
    while ((this.chunk = code.slice(i))) {
      if (this.activeStates.length === 0) {
        break;
      }
      consumed = ((ref1 = this.currentState()) !== $.CJSX_EL && ref1 !== $.CJSX_ATTRIBUTES ? this.csComment() || this.csHeredoc() || this.csString() || this.csRegex() || this.jsEscaped() : void 0) || this.cjsxStart() || this.cjsxAttribute() || this.cjsxComment() || this.cjsxEscape() || this.cjsxUnescape() || this.cjsxEnd() || this.cjsxText() || this.coffeescriptCode();
      ref2 = this.getLineAndColumnFromChunk(consumed), this.chunkLine = ref2[0], this.chunkColumn = ref2[1];
      i += consumed;
    }
    if ((this.activeBranchNode() != null) && this.activeBranchNode() !== this.parseTree) {
      message = "Unexpected end of input: unclosed " + (this.currentState());
      throwSyntaxError(message, {
        first_line: this.chunkLine,
        first_column: this.chunkColumn
      });
    }
    this.remainder = code.slice(i);
    if (!this.opts.recursive) {
      if (this.remainder.length) {
        throwSyntaxError("Unexpected return from root state", {
          first_line: this.chunkLine,
          first_column: this.chunkColumn
        });
      }
    }
    return this.parseTree;
  };

  Parser.prototype.csComment = function() {
    var comment, here, match, pragmaMatch, prefix;
    if (!(match = this.chunk.match(COMMENT))) {
      return 0;
    }
    comment = match[0], here = match[1];
    if (!this.cjsxPragmaChecked) {
      this.cjsxPragmaChecked = true;
      if (pragmaMatch = comment.match(PRAGMA)) {
        if (pragmaMatch && pragmaMatch[1] && pragmaMatch[1].length) {
          prefix = pragmaMatch[1];
        } else {
          prefix = 'React.DOM';
        }
        this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CJSX_PRAGMA, prefix));
        return comment.length;
      }
    }
    this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CS_COMMENT, comment));
    return comment.length;
  };

  Parser.prototype.csHeredoc = function() {
    var heredoc, match;
    if (!(match = HEREDOC.exec(this.chunk))) {
      return 0;
    }
    heredoc = match[0];
    this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CS_HEREDOC, heredoc));
    return heredoc.length;
  };

  Parser.prototype.csString = function() {
    var quote, string;
    switch (quote = this.chunk.charAt(0)) {
      case "'":
        string = SIMPLESTR.exec(this.chunk)[0];
        break;
      case '"':
        string = this.balancedString(this.chunk, '"');
    }
    if (!string) {
      return 0;
    }
    this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CS_STRING, string));
    return string.length;
  };

  Parser.prototype.csRegex = function() {
    var flags, length, match, ref1, regex;
    if (this.chunk.charAt(0) !== '/') {
      return 0;
    }
    if (length = this.csHeregex()) {
      return length;
    }
    if (!(match = REGEX.exec(this.chunk))) {
      return 0;
    }
    ref1 = match, match = ref1[0], regex = ref1[1], flags = ref1[2];
    if (regex.indexOf("\n") > -1) {
      return 0;
    }
    if (regex === '//') {
      return 0;
    }
    this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CS_REGEX, match));
    return match.length;
  };

  Parser.prototype.csHeregex = function() {
    var body, flags, heregex, match;
    if (!(match = HEREGEX.exec(this.chunk))) {
      return 0;
    }
    heregex = match[0], body = match[1], flags = match[2];
    this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CS_HEREGEX, heregex));
    return heregex.length;
  };

  Parser.prototype.jsEscaped = function() {
    var match, script;
    if (!(this.chunk.charAt(0) === '`' && (match = JSTOKEN.exec(this.chunk)))) {
      return 0;
    }
    script = match[0];
    this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.JS_ESC, script));
    return script.length;
  };

  Parser.prototype.cjsxStart = function() {
    var attributesText, input, match, selfClosing, tagName;
    if (!(match = OPENING_TAG.exec(this.chunk))) {
      return 0;
    }
    input = match[0], tagName = match[1], attributesText = match[2], selfClosing = match[3];
    if (!(selfClosing || this.chunk.indexOf("</" + tagName + ">", input.length) > -1)) {
      return 0;
    }
    this.pushActiveBranchNode(ParseTreeBranchNode($.CJSX_EL, tagName));
    this.pushActiveBranchNode(ParseTreeBranchNode($.CJSX_ATTRIBUTES));
    return 1 + tagName.length;
  };

  Parser.prototype.cjsxAttribute = function() {
    var attrName, bareVal, cjsxEscVal, doubleQuotedVal, input, match, singleQuotedVal, spreadAttr, whitespace;
    if (this.currentState() !== $.CJSX_ATTRIBUTES) {
      return 0;
    }
    if (this.chunk.charAt(0) === '/') {
      if (this.chunk.charAt(1) === '>') {
        this.popActiveBranchNode();
        this.popActiveBranchNode();
        return 2;
      } else {
        throwSyntaxError("/ without immediately following > in CJSX tag " + (this.peekActiveState(2).value), {
          first_line: this.chunkLine,
          first_column: this.chunkColumn
        });
      }
    }
    if (this.chunk.charAt(0) === '>') {
      this.popActiveBranchNode();
      return 1;
    }
    if (!(match = TAG_ATTRIBUTES.exec(this.chunk))) {
      return 0;
    }
    input = match[0], attrName = match[1], doubleQuotedVal = match[2], singleQuotedVal = match[3], cjsxEscVal = match[4], bareVal = match[5], spreadAttr = match[6], whitespace = match[7];
    if (attrName) {
      if (doubleQuotedVal != null) {
        this.addLeafNodeToActiveBranch(ParseTreeBranchNode($.CJSX_ATTR_PAIR, null, [ParseTreeLeafNode($.CJSX_ATTR_KEY, "\"" + attrName + "\""), ParseTreeLeafNode($.CJSX_ATTR_VAL, "\"" + doubleQuotedVal + "\"")]));
        return input.length;
      } else if (singleQuotedVal != null) {
        this.addLeafNodeToActiveBranch(ParseTreeBranchNode($.CJSX_ATTR_PAIR, null, [ParseTreeLeafNode($.CJSX_ATTR_KEY, "\"" + attrName + "\""), ParseTreeLeafNode($.CJSX_ATTR_VAL, "'" + singleQuotedVal + "'")]));
        return input.length;
      } else if (cjsxEscVal) {
        this.pushActiveBranchNode(ParseTreeBranchNode($.CJSX_ATTR_PAIR));
        this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CJSX_ATTR_KEY, "\"" + attrName + "\""));
        return input.indexOf('{');
      } else if (bareVal) {
        this.addLeafNodeToActiveBranch(ParseTreeBranchNode($.CJSX_ATTR_PAIR, null, [ParseTreeLeafNode($.CJSX_ATTR_KEY, "\"" + attrName + "\""), ParseTreeLeafNode($.CJSX_ATTR_VAL, bareVal)]));
        return input.length;
      } else {
        this.addLeafNodeToActiveBranch(ParseTreeBranchNode($.CJSX_ATTR_PAIR, null, [ParseTreeLeafNode($.CJSX_ATTR_KEY, "\"" + attrName + "\""), ParseTreeLeafNode($.CJSX_ATTR_VAL, 'true')]));
        return input.length;
      }
    } else if (spreadAttr) {
      this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CJSX_ATTR_SPREAD, spreadAttr));
      return input.length;
    } else if (whitespace != null) {
      this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CJSX_WHITESPACE, whitespace));
      return input.length;
    } else {
      return throwSyntaxError("Invalid attribute " + input + " in CJSX tag " + (this.peekActiveState(2).value), {
        first_line: this.chunkLine,
        first_column: this.chunkColumn
      });
    }
  };

  Parser.prototype.cjsxComment = function() {
    var match;
    match = this.chunk.match(CJSX_ESC_COMMENT);
    if (!match) {
      return 0;
    }
    this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CJSX_COMMENT, match[1]));
    return match[0].length;
  };

  Parser.prototype.cjsxEscape = function() {
    var ref1;
    if (!(this.chunk.charAt(0) === '{' && ((ref1 = this.currentState()) === $.CJSX_EL || ref1 === $.CJSX_ATTR_PAIR))) {
      return 0;
    }
    this.pushActiveBranchNode(ParseTreeBranchNode($.CJSX_ESC));
    this.activeBranchNode().stack = 1;
    return 1;
  };

  Parser.prototype.cjsxUnescape = function() {
    var ref1;
    if (!(this.currentState() === $.CJSX_ESC && this.chunk.charAt(0) === '}')) {
      return 0;
    }
    if (this.activeBranchNode().stack === 0) {
      this.popActiveBranchNode();
      if ((ref1 = this.currentState()) === $.CJSX_ATTR_PAIR) {
        this.popActiveBranchNode();
      }
      return 1;
    } else {
      return 0;
    }
  };

  Parser.prototype.cjsxEnd = function() {
    var input, match, tagName;
    if (this.currentState() !== $.CJSX_EL) {
      return 0;
    }
    if (!(match = CLOSING_TAG.exec(this.chunk))) {
      return 0;
    }
    input = match[0], tagName = match[1];
    if (tagName !== this.activeBranchNode().value) {
      throwSyntaxError("opening CJSX tag " + (this.activeBranchNode().value) + " doesn't match closing CJSX tag " + tagName, {
        first_line: this.chunkLine,
        first_column: this.chunkColumn
      });
    }
    this.popActiveBranchNode();
    return input.length;
  };

  Parser.prototype.cjsxText = function() {
    if (this.currentState() !== $.CJSX_EL) {
      return 0;
    }
    if (this.newestNode().type !== $.CJSX_TEXT) {
      this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CJSX_TEXT, ''));
    }
    this.newestNode().value += this.chunk.charAt(0);
    return 1;
  };

  Parser.prototype.coffeescriptCode = function() {
    if (this.currentState() === $.CJSX_ESC) {
      if (this.chunk.charAt(0) === '{') {
        this.activeBranchNode().stack++;
      } else if (this.chunk.charAt(0) === '}') {
        this.activeBranchNode().stack--;
        if (this.activeBranchNode().stack === 0) {
          return 0;
        }
      }
    }
    if (this.newestNode().type !== $.CS) {
      this.addLeafNodeToActiveBranch(ParseTreeLeafNode($.CS, ''));
    }
    this.newestNode().value += this.chunk.charAt(0);
    return 1;
  };

  Parser.prototype.activeBranchNode = function() {
    return last(this.activeStates);
  };

  Parser.prototype.peekActiveState = function(depth) {
    if (depth == null) {
      depth = 1;
    }
    return this.activeStates.slice(-depth)[0];
  };

  Parser.prototype.currentState = function() {
    return this.activeBranchNode().type;
  };

  Parser.prototype.newestNode = function() {
    return last(this.activeBranchNode().children) || this.activeBranchNode();
  };

  Parser.prototype.pushActiveBranchNode = function(node) {
    this.activeBranchNode().children.push(node);
    return this.activeStates.push(node);
  };

  Parser.prototype.popActiveBranchNode = function() {
    return this.activeStates.pop();
  };

  Parser.prototype.addLeafNodeToActiveBranch = function(node) {
    return this.activeBranchNode().children.push(node);
  };

  Parser.prototype.clean = function(code) {
    var ref1;
    if (code.charCodeAt(0) === BOM) {
      code = code.slice(1);
    }
    code = code.replace(/\r/g, '');
    if ((ref1 = this.opts) != null ? ref1.literate : void 0) {
      code = invertLiterate(code);
    }
    return code;
  };

  Parser.prototype.getLineAndColumnFromChunk = function(offset) {
    var column, lineCount, lines, string;
    if (offset === 0) {
      return [this.chunkLine, this.chunkColumn];
    }
    if (offset >= this.chunk.length) {
      string = this.chunk;
    } else {
      string = this.chunk.slice(0, +(offset - 1) + 1 || 9e9);
    }
    lineCount = count(string, '\n');
    column = this.chunkColumn;
    if (lineCount > 0) {
      lines = string.split('\n');
      column = last(lines).length;
    } else {
      column += string.length;
    }
    return [this.chunkLine + lineCount, column];
  };

  Parser.prototype.balancedString = function(str, end) {
    var continueCount, i, j, letter, match, prev, ref1, stack;
    continueCount = 0;
    stack = [end];
    for (i = j = 1, ref1 = str.length; 1 <= ref1 ? j < ref1 : j > ref1; i = 1 <= ref1 ? ++j : --j) {
      if (continueCount) {
        --continueCount;
        continue;
      }
      switch (letter = str.charAt(i)) {
        case '\\':
          ++continueCount;
          continue;
        case end:
          stack.pop();
          if (!stack.length) {
            return str.slice(0, +i + 1 || 9e9);
          }
          end = stack[stack.length - 1];
          continue;
      }
      if (end === '}' && (letter === '"' || letter === "'")) {
        stack.push(end = letter);
      } else if (end === '}' && letter === '/' && (match = HEREGEX.exec(str.slice(i)) || REGEX.exec(str.slice(i)))) {
        continueCount += match[0].length - 1;
      } else if (end === '}' && letter === '{') {
        stack.push(end = '}');
      } else if (end === '"' && prev === '#' && letter === '{') {
        stack.push(end = '}');
      }
      prev = letter;
    }
    return throwSyntaxError("missing " + (stack.pop()) + ", starting");
  };

  return Parser;

})();

OPENING_TAG = /^<(@?[-A-Za-z0-9_\.]+)((?:(?:(?:\s+[\w-]+(?:\s*=\s*(?:(?:"[^"]*")|(?:'[^']*')|(?:{[\s\S]*?})|[^>\s]+)))|\s+[\w-]+|\s+\{\.\.\.\s*?[^\s{}]+?\s*?\})?)*?\s*)(\/?)>/;

CLOSING_TAG = /^<\/(@?[-A-Za-z0-9_\.]+)[^>]*>/;

TAG_ATTRIBUTES = /(?:([-A-Za-z0-9_]+)(?:\s*=\s*(?:(?:"((?:\\.|[^"])*)")|(?:'((?:\\.|[^'])*)')|(?:{((?:\\.|[\s\S])*)})|([^>\s]+)))?)|(?:\{\.\.\.(\s*?[^\s{}]+?\s*?)\})|([\s\n]+)/;

PRAGMA = /^\s*#\s*@cjsx\s+(\S*)/i;

CJSX_ESC_COMMENT = /^\{#(.*)\}/;

BOM = 65279;

WHITESPACE = /^[^\n\S]+/;

COMMENT = /^###([^#][\s\S]*?)(?:###[^\n\S]*|###$)|^(?:\s*#(?!##[^#]).*)+/;

TRAILING_SPACES = /\s+$/;

HEREDOC = /^("""|''')((?:\\[\s\S]|[^\\])*?)(?:\n[^\n\S]*)?\1/;

SIMPLESTR = /^'[^\\']*(?:\\[\s\S][^\\']*)*'/;

JSTOKEN = /^`[^\\`]*(?:\\.[^\\`]*)*`/;

REGEX = /^(\/(?![\s=])[^[\/\n\\]*(?:(?:\\[\s\S]|\[[^\]\n\\]*(?:\\[\s\S][^\]\n\\]*)*])[^[\/\n\\]*)*\/)([imgy]{0,4})(?!\w)/;

HEREGEX = /^\/{3}((?:\\?[\s\S])+?)\/{3}([imgy]{0,4})(?!\w)/;

},{"./helpers":14,"./symbols":18}],16:[function(require,module,exports){
// Generated by CoffeeScript 1.9.1
var $, SPACES_ONLY, Serialiser, TEXT_LEADING_WHITESPACE, TEXT_TRAILING_WHITESPACE, WHITESPACE_ONLY, containsNewlines, entityDecode, exports, find, firstNonWhitespaceChild, genericBranchSerialiser, genericLeafSerialiser, joinList, last, nodeSerialisers, ref, serialise, stringEscape, tagConvention;

ref = require('./helpers'), last = ref.last, find = ref.find;

$ = require('./symbols');

stringEscape = require('./stringescape');

entityDecode = require('./entitydecode');

module.exports = exports = serialise = function(parseTree) {
  return new Serialiser().serialise(parseTree);
};

Serialiser = (function() {
  function Serialiser() {}

  Serialiser.prototype.serialise = function(parseTree) {
    var domObjectParts;
    if (parseTree.children && parseTree.children.length && parseTree.children[0].type === $.CJSX_PRAGMA) {
      this.domObject = parseTree.children[0].value;
    } else {
      this.domObject = 'React.DOM';
    }
    domObjectParts = this.domObject.split('.');
    if (domObjectParts.length > 0 && domObjectParts[0] !== '') {
      this.reactObject = domObjectParts[0];
    } else {
      this.reactObject = 'React';
    }
    return this.serialiseNode(parseTree);
  };

  Serialiser.prototype.serialiseNode = function(node) {
    var serialised;
    if (nodeSerialisers[node.type] == null) {
      throw new Error("unknown parseTree node type " + node.type);
    }
    serialised = nodeSerialisers[node.type].call(this, node);
    if (!(typeof serialised === 'string' || serialised === null)) {
      throw new Error("serialiser " + node.type + " didn\'t return a string");
    }
    return serialised;
  };

  Serialiser.prototype.serialiseSpreadAndPairAttributes = function(children) {
    var accumulatedWhitespace, assignIndex, assignItem, assigns, assignsWithWhitespace, child, childIndex, flushPairs, j, joinedAssigns, k, lastAssignWithWhitespace, len, len1, pairAttrsBuffer, ref1, trailingWhiteplace;
    assigns = [];
    pairAttrsBuffer = [];
    flushPairs = (function(_this) {
      return function() {
        var serialisedChild, serialisedPairs;
        if (pairAttrsBuffer.length) {
          serialisedChild = _this.serialiseAttributePairs(pairAttrsBuffer);
          if (serialisedChild) {
            assigns.push({
              type: $.CS,
              value: serialisedChild
            });
          } else {
            serialisedPairs = pairAttrsBuffer.map(function(p) {
              return _this.serialiseNode(p);
            }).join('').replace('\n', '\\\n');
            assigns.push({
              type: $.CJSX_WHITESPACE,
              value: serialisedPairs
            });
          }
          return pairAttrsBuffer = [];
        }
      };
    })(this);
    if (((ref1 = firstNonWhitespaceChild(children)) != null ? ref1.type : void 0) === $.CJSX_ATTR_SPREAD) {
      assigns.push({
        type: $.CS,
        value: '{}'
      });
    }
    for (childIndex = j = 0, len = children.length; j < len; childIndex = ++j) {
      child = children[childIndex];
      if (child.type === $.CJSX_ATTR_SPREAD) {
        flushPairs();
        assigns.push({
          type: $.CS,
          value: child.value
        });
      } else {
        pairAttrsBuffer.push(child);
      }
    }
    flushPairs();
    accumulatedWhitespace = '';
    assignsWithWhitespace = [];
    for (assignIndex = k = 0, len1 = assigns.length; k < len1; assignIndex = ++k) {
      assignItem = assigns[assignIndex];
      if (assignItem != null) {
        if (assignItem.type === $.CJSX_WHITESPACE) {
          accumulatedWhitespace += this.serialiseNode(assignItem);
        } else {
          assignsWithWhitespace.push(accumulatedWhitespace + this.serialiseNode(assignItem));
          accumulatedWhitespace = '';
        }
      }
    }
    if (assignsWithWhitespace.length) {
      lastAssignWithWhitespace = assignsWithWhitespace.pop();
      trailingWhiteplace = accumulatedWhitespace.replace('\\\n', '\n');
      assignsWithWhitespace.push(lastAssignWithWhitespace + trailingWhiteplace);
    }
    joinedAssigns = joinList(assignsWithWhitespace);
    return "React.__spread(" + (joinList(assignsWithWhitespace)) + ")";
  };

  Serialiser.prototype.serialiseAttributePairs = function(children) {
    var child, childIndex, indexOfLastSemanticChild, isBeforeLastSemanticChild, ref1, semanticChildren, serialisedChild, serialisedChildren, whitespaceChildren;
    ref1 = children.reduce(function(partitionedChildren, child) {
      if (child.type === $.CJSX_WHITESPACE) {
        partitionedChildren[0].push(child);
      } else {
        partitionedChildren[1].push(child);
      }
      return partitionedChildren;
    }, [[], []]), whitespaceChildren = ref1[0], semanticChildren = ref1[1];
    indexOfLastSemanticChild = children.lastIndexOf(last(semanticChildren));
    isBeforeLastSemanticChild = function(childIndex) {
      return childIndex < indexOfLastSemanticChild;
    };
    if (semanticChildren.length) {
      serialisedChildren = (function() {
        var j, len, results;
        results = [];
        for (childIndex = j = 0, len = children.length; j < len; childIndex = ++j) {
          child = children[childIndex];
          serialisedChild = this.serialiseNode(child);
          if (child.type === $.CJSX_WHITESPACE) {
            if (containsNewlines(serialisedChild)) {
              if (isBeforeLastSemanticChild(childIndex)) {
                results.push(serialisedChild.replace('\n', ' \\\n'));
              } else {
                results.push(serialisedChild);
              }
            } else {
              results.push(null);
            }
          } else if (isBeforeLastSemanticChild(childIndex)) {
            results.push(serialisedChild + ', ');
          } else {
            results.push(serialisedChild);
          }
        }
        return results;
      }).call(this);
      return '{' + serialisedChildren.join('') + '}';
    } else {
      return null;
    }
  };

  return Serialiser;

})();

genericBranchSerialiser = function(node) {
  return node.children.map((function(_this) {
    return function(child) {
      return _this.serialiseNode(child);
    };
  })(this)).join('');
};

genericLeafSerialiser = function(node) {
  return node.value;
};

tagConvention = /^[a-z]|\-/;

nodeSerialisers = {
  ROOT: genericBranchSerialiser,
  CJSX_PRAGMA: function() {
    return "`/** @jsx " + this.domObject + " */`";
  },
  CJSX_EL: function(node) {
    var accumulatedWhitespace, child, element, j, len, ref1, serialisedChild, serialisedChildren;
    serialisedChildren = [];
    accumulatedWhitespace = '';
    ref1 = node.children;
    for (j = 0, len = ref1.length; j < len; j++) {
      child = ref1[j];
      serialisedChild = this.serialiseNode(child);
      if (child != null) {
        if (serialisedChild.length === 0 || WHITESPACE_ONLY.test(serialisedChild)) {
          accumulatedWhitespace += serialisedChild;
        } else {
          serialisedChildren.push(accumulatedWhitespace + serialisedChild);
          accumulatedWhitespace = '';
        }
      }
    }
    if (serialisedChildren.length) {
      serialisedChildren[serialisedChildren.length - 1] += accumulatedWhitespace;
      accumulatedWhitespace = '';
    }
    if (tagConvention.test(node.value)) {
      element = '"' + node.value + '"';
    } else {
      element = node.value;
    }
    return this.reactObject + ".createElement(" + element + ", " + (joinList(serialisedChildren)) + ")";
  },
  CJSX_COMMENT: function(node) {
    return '';
  },
  CJSX_ESC: function(node) {
    var childrenSerialised;
    childrenSerialised = node.children.map((function(_this) {
      return function(child) {
        return _this.serialiseNode(child);
      };
    })(this)).join('');
    return '(' + childrenSerialised + ')';
  },
  CJSX_ATTRIBUTES: function(node) {
    if (node.children.some(function(child) {
      return child.type === $.CJSX_ATTR_SPREAD;
    })) {
      return this.serialiseSpreadAndPairAttributes(node.children);
    } else {
      return this.serialiseAttributePairs(node.children) || 'null';
    }
  },
  CJSX_ATTR_PAIR: function(node) {
    return node.children.map((function(_this) {
      return function(child) {
        return _this.serialiseNode(child);
      };
    })(this)).join(': ');
  },
  CJSX_ATTR_SPREAD: function(node) {
    return node.value;
  },
  CS: genericLeafSerialiser,
  CS_COMMENT: genericLeafSerialiser,
  CS_HEREDOC: genericLeafSerialiser,
  CS_STRING: genericLeafSerialiser,
  CS_REGEX: genericLeafSerialiser,
  CS_HEREGEX: genericLeafSerialiser,
  JS_ESC: genericLeafSerialiser,
  CJSX_WHITESPACE: genericLeafSerialiser,
  CJSX_TEXT: function(node) {
    var escapedText, leftSpace, leftTrim, rightSpace, rightTrim, text, trimmedText;
    text = node.value;
    if (containsNewlines(text)) {
      if (WHITESPACE_ONLY.test(text)) {
        return text;
      } else {
        leftSpace = text.match(TEXT_LEADING_WHITESPACE);
        rightSpace = text.match(TEXT_TRAILING_WHITESPACE);
        if (leftSpace) {
          leftTrim = text.indexOf('\n');
        } else {
          leftTrim = 0;
        }
        if (rightSpace) {
          rightTrim = text.lastIndexOf('\n') + 1;
        } else {
          rightTrim = text.length;
        }
        trimmedText = text.substring(leftTrim, rightTrim);
        escapedText = stringEscape(entityDecode(trimmedText), {
          preserveNewlines: true
        });
        return '"""' + escapedText + '"""';
      }
    } else {
      if (text === '') {
        return null;
      } else {
        return '"' + stringEscape(entityDecode(text)) + '"';
      }
    }
  },
  CJSX_ATTR_KEY: genericLeafSerialiser,
  CJSX_ATTR_VAL: genericLeafSerialiser
};

firstNonWhitespaceChild = function(children) {
  return find.call(children, function(child) {
    return child.type !== $.CJSX_WHITESPACE;
  });
};

containsNewlines = function(text) {
  return text.indexOf('\n') > -1;
};

joinList = function(items) {
  var i, output;
  output = items[items.length - 1];
  i = items.length - 2;
  while (i >= 0) {
    if (output.charAt(0) === '\n') {
      output = items[i] + ',' + output;
    } else {
      output = items[i] + ', ' + output;
    }
    i--;
  }
  return output;
};

SPACES_ONLY = /^\s+$/;

WHITESPACE_ONLY = /^[\n\s]+$/;

TEXT_LEADING_WHITESPACE = /^\s*?\n\s*/;

TEXT_TRAILING_WHITESPACE = /\s*?\n\s*?$/;

exports.Serialiser = Serialiser;

exports.nodeSerialisers = nodeSerialisers;

},{"./entitydecode":13,"./helpers":14,"./stringescape":17,"./symbols":18}],17:[function(require,module,exports){

var hex = '0123456789abcdef'.split('');

module.exports  =  function stringEncode(input, opts) {
  opts = opts || {};
  var escaped = "";
  
  for (var i = 0; i < input.length; i++) {
    escaped = escaped + encodeChar(input.charAt(i), opts.preserveNewlines);
  }
  
  return escaped;
}

function encodeChar(inputChar, preserveNewlines) {
  var character = inputChar.charAt(0);
  var characterCode = inputChar.charCodeAt(0);

  switch(character) {
    case '\n':
      if (!preserveNewlines) return "\\n";
      else return character;
    case '\r':
      if (!preserveNewlines) return "\\r";
      else return character;
    case '\'': return "\\'";
    case '"': return "\\\"";
    case '\&': return "\\&";
    case '\\': return "\\\\";
    case '\t': return "\\t";
    case '\b': return "\\b";
    case '\f': return "\\f";
    case '/': return "\\x2F";
    case '<': return "\\x3C";
    case '>': return "\\x3E";
  }

  if (characterCode > 127) {
    var c = characterCode;
    var a4 = c % 16;
    c = ~~(c/16); 
    var a3 = c % 16;
    c = ~~(c/16);
    var a2 = c % 16;
    c = ~~(c/16);
    var a1 = c % 16;
    
    return ["\\u", hex[a1], hex[a2], hex[a3], hex[a4]].join('');    
  } else {
    return inputChar;
  }
}

},{}],18:[function(require,module,exports){
// Generated by CoffeeScript 1.9.1
module.exports = {
  ROOT: 'ROOT',
  CJSX_EL: 'CJSX_EL',
  CJSX_ESC: 'CJSX_ESC',
  CJSX_ATTRIBUTES: 'CJSX_ATTRIBUTES',
  CJSX_ATTR_PAIR: 'CJSX_ATTR_PAIR',
  CS: 'CS',
  CS_COMMENT: 'CS_COMMENT',
  CS_HEREDOC: 'CS_HEREDOC',
  CS_STRING: 'CS_STRING',
  CS_REGEX: 'CS_REGEX',
  CS_HEREGEX: 'CS_HEREGEX',
  JS_ESC: 'JS_ESC',
  CJSX_WHITESPACE: 'CJSX_WHITESPACE',
  CJSX_TEXT: 'CJSX_TEXT',
  CJSX_ATTR_KEY: 'CJSX_ATTR_KEY',
  CJSX_ATTR_VAL: 'CJSX_ATTR_VAL',
  CJSX_ATTR_SPREAD: 'CJSX_ATTR_SPREAD',
  CJSX_START: 'CJSX_START',
  CJSX_END: 'CJSX_END',
  CJSX_COMMENT: 'CJSX_COMMENT',
  CJSX_ESC_START: 'CJSX_ESC_START',
  CJSX_ESC_END: 'CJSX_ESC_END',
  CJSX_PRAGMA: 'CJSX_PRAGMA'
};

},{}],19:[function(require,module,exports){
// Generated by CoffeeScript 1.9.1
var Parser, serialise;

Parser = require('./parser');

serialise = require('./serialiser');

module.exports.transform = function(code, opts) {
  return serialise(new Parser().parse(code, opts));
};

},{"./parser":15,"./serialiser":16}],20:[function(require,module,exports){
(function (process,global){
// Generated by CoffeeScript 1.9.3
(function() {
  var Lexer, SourceMap, base, compile, ext, formatSourcePosition, fs, getSourceMap, helpers, i, len, lexer, parser, path, ref, sourceMaps, vm, withPrettyErrors,
    hasProp = {}.hasOwnProperty,
    indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  fs = require('fs');

  vm = require('vm');

  path = require('path');

  Lexer = require('./lexer').Lexer;

  parser = require('./parser').parser;

  helpers = require('./helpers');

  SourceMap = require('./sourcemap');

  exports.VERSION = '1.9.3';

  exports.FILE_EXTENSIONS = ['.coffee', '.litcoffee', '.coffee.md'];

  exports.helpers = helpers;

  withPrettyErrors = function(fn) {
    return function(code, options) {
      var err;
      if (options == null) {
        options = {};
      }
      try {
        return fn.call(this, code, options);
      } catch (_error) {
        err = _error;
        if (typeof code !== 'string') {
          throw err;
        }
        throw helpers.updateSyntaxError(err, code, options.filename);
      }
    };
  };

  exports.compile = compile = withPrettyErrors(function(code, options) {
    var answer, currentColumn, currentLine, extend, fragment, fragments, header, i, js, len, map, merge, newLines, token, tokens;
    merge = helpers.merge, extend = helpers.extend;
    options = extend({}, options);
    if (options.sourceMap) {
      map = new SourceMap;
    }
    tokens = lexer.tokenize(code, options);
    options.referencedVars = (function() {
      var i, len, results;
      results = [];
      for (i = 0, len = tokens.length; i < len; i++) {
        token = tokens[i];
        if (token.variable) {
          results.push(token[1]);
        }
      }
      return results;
    })();
    fragments = parser.parse(tokens).compileToFragments(options);
    currentLine = 0;
    if (options.header) {
      currentLine += 1;
    }
    if (options.shiftLine) {
      currentLine += 1;
    }
    currentColumn = 0;
    js = "";
    for (i = 0, len = fragments.length; i < len; i++) {
      fragment = fragments[i];
      if (options.sourceMap) {
        if (fragment.locationData && !/^[;\s]*$/.test(fragment.code)) {
          map.add([fragment.locationData.first_line, fragment.locationData.first_column], [currentLine, currentColumn], {
            noReplace: true
          });
        }
        newLines = helpers.count(fragment.code, "\n");
        currentLine += newLines;
        if (newLines) {
          currentColumn = fragment.code.length - (fragment.code.lastIndexOf("\n") + 1);
        } else {
          currentColumn += fragment.code.length;
        }
      }
      js += fragment.code;
    }
    if (options.header) {
      header = "Generated by CoffeeScript " + this.VERSION;
      js = "// " + header + "\n" + js;
    }
    if (options.sourceMap) {
      answer = {
        js: js
      };
      answer.sourceMap = map;
      answer.v3SourceMap = map.generate(options, code);
      return answer;
    } else {
      return js;
    }
  });

  exports.tokens = withPrettyErrors(function(code, options) {
    return lexer.tokenize(code, options);
  });

  exports.nodes = withPrettyErrors(function(source, options) {
    if (typeof source === 'string') {
      return parser.parse(lexer.tokenize(source, options));
    } else {
      return parser.parse(source);
    }
  });

  exports.run = function(code, options) {
    var answer, dir, mainModule, ref;
    if (options == null) {
      options = {};
    }
    mainModule = require.main;
    mainModule.filename = process.argv[1] = options.filename ? fs.realpathSync(options.filename) : '.';
    mainModule.moduleCache && (mainModule.moduleCache = {});
    dir = options.filename ? path.dirname(fs.realpathSync(options.filename)) : fs.realpathSync('.');
    mainModule.paths = require('module')._nodeModulePaths(dir);
    if (!helpers.isCoffee(mainModule.filename) || require.extensions) {
      answer = compile(code, options);
      code = (ref = answer.js) != null ? ref : answer;
    }
    return mainModule._compile(code, mainModule.filename);
  };

  exports["eval"] = function(code, options) {
    var Module, _module, _require, createContext, i, isContext, js, k, len, o, r, ref, ref1, ref2, ref3, sandbox, v;
    if (options == null) {
      options = {};
    }
    if (!(code = code.trim())) {
      return;
    }
    createContext = (ref = vm.Script.createContext) != null ? ref : vm.createContext;
    isContext = (ref1 = vm.isContext) != null ? ref1 : function(ctx) {
      return options.sandbox instanceof createContext().constructor;
    };
    if (createContext) {
      if (options.sandbox != null) {
        if (isContext(options.sandbox)) {
          sandbox = options.sandbox;
        } else {
          sandbox = createContext();
          ref2 = options.sandbox;
          for (k in ref2) {
            if (!hasProp.call(ref2, k)) continue;
            v = ref2[k];
            sandbox[k] = v;
          }
        }
        sandbox.global = sandbox.root = sandbox.GLOBAL = sandbox;
      } else {
        sandbox = global;
      }
      sandbox.__filename = options.filename || 'eval';
      sandbox.__dirname = path.dirname(sandbox.__filename);
      if (!(sandbox !== global || sandbox.module || sandbox.require)) {
        Module = require('module');
        sandbox.module = _module = new Module(options.modulename || 'eval');
        sandbox.require = _require = function(path) {
          return Module._load(path, _module, true);
        };
        _module.filename = sandbox.__filename;
        ref3 = Object.getOwnPropertyNames(require);
        for (i = 0, len = ref3.length; i < len; i++) {
          r = ref3[i];
          if (r !== 'paths') {
            _require[r] = require[r];
          }
        }
        _require.paths = _module.paths = Module._nodeModulePaths(process.cwd());
        _require.resolve = function(request) {
          return Module._resolveFilename(request, _module);
        };
      }
    }
    o = {};
    for (k in options) {
      if (!hasProp.call(options, k)) continue;
      v = options[k];
      o[k] = v;
    }
    o.bare = true;
    js = compile(code, o);
    if (sandbox === global) {
      return vm.runInThisContext(js);
    } else {
      return vm.runInContext(js, sandbox);
    }
  };

  exports.register = function() {
    return require('./register');
  };

  if (require.extensions) {
    ref = this.FILE_EXTENSIONS;
    for (i = 0, len = ref.length; i < len; i++) {
      ext = ref[i];
      if ((base = require.extensions)[ext] == null) {
        base[ext] = function() {
          throw new Error("Use CoffeeScript.register() or require the coffee-script/register module to require " + ext + " files.");
        };
      }
    }
  }

  exports._compileFile = function(filename, sourceMap) {
    var answer, err, raw, stripped;
    if (sourceMap == null) {
      sourceMap = false;
    }
    raw = fs.readFileSync(filename, 'utf8');
    stripped = raw.charCodeAt(0) === 0xFEFF ? raw.substring(1) : raw;
    try {
      answer = compile(stripped, {
        filename: filename,
        sourceMap: sourceMap,
        literate: helpers.isLiterate(filename)
      });
    } catch (_error) {
      err = _error;
      throw helpers.updateSyntaxError(err, stripped, filename);
    }
    return answer;
  };

  lexer = new Lexer;

  parser.lexer = {
    lex: function() {
      var tag, token;
      token = parser.tokens[this.pos++];
      if (token) {
        tag = token[0], this.yytext = token[1], this.yylloc = token[2];
        parser.errorToken = token.origin || token;
        this.yylineno = this.yylloc.first_line;
      } else {
        tag = '';
      }
      return tag;
    },
    setInput: function(tokens) {
      parser.tokens = tokens;
      return this.pos = 0;
    },
    upcomingInput: function() {
      return "";
    }
  };

  parser.yy = require('./nodes');

  parser.yy.parseError = function(message, arg) {
    var errorLoc, errorTag, errorText, errorToken, token, tokens;
    token = arg.token;
    errorToken = parser.errorToken, tokens = parser.tokens;
    errorTag = errorToken[0], errorText = errorToken[1], errorLoc = errorToken[2];
    errorText = (function() {
      switch (false) {
        case errorToken !== tokens[tokens.length - 1]:
          return 'end of input';
        case errorTag !== 'INDENT' && errorTag !== 'OUTDENT':
          return 'indentation';
        case errorTag !== 'IDENTIFIER' && errorTag !== 'NUMBER' && errorTag !== 'STRING' && errorTag !== 'STRING_START' && errorTag !== 'REGEX' && errorTag !== 'REGEX_START':
          return errorTag.replace(/_START$/, '').toLowerCase();
        default:
          return helpers.nameWhitespaceCharacter(errorText);
      }
    })();
    return helpers.throwSyntaxError("unexpected " + errorText, errorLoc);
  };

  formatSourcePosition = function(frame, getSourceMapping) {
    var as, column, fileLocation, fileName, functionName, isConstructor, isMethodCall, line, methodName, source, tp, typeName;
    fileName = void 0;
    fileLocation = '';
    if (frame.isNative()) {
      fileLocation = "native";
    } else {
      if (frame.isEval()) {
        fileName = frame.getScriptNameOrSourceURL();
        if (!fileName) {
          fileLocation = (frame.getEvalOrigin()) + ", ";
        }
      } else {
        fileName = frame.getFileName();
      }
      fileName || (fileName = "<anonymous>");
      line = frame.getLineNumber();
      column = frame.getColumnNumber();
      source = getSourceMapping(fileName, line, column);
      fileLocation = source ? fileName + ":" + source[0] + ":" + source[1] : fileName + ":" + line + ":" + column;
    }
    functionName = frame.getFunctionName();
    isConstructor = frame.isConstructor();
    isMethodCall = !(frame.isToplevel() || isConstructor);
    if (isMethodCall) {
      methodName = frame.getMethodName();
      typeName = frame.getTypeName();
      if (functionName) {
        tp = as = '';
        if (typeName && functionName.indexOf(typeName)) {
          tp = typeName + ".";
        }
        if (methodName && functionName.indexOf("." + methodName) !== functionName.length - methodName.length - 1) {
          as = " [as " + methodName + "]";
        }
        return "" + tp + functionName + as + " (" + fileLocation + ")";
      } else {
        return typeName + "." + (methodName || '<anonymous>') + " (" + fileLocation + ")";
      }
    } else if (isConstructor) {
      return "new " + (functionName || '<anonymous>') + " (" + fileLocation + ")";
    } else if (functionName) {
      return functionName + " (" + fileLocation + ")";
    } else {
      return fileLocation;
    }
  };

  sourceMaps = {};

  getSourceMap = function(filename) {
    var answer, ref1;
    if (sourceMaps[filename]) {
      return sourceMaps[filename];
    }
    if (ref1 = path != null ? path.extname(filename) : void 0, indexOf.call(exports.FILE_EXTENSIONS, ref1) < 0) {
      return;
    }
    answer = exports._compileFile(filename, true);
    return sourceMaps[filename] = answer.sourceMap;
  };

  Error.prepareStackTrace = function(err, stack) {
    var frame, frames, getSourceMapping;
    getSourceMapping = function(filename, line, column) {
      var answer, sourceMap;
      sourceMap = getSourceMap(filename);
      if (sourceMap) {
        answer = sourceMap.sourceLocation([line - 1, column - 1]);
      }
      if (answer) {
        return [answer[0] + 1, answer[1] + 1];
      } else {
        return null;
      }
    };
    frames = (function() {
      var j, len1, results;
      results = [];
      for (j = 0, len1 = stack.length; j < len1; j++) {
        frame = stack[j];
        if (frame.getFunction() === exports.run) {
          break;
        }
        results.push("  at " + (formatSourcePosition(frame, getSourceMapping)));
      }
      return results;
    })();
    return (err.toString()) + "\n" + (frames.join('\n')) + "\n";
  };

}).call(this);

}).call(this,require('_process'),typeof global !== "undefined" ? global : typeof self !== "undefined" ? self : typeof window !== "undefined" ? window : {})
},{"./helpers":21,"./lexer":22,"./nodes":23,"./parser":24,"./register":25,"./sourcemap":28,"_process":8,"fs":2,"module":2,"path":7,"vm":9}],21:[function(require,module,exports){
(function (process){
// Generated by CoffeeScript 1.9.3
(function() {
  var buildLocationData, extend, flatten, ref, repeat, syntaxErrorToString;

  exports.starts = function(string, literal, start) {
    return literal === string.substr(start, literal.length);
  };

  exports.ends = function(string, literal, back) {
    var len;
    len = literal.length;
    return literal === string.substr(string.length - len - (back || 0), len);
  };

  exports.repeat = repeat = function(str, n) {
    var res;
    res = '';
    while (n > 0) {
      if (n & 1) {
        res += str;
      }
      n >>>= 1;
      str += str;
    }
    return res;
  };

  exports.compact = function(array) {
    var i, item, len1, results;
    results = [];
    for (i = 0, len1 = array.length; i < len1; i++) {
      item = array[i];
      if (item) {
        results.push(item);
      }
    }
    return results;
  };

  exports.count = function(string, substr) {
    var num, pos;
    num = pos = 0;
    if (!substr.length) {
      return 1 / 0;
    }
    while (pos = 1 + string.indexOf(substr, pos)) {
      num++;
    }
    return num;
  };

  exports.merge = function(options, overrides) {
    return extend(extend({}, options), overrides);
  };

  extend = exports.extend = function(object, properties) {
    var key, val;
    for (key in properties) {
      val = properties[key];
      object[key] = val;
    }
    return object;
  };

  exports.flatten = flatten = function(array) {
    var element, flattened, i, len1;
    flattened = [];
    for (i = 0, len1 = array.length; i < len1; i++) {
      element = array[i];
      if (element instanceof Array) {
        flattened = flattened.concat(flatten(element));
      } else {
        flattened.push(element);
      }
    }
    return flattened;
  };

  exports.del = function(obj, key) {
    var val;
    val = obj[key];
    delete obj[key];
    return val;
  };

  exports.some = (ref = Array.prototype.some) != null ? ref : function(fn) {
    var e, i, len1;
    for (i = 0, len1 = this.length; i < len1; i++) {
      e = this[i];
      if (fn(e)) {
        return true;
      }
    }
    return false;
  };

  exports.invertLiterate = function(code) {
    var line, lines, maybe_code;
    maybe_code = true;
    lines = (function() {
      var i, len1, ref1, results;
      ref1 = code.split('\n');
      results = [];
      for (i = 0, len1 = ref1.length; i < len1; i++) {
        line = ref1[i];
        if (maybe_code && /^([ ]{4}|[ ]{0,3}\t)/.test(line)) {
          results.push(line);
        } else if (maybe_code = /^\s*$/.test(line)) {
          results.push(line);
        } else {
          results.push('# ' + line);
        }
      }
      return results;
    })();
    return lines.join('\n');
  };

  buildLocationData = function(first, last) {
    if (!last) {
      return first;
    } else {
      return {
        first_line: first.first_line,
        first_column: first.first_column,
        last_line: last.last_line,
        last_column: last.last_column
      };
    }
  };

  exports.addLocationDataFn = function(first, last) {
    return function(obj) {
      if (((typeof obj) === 'object') && (!!obj['updateLocationDataIfMissing'])) {
        obj.updateLocationDataIfMissing(buildLocationData(first, last));
      }
      return obj;
    };
  };

  exports.locationDataToString = function(obj) {
    var locationData;
    if (("2" in obj) && ("first_line" in obj[2])) {
      locationData = obj[2];
    } else if ("first_line" in obj) {
      locationData = obj;
    }
    if (locationData) {
      return ((locationData.first_line + 1) + ":" + (locationData.first_column + 1) + "-") + ((locationData.last_line + 1) + ":" + (locationData.last_column + 1));
    } else {
      return "No location data";
    }
  };

  exports.baseFileName = function(file, stripExt, useWinPathSep) {
    var parts, pathSep;
    if (stripExt == null) {
      stripExt = false;
    }
    if (useWinPathSep == null) {
      useWinPathSep = false;
    }
    pathSep = useWinPathSep ? /\\|\// : /\//;
    parts = file.split(pathSep);
    file = parts[parts.length - 1];
    if (!(stripExt && file.indexOf('.') >= 0)) {
      return file;
    }
    parts = file.split('.');
    parts.pop();
    if (parts[parts.length - 1] === 'coffee' && parts.length > 1) {
      parts.pop();
    }
    return parts.join('.');
  };

  exports.isCoffee = function(file) {
    return /\.((lit)?coffee|coffee\.md)$/.test(file);
  };

  exports.isLiterate = function(file) {
    return /\.(litcoffee|coffee\.md)$/.test(file);
  };

  exports.throwSyntaxError = function(message, location) {
    var error;
    error = new SyntaxError(message);
    error.location = location;
    error.toString = syntaxErrorToString;
    error.stack = error.toString();
    throw error;
  };

  exports.updateSyntaxError = function(error, code, filename) {
    if (error.toString === syntaxErrorToString) {
      error.code || (error.code = code);
      error.filename || (error.filename = filename);
      error.stack = error.toString();
    }
    return error;
  };

  syntaxErrorToString = function() {
    var codeLine, colorize, colorsEnabled, end, filename, first_column, first_line, last_column, last_line, marker, ref1, ref2, ref3, ref4, start;
    if (!(this.code && this.location)) {
      return Error.prototype.toString.call(this);
    }
    ref1 = this.location, first_line = ref1.first_line, first_column = ref1.first_column, last_line = ref1.last_line, last_column = ref1.last_column;
    if (last_line == null) {
      last_line = first_line;
    }
    if (last_column == null) {
      last_column = first_column;
    }
    filename = this.filename || '[stdin]';
    codeLine = this.code.split('\n')[first_line];
    start = first_column;
    end = first_line === last_line ? last_column + 1 : codeLine.length;
    marker = codeLine.slice(0, start).replace(/[^\s]/g, ' ') + repeat('^', end - start);
    if (typeof process !== "undefined" && process !== null) {
      colorsEnabled = ((ref2 = process.stdout) != null ? ref2.isTTY : void 0) && !((ref3 = process.env) != null ? ref3.NODE_DISABLE_COLORS : void 0);
    }
    if ((ref4 = this.colorful) != null ? ref4 : colorsEnabled) {
      colorize = function(str) {
        return "\x1B[1;31m" + str + "\x1B[0m";
      };
      codeLine = codeLine.slice(0, start) + colorize(codeLine.slice(start, end)) + codeLine.slice(end);
      marker = colorize(marker);
    }
    return filename + ":" + (first_line + 1) + ":" + (first_column + 1) + ": error: " + this.message + "\n" + codeLine + "\n" + marker;
  };

  exports.nameWhitespaceCharacter = function(string) {
    switch (string) {
      case ' ':
        return 'space';
      case '\n':
        return 'newline';
      case '\r':
        return 'carriage return';
      case '\t':
        return 'tab';
      default:
        return string;
    }
  };

}).call(this);

}).call(this,require('_process'))
},{"_process":8}],22:[function(require,module,exports){
// Generated by CoffeeScript 1.9.3
(function() {
  var BOM, BOOL, CALLABLE, CODE, COFFEE_ALIASES, COFFEE_ALIAS_MAP, COFFEE_KEYWORDS, COMMENT, COMPARE, COMPOUND_ASSIGN, HERECOMMENT_ILLEGAL, HEREDOC_DOUBLE, HEREDOC_INDENT, HEREDOC_SINGLE, HEREGEX, HEREGEX_OMIT, IDENTIFIER, INDENTABLE_CLOSERS, INDEXABLE, INVALID_ESCAPE, INVERSES, JSTOKEN, JS_FORBIDDEN, JS_KEYWORDS, LEADING_BLANK_LINE, LINE_BREAK, LINE_CONTINUER, LOGIC, Lexer, MATH, MULTI_DENT, NOT_REGEX, NUMBER, OPERATOR, POSSIBLY_DIVISION, REGEX, REGEX_FLAGS, REGEX_ILLEGAL, RELATION, RESERVED, Rewriter, SHIFT, SIMPLE_STRING_OMIT, STRICT_PROSCRIBED, STRING_DOUBLE, STRING_OMIT, STRING_SINGLE, STRING_START, TRAILING_BLANK_LINE, TRAILING_SPACES, UNARY, UNARY_MATH, VALID_FLAGS, WHITESPACE, compact, count, invertLiterate, key, locationDataToString, ref, ref1, repeat, starts, throwSyntaxError,
    indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  ref = require('./rewriter'), Rewriter = ref.Rewriter, INVERSES = ref.INVERSES;

  ref1 = require('./helpers'), count = ref1.count, starts = ref1.starts, compact = ref1.compact, repeat = ref1.repeat, invertLiterate = ref1.invertLiterate, locationDataToString = ref1.locationDataToString, throwSyntaxError = ref1.throwSyntaxError;

  exports.Lexer = Lexer = (function() {
    function Lexer() {}

    Lexer.prototype.tokenize = function(code, opts) {
      var consumed, end, i, ref2;
      if (opts == null) {
        opts = {};
      }
      this.literate = opts.literate;
      this.indent = 0;
      this.baseIndent = 0;
      this.indebt = 0;
      this.outdebt = 0;
      this.indents = [];
      this.ends = [];
      this.tokens = [];
      this.chunkLine = opts.line || 0;
      this.chunkColumn = opts.column || 0;
      code = this.clean(code);
      i = 0;
      while (this.chunk = code.slice(i)) {
        consumed = this.identifierToken() || this.commentToken() || this.whitespaceToken() || this.lineToken() || this.stringToken() || this.numberToken() || this.regexToken() || this.jsToken() || this.literalToken();
        ref2 = this.getLineAndColumnFromChunk(consumed), this.chunkLine = ref2[0], this.chunkColumn = ref2[1];
        i += consumed;
        if (opts.untilBalanced && this.ends.length === 0) {
          return {
            tokens: this.tokens,
            index: i
          };
        }
      }
      this.closeIndentation();
      if (end = this.ends.pop()) {
        this.error("missing " + end.tag, end.origin[2]);
      }
      if (opts.rewrite === false) {
        return this.tokens;
      }
      return (new Rewriter).rewrite(this.tokens);
    };

    Lexer.prototype.clean = function(code) {
      if (code.charCodeAt(0) === BOM) {
        code = code.slice(1);
      }
      code = code.replace(/\r/g, '').replace(TRAILING_SPACES, '');
      if (WHITESPACE.test(code)) {
        code = "\n" + code;
        this.chunkLine--;
      }
      if (this.literate) {
        code = invertLiterate(code);
      }
      return code;
    };

    Lexer.prototype.identifierToken = function() {
      var alias, colon, colonOffset, forcedIdentifier, id, idLength, input, match, poppedToken, prev, ref2, ref3, ref4, ref5, tag, tagToken;
      if (!(match = IDENTIFIER.exec(this.chunk))) {
        return 0;
      }
      input = match[0], id = match[1], colon = match[2];
      idLength = id.length;
      poppedToken = void 0;
      if (id === 'own' && this.tag() === 'FOR') {
        this.token('OWN', id);
        return id.length;
      }
      if (id === 'from' && this.tag() === 'YIELD') {
        this.token('FROM', id);
        return id.length;
      }
      ref2 = this.tokens, prev = ref2[ref2.length - 1];
      forcedIdentifier = colon || (prev != null) && (((ref3 = prev[0]) === '.' || ref3 === '?.' || ref3 === '::' || ref3 === '?::') || !prev.spaced && prev[0] === '@');
      tag = 'IDENTIFIER';
      if (!forcedIdentifier && (indexOf.call(JS_KEYWORDS, id) >= 0 || indexOf.call(COFFEE_KEYWORDS, id) >= 0)) {
        tag = id.toUpperCase();
        if (tag === 'WHEN' && (ref4 = this.tag(), indexOf.call(LINE_BREAK, ref4) >= 0)) {
          tag = 'LEADING_WHEN';
        } else if (tag === 'FOR') {
          this.seenFor = true;
        } else if (tag === 'UNLESS') {
          tag = 'IF';
        } else if (indexOf.call(UNARY, tag) >= 0) {
          tag = 'UNARY';
        } else if (indexOf.call(RELATION, tag) >= 0) {
          if (tag !== 'INSTANCEOF' && this.seenFor) {
            tag = 'FOR' + tag;
            this.seenFor = false;
          } else {
            tag = 'RELATION';
            if (this.value() === '!') {
              poppedToken = this.tokens.pop();
              id = '!' + id;
            }
          }
        }
      }
      if (indexOf.call(JS_FORBIDDEN, id) >= 0) {
        if (forcedIdentifier) {
          tag = 'IDENTIFIER';
          id = new String(id);
          id.reserved = true;
        } else if (indexOf.call(RESERVED, id) >= 0) {
          this.error("reserved word '" + id + "'", {
            length: id.length
          });
        }
      }
      if (!forcedIdentifier) {
        if (indexOf.call(COFFEE_ALIASES, id) >= 0) {
          alias = id;
          id = COFFEE_ALIAS_MAP[id];
        }
        tag = (function() {
          switch (id) {
            case '!':
              return 'UNARY';
            case '==':
            case '!=':
              return 'COMPARE';
            case '&&':
            case '||':
              return 'LOGIC';
            case 'true':
            case 'false':
              return 'BOOL';
            case 'break':
            case 'continue':
              return 'STATEMENT';
            default:
              return tag;
          }
        })();
      }
      tagToken = this.token(tag, id, 0, idLength);
      if (alias) {
        tagToken.origin = [tag, alias, tagToken[2]];
      }
      tagToken.variable = !forcedIdentifier;
      if (poppedToken) {
        ref5 = [poppedToken[2].first_line, poppedToken[2].first_column], tagToken[2].first_line = ref5[0], tagToken[2].first_column = ref5[1];
      }
      if (colon) {
        colonOffset = input.lastIndexOf(':');
        this.token(':', ':', colonOffset, colon.length);
      }
      return input.length;
    };

    Lexer.prototype.numberToken = function() {
      var binaryLiteral, lexedLength, match, number, octalLiteral;
      if (!(match = NUMBER.exec(this.chunk))) {
        return 0;
      }
      number = match[0];
      lexedLength = number.length;
      if (/^0[BOX]/.test(number)) {
        this.error("radix prefix in '" + number + "' must be lowercase", {
          offset: 1
        });
      } else if (/E/.test(number) && !/^0x/.test(number)) {
        this.error("exponential notation in '" + number + "' must be indicated with a lowercase 'e'", {
          offset: number.indexOf('E')
        });
      } else if (/^0\d*[89]/.test(number)) {
        this.error("decimal literal '" + number + "' must not be prefixed with '0'", {
          length: lexedLength
        });
      } else if (/^0\d+/.test(number)) {
        this.error("octal literal '" + number + "' must be prefixed with '0o'", {
          length: lexedLength
        });
      }
      if (octalLiteral = /^0o([0-7]+)/.exec(number)) {
        number = '0x' + parseInt(octalLiteral[1], 8).toString(16);
      }
      if (binaryLiteral = /^0b([01]+)/.exec(number)) {
        number = '0x' + parseInt(binaryLiteral[1], 2).toString(16);
      }
      this.token('NUMBER', number, 0, lexedLength);
      return lexedLength;
    };

    Lexer.prototype.stringToken = function() {
      var $, attempt, delimiter, doc, end, heredoc, i, indent, indentRegex, match, quote, ref2, ref3, regex, token, tokens;
      quote = (STRING_START.exec(this.chunk) || [])[0];
      if (!quote) {
        return 0;
      }
      regex = (function() {
        switch (quote) {
          case "'":
            return STRING_SINGLE;
          case '"':
            return STRING_DOUBLE;
          case "'''":
            return HEREDOC_SINGLE;
          case '"""':
            return HEREDOC_DOUBLE;
        }
      })();
      heredoc = quote.length === 3;
      ref2 = this.matchWithInterpolations(regex, quote), tokens = ref2.tokens, end = ref2.index;
      $ = tokens.length - 1;
      delimiter = quote.charAt(0);
      if (heredoc) {
        indent = null;
        doc = ((function() {
          var j, len, results;
          results = [];
          for (i = j = 0, len = tokens.length; j < len; i = ++j) {
            token = tokens[i];
            if (token[0] === 'NEOSTRING') {
              results.push(token[1]);
            }
          }
          return results;
        })()).join('#{}');
        while (match = HEREDOC_INDENT.exec(doc)) {
          attempt = match[1];
          if (indent === null || (0 < (ref3 = attempt.length) && ref3 < indent.length)) {
            indent = attempt;
          }
        }
        if (indent) {
          indentRegex = RegExp("^" + indent, "gm");
        }
        this.mergeInterpolationTokens(tokens, {
          delimiter: delimiter
        }, (function(_this) {
          return function(value, i) {
            value = _this.formatString(value);
            if (i === 0) {
              value = value.replace(LEADING_BLANK_LINE, '');
            }
            if (i === $) {
              value = value.replace(TRAILING_BLANK_LINE, '');
            }
            if (indentRegex) {
              value = value.replace(indentRegex, '');
            }
            return value;
          };
        })(this));
      } else {
        this.mergeInterpolationTokens(tokens, {
          delimiter: delimiter
        }, (function(_this) {
          return function(value, i) {
            value = _this.formatString(value);
            value = value.replace(SIMPLE_STRING_OMIT, function(match, offset) {
              if ((i === 0 && offset === 0) || (i === $ && offset + match.length === value.length)) {
                return '';
              } else {
                return ' ';
              }
            });
            return value;
          };
        })(this));
      }
      return end;
    };

    Lexer.prototype.commentToken = function() {
      var comment, here, match;
      if (!(match = this.chunk.match(COMMENT))) {
        return 0;
      }
      comment = match[0], here = match[1];
      if (here) {
        if (match = HERECOMMENT_ILLEGAL.exec(comment)) {
          this.error("block comments cannot contain " + match[0], {
            offset: match.index,
            length: match[0].length
          });
        }
        if (here.indexOf('\n') >= 0) {
          here = here.replace(RegExp("\\n" + (repeat(' ', this.indent)), "g"), '\n');
        }
        this.token('HERECOMMENT', here, 0, comment.length);
      }
      return comment.length;
    };

    Lexer.prototype.jsToken = function() {
      var match, script;
      if (!(this.chunk.charAt(0) === '`' && (match = JSTOKEN.exec(this.chunk)))) {
        return 0;
      }
      this.token('JS', (script = match[0]).slice(1, -1), 0, script.length);
      return script.length;
    };

    Lexer.prototype.regexToken = function() {
      var body, closed, end, flags, index, match, origin, prev, ref2, ref3, ref4, regex, tokens;
      switch (false) {
        case !(match = REGEX_ILLEGAL.exec(this.chunk)):
          this.error("regular expressions cannot begin with " + match[2], {
            offset: match.index + match[1].length
          });
          break;
        case !(match = this.matchWithInterpolations(HEREGEX, '///')):
          tokens = match.tokens, index = match.index;
          break;
        case !(match = REGEX.exec(this.chunk)):
          regex = match[0], body = match[1], closed = match[2];
          this.validateEscapes(body, {
            isRegex: true,
            offsetInChunk: 1
          });
          index = regex.length;
          ref2 = this.tokens, prev = ref2[ref2.length - 1];
          if (prev) {
            if (prev.spaced && (ref3 = prev[0], indexOf.call(CALLABLE, ref3) >= 0)) {
              if (!closed || POSSIBLY_DIVISION.test(regex)) {
                return 0;
              }
            } else if (ref4 = prev[0], indexOf.call(NOT_REGEX, ref4) >= 0) {
              return 0;
            }
          }
          if (!closed) {
            this.error('missing / (unclosed regex)');
          }
          break;
        default:
          return 0;
      }
      flags = REGEX_FLAGS.exec(this.chunk.slice(index))[0];
      end = index + flags.length;
      origin = this.makeToken('REGEX', null, 0, end);
      switch (false) {
        case !!VALID_FLAGS.test(flags):
          this.error("invalid regular expression flags " + flags, {
            offset: index,
            length: flags.length
          });
          break;
        case !(regex || tokens.length === 1):
          if (body == null) {
            body = this.formatHeregex(tokens[0][1]);
          }
          this.token('REGEX', "" + (this.makeDelimitedLiteral(body, {
            delimiter: '/'
          })) + flags, 0, end, origin);
          break;
        default:
          this.token('REGEX_START', '(', 0, 0, origin);
          this.token('IDENTIFIER', 'RegExp', 0, 0);
          this.token('CALL_START', '(', 0, 0);
          this.mergeInterpolationTokens(tokens, {
            delimiter: '"',
            double: true
          }, this.formatHeregex);
          if (flags) {
            this.token(',', ',', index, 0);
            this.token('STRING', '"' + flags + '"', index, flags.length);
          }
          this.token(')', ')', end, 0);
          this.token('REGEX_END', ')', end, 0);
      }
      return end;
    };

    Lexer.prototype.lineToken = function() {
      var diff, indent, match, noNewlines, size;
      if (!(match = MULTI_DENT.exec(this.chunk))) {
        return 0;
      }
      indent = match[0];
      this.seenFor = false;
      size = indent.length - 1 - indent.lastIndexOf('\n');
      noNewlines = this.unfinished();
      if (size - this.indebt === this.indent) {
        if (noNewlines) {
          this.suppressNewlines();
        } else {
          this.newlineToken(0);
        }
        return indent.length;
      }
      if (size > this.indent) {
        if (noNewlines) {
          this.indebt = size - this.indent;
          this.suppressNewlines();
          return indent.length;
        }
        if (!this.tokens.length) {
          this.baseIndent = this.indent = size;
          return indent.length;
        }
        diff = size - this.indent + this.outdebt;
        this.token('INDENT', diff, indent.length - size, size);
        this.indents.push(diff);
        this.ends.push({
          tag: 'OUTDENT'
        });
        this.outdebt = this.indebt = 0;
        this.indent = size;
      } else if (size < this.baseIndent) {
        this.error('missing indentation', {
          offset: indent.length
        });
      } else {
        this.indebt = 0;
        this.outdentToken(this.indent - size, noNewlines, indent.length);
      }
      return indent.length;
    };

    Lexer.prototype.outdentToken = function(moveOut, noNewlines, outdentLength) {
      var decreasedIndent, dent, lastIndent, ref2;
      decreasedIndent = this.indent - moveOut;
      while (moveOut > 0) {
        lastIndent = this.indents[this.indents.length - 1];
        if (!lastIndent) {
          moveOut = 0;
        } else if (lastIndent === this.outdebt) {
          moveOut -= this.outdebt;
          this.outdebt = 0;
        } else if (lastIndent < this.outdebt) {
          this.outdebt -= lastIndent;
          moveOut -= lastIndent;
        } else {
          dent = this.indents.pop() + this.outdebt;
          if (outdentLength && (ref2 = this.chunk[outdentLength], indexOf.call(INDENTABLE_CLOSERS, ref2) >= 0)) {
            decreasedIndent -= dent - moveOut;
            moveOut = dent;
          }
          this.outdebt = 0;
          this.pair('OUTDENT');
          this.token('OUTDENT', moveOut, 0, outdentLength);
          moveOut -= dent;
        }
      }
      if (dent) {
        this.outdebt -= moveOut;
      }
      while (this.value() === ';') {
        this.tokens.pop();
      }
      if (!(this.tag() === 'TERMINATOR' || noNewlines)) {
        this.token('TERMINATOR', '\n', outdentLength, 0);
      }
      this.indent = decreasedIndent;
      return this;
    };

    Lexer.prototype.whitespaceToken = function() {
      var match, nline, prev, ref2;
      if (!((match = WHITESPACE.exec(this.chunk)) || (nline = this.chunk.charAt(0) === '\n'))) {
        return 0;
      }
      ref2 = this.tokens, prev = ref2[ref2.length - 1];
      if (prev) {
        prev[match ? 'spaced' : 'newLine'] = true;
      }
      if (match) {
        return match[0].length;
      } else {
        return 0;
      }
    };

    Lexer.prototype.newlineToken = function(offset) {
      while (this.value() === ';') {
        this.tokens.pop();
      }
      if (this.tag() !== 'TERMINATOR') {
        this.token('TERMINATOR', '\n', offset, 0);
      }
      return this;
    };

    Lexer.prototype.suppressNewlines = function() {
      if (this.value() === '\\') {
        this.tokens.pop();
      }
      return this;
    };

    Lexer.prototype.literalToken = function() {
      var match, prev, ref2, ref3, ref4, ref5, ref6, tag, token, value;
      if (match = OPERATOR.exec(this.chunk)) {
        value = match[0];
        if (CODE.test(value)) {
          this.tagParameters();
        }
      } else {
        value = this.chunk.charAt(0);
      }
      tag = value;
      ref2 = this.tokens, prev = ref2[ref2.length - 1];
      if (value === '=' && prev) {
        if (!prev[1].reserved && (ref3 = prev[1], indexOf.call(JS_FORBIDDEN, ref3) >= 0)) {
          if (prev.origin) {
            prev = prev.origin;
          }
          this.error("reserved word '" + prev[1] + "' can't be assigned", prev[2]);
        }
        if ((ref4 = prev[1]) === '||' || ref4 === '&&') {
          prev[0] = 'COMPOUND_ASSIGN';
          prev[1] += '=';
          return value.length;
        }
      }
      if (value === ';') {
        this.seenFor = false;
        tag = 'TERMINATOR';
      } else if (indexOf.call(MATH, value) >= 0) {
        tag = 'MATH';
      } else if (indexOf.call(COMPARE, value) >= 0) {
        tag = 'COMPARE';
      } else if (indexOf.call(COMPOUND_ASSIGN, value) >= 0) {
        tag = 'COMPOUND_ASSIGN';
      } else if (indexOf.call(UNARY, value) >= 0) {
        tag = 'UNARY';
      } else if (indexOf.call(UNARY_MATH, value) >= 0) {
        tag = 'UNARY_MATH';
      } else if (indexOf.call(SHIFT, value) >= 0) {
        tag = 'SHIFT';
      } else if (indexOf.call(LOGIC, value) >= 0 || value === '?' && (prev != null ? prev.spaced : void 0)) {
        tag = 'LOGIC';
      } else if (prev && !prev.spaced) {
        if (value === '(' && (ref5 = prev[0], indexOf.call(CALLABLE, ref5) >= 0)) {
          if (prev[0] === '?') {
            prev[0] = 'FUNC_EXIST';
          }
          tag = 'CALL_START';
        } else if (value === '[' && (ref6 = prev[0], indexOf.call(INDEXABLE, ref6) >= 0)) {
          tag = 'INDEX_START';
          switch (prev[0]) {
            case '?':
              prev[0] = 'INDEX_SOAK';
          }
        }
      }
      token = this.makeToken(tag, value);
      switch (value) {
        case '(':
        case '{':
        case '[':
          this.ends.push({
            tag: INVERSES[value],
            origin: token
          });
          break;
        case ')':
        case '}':
        case ']':
          this.pair(value);
      }
      this.tokens.push(token);
      return value.length;
    };

    Lexer.prototype.tagParameters = function() {
      var i, stack, tok, tokens;
      if (this.tag() !== ')') {
        return this;
      }
      stack = [];
      tokens = this.tokens;
      i = tokens.length;
      tokens[--i][0] = 'PARAM_END';
      while (tok = tokens[--i]) {
        switch (tok[0]) {
          case ')':
            stack.push(tok);
            break;
          case '(':
          case 'CALL_START':
            if (stack.length) {
              stack.pop();
            } else if (tok[0] === '(') {
              tok[0] = 'PARAM_START';
              return this;
            } else {
              return this;
            }
        }
      }
      return this;
    };

    Lexer.prototype.closeIndentation = function() {
      return this.outdentToken(this.indent);
    };

    Lexer.prototype.matchWithInterpolations = function(regex, delimiter) {
      var close, column, firstToken, index, lastToken, line, nested, offsetInChunk, open, ref2, ref3, ref4, str, strPart, tokens;
      tokens = [];
      offsetInChunk = delimiter.length;
      if (this.chunk.slice(0, offsetInChunk) !== delimiter) {
        return null;
      }
      str = this.chunk.slice(offsetInChunk);
      while (true) {
        strPart = regex.exec(str)[0];
        this.validateEscapes(strPart, {
          isRegex: delimiter.charAt(0) === '/',
          offsetInChunk: offsetInChunk
        });
        tokens.push(this.makeToken('NEOSTRING', strPart, offsetInChunk));
        str = str.slice(strPart.length);
        offsetInChunk += strPart.length;
        if (str.slice(0, 2) !== '#{') {
          break;
        }
        ref2 = this.getLineAndColumnFromChunk(offsetInChunk + 1), line = ref2[0], column = ref2[1];
        ref3 = new Lexer().tokenize(str.slice(1), {
          line: line,
          column: column,
          untilBalanced: true
        }), nested = ref3.tokens, index = ref3.index;
        index += 1;
        open = nested[0], close = nested[nested.length - 1];
        open[0] = open[1] = '(';
        close[0] = close[1] = ')';
        close.origin = ['', 'end of interpolation', close[2]];
        if (((ref4 = nested[1]) != null ? ref4[0] : void 0) === 'TERMINATOR') {
          nested.splice(1, 1);
        }
        tokens.push(['TOKENS', nested]);
        str = str.slice(index);
        offsetInChunk += index;
      }
      if (str.slice(0, delimiter.length) !== delimiter) {
        this.error("missing " + delimiter, {
          length: delimiter.length
        });
      }
      firstToken = tokens[0], lastToken = tokens[tokens.length - 1];
      firstToken[2].first_column -= delimiter.length;
      lastToken[2].last_column += delimiter.length;
      if (lastToken[1].length === 0) {
        lastToken[2].last_column -= 1;
      }
      return {
        tokens: tokens,
        index: offsetInChunk + delimiter.length
      };
    };

    Lexer.prototype.mergeInterpolationTokens = function(tokens, options, fn) {
      var converted, firstEmptyStringIndex, firstIndex, i, j, lastToken, len, locationToken, lparen, plusToken, ref2, rparen, tag, token, tokensToPush, value;
      if (tokens.length > 1) {
        lparen = this.token('STRING_START', '(', 0, 0);
      }
      firstIndex = this.tokens.length;
      for (i = j = 0, len = tokens.length; j < len; i = ++j) {
        token = tokens[i];
        tag = token[0], value = token[1];
        switch (tag) {
          case 'TOKENS':
            if (value.length === 2) {
              continue;
            }
            locationToken = value[0];
            tokensToPush = value;
            break;
          case 'NEOSTRING':
            converted = fn(token[1], i);
            if (converted.length === 0) {
              if (i === 0) {
                firstEmptyStringIndex = this.tokens.length;
              } else {
                continue;
              }
            }
            if (i === 2 && (firstEmptyStringIndex != null)) {
              this.tokens.splice(firstEmptyStringIndex, 2);
            }
            token[0] = 'STRING';
            token[1] = this.makeDelimitedLiteral(converted, options);
            locationToken = token;
            tokensToPush = [token];
        }
        if (this.tokens.length > firstIndex) {
          plusToken = this.token('+', '+');
          plusToken[2] = {
            first_line: locationToken[2].first_line,
            first_column: locationToken[2].first_column,
            last_line: locationToken[2].first_line,
            last_column: locationToken[2].first_column
          };
        }
        (ref2 = this.tokens).push.apply(ref2, tokensToPush);
      }
      if (lparen) {
        lastToken = tokens[tokens.length - 1];
        lparen.origin = [
          'STRING', null, {
            first_line: lparen[2].first_line,
            first_column: lparen[2].first_column,
            last_line: lastToken[2].last_line,
            last_column: lastToken[2].last_column
          }
        ];
        rparen = this.token('STRING_END', ')');
        return rparen[2] = {
          first_line: lastToken[2].last_line,
          first_column: lastToken[2].last_column,
          last_line: lastToken[2].last_line,
          last_column: lastToken[2].last_column
        };
      }
    };

    Lexer.prototype.pair = function(tag) {
      var lastIndent, prev, ref2, ref3, wanted;
      ref2 = this.ends, prev = ref2[ref2.length - 1];
      if (tag !== (wanted = prev != null ? prev.tag : void 0)) {
        if ('OUTDENT' !== wanted) {
          this.error("unmatched " + tag);
        }
        ref3 = this.indents, lastIndent = ref3[ref3.length - 1];
        this.outdentToken(lastIndent, true);
        return this.pair(tag);
      }
      return this.ends.pop();
    };

    Lexer.prototype.getLineAndColumnFromChunk = function(offset) {
      var column, lastLine, lineCount, ref2, string;
      if (offset === 0) {
        return [this.chunkLine, this.chunkColumn];
      }
      if (offset >= this.chunk.length) {
        string = this.chunk;
      } else {
        string = this.chunk.slice(0, +(offset - 1) + 1 || 9e9);
      }
      lineCount = count(string, '\n');
      column = this.chunkColumn;
      if (lineCount > 0) {
        ref2 = string.split('\n'), lastLine = ref2[ref2.length - 1];
        column = lastLine.length;
      } else {
        column += string.length;
      }
      return [this.chunkLine + lineCount, column];
    };

    Lexer.prototype.makeToken = function(tag, value, offsetInChunk, length) {
      var lastCharacter, locationData, ref2, ref3, token;
      if (offsetInChunk == null) {
        offsetInChunk = 0;
      }
      if (length == null) {
        length = value.length;
      }
      locationData = {};
      ref2 = this.getLineAndColumnFromChunk(offsetInChunk), locationData.first_line = ref2[0], locationData.first_column = ref2[1];
      lastCharacter = Math.max(0, length - 1);
      ref3 = this.getLineAndColumnFromChunk(offsetInChunk + lastCharacter), locationData.last_line = ref3[0], locationData.last_column = ref3[1];
      token = [tag, value, locationData];
      return token;
    };

    Lexer.prototype.token = function(tag, value, offsetInChunk, length, origin) {
      var token;
      token = this.makeToken(tag, value, offsetInChunk, length);
      if (origin) {
        token.origin = origin;
      }
      this.tokens.push(token);
      return token;
    };

    Lexer.prototype.tag = function() {
      var ref2, token;
      ref2 = this.tokens, token = ref2[ref2.length - 1];
      return token != null ? token[0] : void 0;
    };

    Lexer.prototype.value = function() {
      var ref2, token;
      ref2 = this.tokens, token = ref2[ref2.length - 1];
      return token != null ? token[1] : void 0;
    };

    Lexer.prototype.unfinished = function() {
      var ref2;
      return LINE_CONTINUER.test(this.chunk) || ((ref2 = this.tag()) === '\\' || ref2 === '.' || ref2 === '?.' || ref2 === '?::' || ref2 === 'UNARY' || ref2 === 'MATH' || ref2 === 'UNARY_MATH' || ref2 === '+' || ref2 === '-' || ref2 === 'YIELD' || ref2 === '**' || ref2 === 'SHIFT' || ref2 === 'RELATION' || ref2 === 'COMPARE' || ref2 === 'LOGIC' || ref2 === 'THROW' || ref2 === 'EXTENDS');
    };

    Lexer.prototype.formatString = function(str) {
      return str.replace(STRING_OMIT, '$1');
    };

    Lexer.prototype.formatHeregex = function(str) {
      return str.replace(HEREGEX_OMIT, '$1$2');
    };

    Lexer.prototype.validateEscapes = function(str, options) {
      var before, hex, invalidEscape, match, message, octal, ref2, unicode;
      if (options == null) {
        options = {};
      }
      match = INVALID_ESCAPE.exec(str);
      if (!match) {
        return;
      }
      match[0], before = match[1], octal = match[2], hex = match[3], unicode = match[4];
      if (options.isRegex && octal && octal.charAt(0) !== '0') {
        return;
      }
      message = octal ? "octal escape sequences are not allowed" : "invalid escape sequence";
      invalidEscape = "\\" + (octal || hex || unicode);
      return this.error(message + " " + invalidEscape, {
        offset: ((ref2 = options.offsetInChunk) != null ? ref2 : 0) + match.index + before.length,
        length: invalidEscape.length
      });
    };

    Lexer.prototype.makeDelimitedLiteral = function(body, options) {
      var regex;
      if (options == null) {
        options = {};
      }
      if (body === '' && options.delimiter === '/') {
        body = '(?:)';
      }
      regex = RegExp("(\\\\\\\\)|(\\\\0(?=[1-7]))|\\\\?(" + options.delimiter + ")|\\\\?(?:(\\n)|(\\r)|(\\u2028)|(\\u2029))|(\\\\.)", "g");
      body = body.replace(regex, function(match, backslash, nul, delimiter, lf, cr, ls, ps, other) {
        switch (false) {
          case !backslash:
            if (options.double) {
              return backslash + backslash;
            } else {
              return backslash;
            }
          case !nul:
            return '\\x00';
          case !delimiter:
            return "\\" + delimiter;
          case !lf:
            return '\\n';
          case !cr:
            return '\\r';
          case !ls:
            return '\\u2028';
          case !ps:
            return '\\u2029';
          case !other:
            if (options.double) {
              return "\\" + other;
            } else {
              return other;
            }
        }
      });
      return "" + options.delimiter + body + options.delimiter;
    };

    Lexer.prototype.error = function(message, options) {
      var first_column, first_line, location, ref2, ref3, ref4;
      if (options == null) {
        options = {};
      }
      location = 'first_line' in options ? options : ((ref3 = this.getLineAndColumnFromChunk((ref2 = options.offset) != null ? ref2 : 0), first_line = ref3[0], first_column = ref3[1], ref3), {
        first_line: first_line,
        first_column: first_column,
        last_column: first_column + ((ref4 = options.length) != null ? ref4 : 1) - 1
      });
      return throwSyntaxError(message, location);
    };

    return Lexer;

  })();

  JS_KEYWORDS = ['true', 'false', 'null', 'this', 'new', 'delete', 'typeof', 'in', 'instanceof', 'return', 'throw', 'break', 'continue', 'debugger', 'yield', 'if', 'else', 'switch', 'for', 'while', 'do', 'try', 'catch', 'finally', 'class', 'extends', 'super'];

  COFFEE_KEYWORDS = ['undefined', 'then', 'unless', 'until', 'loop', 'of', 'by', 'when'];

  COFFEE_ALIAS_MAP = {
    and: '&&',
    or: '||',
    is: '==',
    isnt: '!=',
    not: '!',
    yes: 'true',
    no: 'false',
    on: 'true',
    off: 'false'
  };

  COFFEE_ALIASES = (function() {
    var results;
    results = [];
    for (key in COFFEE_ALIAS_MAP) {
      results.push(key);
    }
    return results;
  })();

  COFFEE_KEYWORDS = COFFEE_KEYWORDS.concat(COFFEE_ALIASES);

  RESERVED = ['case', 'default', 'function', 'var', 'void', 'with', 'const', 'let', 'enum', 'export', 'import', 'native', 'implements', 'interface', 'package', 'private', 'protected', 'public', 'static'];

  STRICT_PROSCRIBED = ['arguments', 'eval', 'yield*'];

  JS_FORBIDDEN = JS_KEYWORDS.concat(RESERVED).concat(STRICT_PROSCRIBED);

  exports.RESERVED = RESERVED.concat(JS_KEYWORDS).concat(COFFEE_KEYWORDS).concat(STRICT_PROSCRIBED);

  exports.STRICT_PROSCRIBED = STRICT_PROSCRIBED;

  BOM = 65279;

  IDENTIFIER = /^(?!\d)((?:(?!\s)[$\w\x7f-\uffff])+)([^\n\S]*:(?!:))?/;

  NUMBER = /^0b[01]+|^0o[0-7]+|^0x[\da-f]+|^\d*\.?\d+(?:e[+-]?\d+)?/i;

  OPERATOR = /^(?:[-=]>|[-+*\/%<>&|^!?=]=|>>>=?|([-+:])\1|([&|<>*\/%])\2=?|\?(\.|::)|\.{2,3})/;

  WHITESPACE = /^[^\n\S]+/;

  COMMENT = /^###([^#][\s\S]*?)(?:###[^\n\S]*|###$)|^(?:\s*#(?!##[^#]).*)+/;

  CODE = /^[-=]>/;

  MULTI_DENT = /^(?:\n[^\n\S]*)+/;

  JSTOKEN = /^`[^\\`]*(?:\\.[^\\`]*)*`/;

  STRING_START = /^(?:'''|"""|'|")/;

  STRING_SINGLE = /^(?:[^\\']|\\[\s\S])*/;

  STRING_DOUBLE = /^(?:[^\\"#]|\\[\s\S]|\#(?!\{))*/;

  HEREDOC_SINGLE = /^(?:[^\\']|\\[\s\S]|'(?!''))*/;

  HEREDOC_DOUBLE = /^(?:[^\\"#]|\\[\s\S]|"(?!"")|\#(?!\{))*/;

  STRING_OMIT = /((?:\\\\)+)|\\[^\S\n]*\n\s*/g;

  SIMPLE_STRING_OMIT = /\s*\n\s*/g;

  HEREDOC_INDENT = /\n+([^\n\S]*)(?=\S)/g;

  REGEX = /^\/(?!\/)((?:[^[\/\n\\]|\\[^\n]|\[(?:\\[^\n]|[^\]\n\\])*\])*)(\/)?/;

  REGEX_FLAGS = /^\w*/;

  VALID_FLAGS = /^(?!.*(.).*\1)[imgy]*$/;

  HEREGEX = /^(?:[^\\\/#]|\\[\s\S]|\/(?!\/\/)|\#(?!\{))*/;

  HEREGEX_OMIT = /((?:\\\\)+)|\\(\s)|\s+(?:#.*)?/g;

  REGEX_ILLEGAL = /^(\/|\/{3}\s*)(\*)/;

  POSSIBLY_DIVISION = /^\/=?\s/;

  HERECOMMENT_ILLEGAL = /\*\//;

  LINE_CONTINUER = /^\s*(?:,|\??\.(?![.\d])|::)/;

  INVALID_ESCAPE = /((?:^|[^\\])(?:\\\\)*)\\(?:(0[0-7]|[1-7])|(x(?![\da-fA-F]{2}).{0,2})|(u(?![\da-fA-F]{4}).{0,4}))/;

  LEADING_BLANK_LINE = /^[^\n\S]*\n/;

  TRAILING_BLANK_LINE = /\n[^\n\S]*$/;

  TRAILING_SPACES = /\s+$/;

  COMPOUND_ASSIGN = ['-=', '+=', '/=', '*=', '%=', '||=', '&&=', '?=', '<<=', '>>=', '>>>=', '&=', '^=', '|=', '**=', '//=', '%%='];

  UNARY = ['NEW', 'TYPEOF', 'DELETE', 'DO'];

  UNARY_MATH = ['!', '~'];

  LOGIC = ['&&', '||', '&', '|', '^'];

  SHIFT = ['<<', '>>', '>>>'];

  COMPARE = ['==', '!=', '<', '>', '<=', '>='];

  MATH = ['*', '/', '%', '//', '%%'];

  RELATION = ['IN', 'OF', 'INSTANCEOF'];

  BOOL = ['TRUE', 'FALSE'];

  CALLABLE = ['IDENTIFIER', ')', ']', '?', '@', 'THIS', 'SUPER'];

  INDEXABLE = CALLABLE.concat(['NUMBER', 'STRING', 'STRING_END', 'REGEX', 'REGEX_END', 'BOOL', 'NULL', 'UNDEFINED', '}', '::']);

  NOT_REGEX = INDEXABLE.concat(['++', '--']);

  LINE_BREAK = ['INDENT', 'OUTDENT', 'TERMINATOR'];

  INDENTABLE_CLOSERS = [')', '}', ']'];

}).call(this);

},{"./helpers":21,"./rewriter":26}],23:[function(require,module,exports){
// Generated by CoffeeScript 1.9.3
(function() {
  var Access, Arr, Assign, Base, Block, Call, Class, Code, CodeFragment, Comment, Existence, Expansion, Extends, For, HEXNUM, IDENTIFIER, IS_REGEX, IS_STRING, If, In, Index, LEVEL_ACCESS, LEVEL_COND, LEVEL_LIST, LEVEL_OP, LEVEL_PAREN, LEVEL_TOP, Literal, NEGATE, NO, NUMBER, Obj, Op, Param, Parens, RESERVED, Range, Return, SIMPLENUM, STRICT_PROSCRIBED, Scope, Slice, Splat, Switch, TAB, THIS, Throw, Try, UTILITIES, Value, While, YES, addLocationDataFn, compact, del, ends, extend, flatten, fragmentsToText, isComplexOrAssignable, isLiteralArguments, isLiteralThis, locationDataToString, merge, multident, parseNum, ref1, ref2, some, starts, throwSyntaxError, unfoldSoak, utility,
    extend1 = function(child, parent) { for (var key in parent) { if (hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; },
    hasProp = {}.hasOwnProperty,
    indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; },
    slice = [].slice;

  Error.stackTraceLimit = Infinity;

  Scope = require('./scope').Scope;

  ref1 = require('./lexer'), RESERVED = ref1.RESERVED, STRICT_PROSCRIBED = ref1.STRICT_PROSCRIBED;

  ref2 = require('./helpers'), compact = ref2.compact, flatten = ref2.flatten, extend = ref2.extend, merge = ref2.merge, del = ref2.del, starts = ref2.starts, ends = ref2.ends, some = ref2.some, addLocationDataFn = ref2.addLocationDataFn, locationDataToString = ref2.locationDataToString, throwSyntaxError = ref2.throwSyntaxError;

  exports.extend = extend;

  exports.addLocationDataFn = addLocationDataFn;

  YES = function() {
    return true;
  };

  NO = function() {
    return false;
  };

  THIS = function() {
    return this;
  };

  NEGATE = function() {
    this.negated = !this.negated;
    return this;
  };

  exports.CodeFragment = CodeFragment = (function() {
    function CodeFragment(parent, code) {
      var ref3;
      this.code = "" + code;
      this.locationData = parent != null ? parent.locationData : void 0;
      this.type = (parent != null ? (ref3 = parent.constructor) != null ? ref3.name : void 0 : void 0) || 'unknown';
    }

    CodeFragment.prototype.toString = function() {
      return "" + this.code + (this.locationData ? ": " + locationDataToString(this.locationData) : '');
    };

    return CodeFragment;

  })();

  fragmentsToText = function(fragments) {
    var fragment;
    return ((function() {
      var j, len1, results;
      results = [];
      for (j = 0, len1 = fragments.length; j < len1; j++) {
        fragment = fragments[j];
        results.push(fragment.code);
      }
      return results;
    })()).join('');
  };

  exports.Base = Base = (function() {
    function Base() {}

    Base.prototype.compile = function(o, lvl) {
      return fragmentsToText(this.compileToFragments(o, lvl));
    };

    Base.prototype.compileToFragments = function(o, lvl) {
      var node;
      o = extend({}, o);
      if (lvl) {
        o.level = lvl;
      }
      node = this.unfoldSoak(o) || this;
      node.tab = o.indent;
      if (o.level === LEVEL_TOP || !node.isStatement(o)) {
        return node.compileNode(o);
      } else {
        return node.compileClosure(o);
      }
    };

    Base.prototype.compileClosure = function(o) {
      var args, argumentsNode, func, jumpNode, meth, parts, ref3;
      if (jumpNode = this.jumps()) {
        jumpNode.error('cannot use a pure statement in an expression');
      }
      o.sharedScope = true;
      func = new Code([], Block.wrap([this]));
      args = [];
      if ((argumentsNode = this.contains(isLiteralArguments)) || this.contains(isLiteralThis)) {
        args = [new Literal('this')];
        if (argumentsNode) {
          meth = 'apply';
          args.push(new Literal('arguments'));
        } else {
          meth = 'call';
        }
        func = new Value(func, [new Access(new Literal(meth))]);
      }
      parts = (new Call(func, args)).compileNode(o);
      if (func.isGenerator || ((ref3 = func.base) != null ? ref3.isGenerator : void 0)) {
        parts.unshift(this.makeCode("(yield* "));
        parts.push(this.makeCode(")"));
      }
      return parts;
    };

    Base.prototype.cache = function(o, level, isComplex) {
      var complex, ref, sub;
      complex = isComplex != null ? isComplex(this) : this.isComplex();
      if (complex) {
        ref = new Literal(o.scope.freeVariable('ref'));
        sub = new Assign(ref, this);
        if (level) {
          return [sub.compileToFragments(o, level), [this.makeCode(ref.value)]];
        } else {
          return [sub, ref];
        }
      } else {
        ref = level ? this.compileToFragments(o, level) : this;
        return [ref, ref];
      }
    };

    Base.prototype.cacheToCodeFragments = function(cacheValues) {
      return [fragmentsToText(cacheValues[0]), fragmentsToText(cacheValues[1])];
    };

    Base.prototype.makeReturn = function(res) {
      var me;
      me = this.unwrapAll();
      if (res) {
        return new Call(new Literal(res + ".push"), [me]);
      } else {
        return new Return(me);
      }
    };

    Base.prototype.contains = function(pred) {
      var node;
      node = void 0;
      this.traverseChildren(false, function(n) {
        if (pred(n)) {
          node = n;
          return false;
        }
      });
      return node;
    };

    Base.prototype.lastNonComment = function(list) {
      var i;
      i = list.length;
      while (i--) {
        if (!(list[i] instanceof Comment)) {
          return list[i];
        }
      }
      return null;
    };

    Base.prototype.toString = function(idt, name) {
      var tree;
      if (idt == null) {
        idt = '';
      }
      if (name == null) {
        name = this.constructor.name;
      }
      tree = '\n' + idt + name;
      if (this.soak) {
        tree += '?';
      }
      this.eachChild(function(node) {
        return tree += node.toString(idt + TAB);
      });
      return tree;
    };

    Base.prototype.eachChild = function(func) {
      var attr, child, j, k, len1, len2, ref3, ref4;
      if (!this.children) {
        return this;
      }
      ref3 = this.children;
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        attr = ref3[j];
        if (this[attr]) {
          ref4 = flatten([this[attr]]);
          for (k = 0, len2 = ref4.length; k < len2; k++) {
            child = ref4[k];
            if (func(child) === false) {
              return this;
            }
          }
        }
      }
      return this;
    };

    Base.prototype.traverseChildren = function(crossScope, func) {
      return this.eachChild(function(child) {
        var recur;
        recur = func(child);
        if (recur !== false) {
          return child.traverseChildren(crossScope, func);
        }
      });
    };

    Base.prototype.invert = function() {
      return new Op('!', this);
    };

    Base.prototype.unwrapAll = function() {
      var node;
      node = this;
      while (node !== (node = node.unwrap())) {
        continue;
      }
      return node;
    };

    Base.prototype.children = [];

    Base.prototype.isStatement = NO;

    Base.prototype.jumps = NO;

    Base.prototype.isComplex = YES;

    Base.prototype.isChainable = NO;

    Base.prototype.isAssignable = NO;

    Base.prototype.unwrap = THIS;

    Base.prototype.unfoldSoak = NO;

    Base.prototype.assigns = NO;

    Base.prototype.updateLocationDataIfMissing = function(locationData) {
      if (this.locationData) {
        return this;
      }
      this.locationData = locationData;
      return this.eachChild(function(child) {
        return child.updateLocationDataIfMissing(locationData);
      });
    };

    Base.prototype.error = function(message) {
      return throwSyntaxError(message, this.locationData);
    };

    Base.prototype.makeCode = function(code) {
      return new CodeFragment(this, code);
    };

    Base.prototype.wrapInBraces = function(fragments) {
      return [].concat(this.makeCode('('), fragments, this.makeCode(')'));
    };

    Base.prototype.joinFragmentArrays = function(fragmentsList, joinStr) {
      var answer, fragments, i, j, len1;
      answer = [];
      for (i = j = 0, len1 = fragmentsList.length; j < len1; i = ++j) {
        fragments = fragmentsList[i];
        if (i) {
          answer.push(this.makeCode(joinStr));
        }
        answer = answer.concat(fragments);
      }
      return answer;
    };

    return Base;

  })();

  exports.Block = Block = (function(superClass1) {
    extend1(Block, superClass1);

    function Block(nodes) {
      this.expressions = compact(flatten(nodes || []));
    }

    Block.prototype.children = ['expressions'];

    Block.prototype.push = function(node) {
      this.expressions.push(node);
      return this;
    };

    Block.prototype.pop = function() {
      return this.expressions.pop();
    };

    Block.prototype.unshift = function(node) {
      this.expressions.unshift(node);
      return this;
    };

    Block.prototype.unwrap = function() {
      if (this.expressions.length === 1) {
        return this.expressions[0];
      } else {
        return this;
      }
    };

    Block.prototype.isEmpty = function() {
      return !this.expressions.length;
    };

    Block.prototype.isStatement = function(o) {
      var exp, j, len1, ref3;
      ref3 = this.expressions;
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        exp = ref3[j];
        if (exp.isStatement(o)) {
          return true;
        }
      }
      return false;
    };

    Block.prototype.jumps = function(o) {
      var exp, j, jumpNode, len1, ref3;
      ref3 = this.expressions;
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        exp = ref3[j];
        if (jumpNode = exp.jumps(o)) {
          return jumpNode;
        }
      }
    };

    Block.prototype.makeReturn = function(res) {
      var expr, len;
      len = this.expressions.length;
      while (len--) {
        expr = this.expressions[len];
        if (!(expr instanceof Comment)) {
          this.expressions[len] = expr.makeReturn(res);
          if (expr instanceof Return && !expr.expression) {
            this.expressions.splice(len, 1);
          }
          break;
        }
      }
      return this;
    };

    Block.prototype.compileToFragments = function(o, level) {
      if (o == null) {
        o = {};
      }
      if (o.scope) {
        return Block.__super__.compileToFragments.call(this, o, level);
      } else {
        return this.compileRoot(o);
      }
    };

    Block.prototype.compileNode = function(o) {
      var answer, compiledNodes, fragments, index, j, len1, node, ref3, top;
      this.tab = o.indent;
      top = o.level === LEVEL_TOP;
      compiledNodes = [];
      ref3 = this.expressions;
      for (index = j = 0, len1 = ref3.length; j < len1; index = ++j) {
        node = ref3[index];
        node = node.unwrapAll();
        node = node.unfoldSoak(o) || node;
        if (node instanceof Block) {
          compiledNodes.push(node.compileNode(o));
        } else if (top) {
          node.front = true;
          fragments = node.compileToFragments(o);
          if (!node.isStatement(o)) {
            fragments.unshift(this.makeCode("" + this.tab));
            fragments.push(this.makeCode(";"));
          }
          compiledNodes.push(fragments);
        } else {
          compiledNodes.push(node.compileToFragments(o, LEVEL_LIST));
        }
      }
      if (top) {
        if (this.spaced) {
          return [].concat(this.joinFragmentArrays(compiledNodes, '\n\n'), this.makeCode("\n"));
        } else {
          return this.joinFragmentArrays(compiledNodes, '\n');
        }
      }
      if (compiledNodes.length) {
        answer = this.joinFragmentArrays(compiledNodes, ', ');
      } else {
        answer = [this.makeCode("void 0")];
      }
      if (compiledNodes.length > 1 && o.level >= LEVEL_LIST) {
        return this.wrapInBraces(answer);
      } else {
        return answer;
      }
    };

    Block.prototype.compileRoot = function(o) {
      var exp, fragments, i, j, len1, name, prelude, preludeExps, ref3, ref4, rest;
      o.indent = o.bare ? '' : TAB;
      o.level = LEVEL_TOP;
      this.spaced = true;
      o.scope = new Scope(null, this, null, (ref3 = o.referencedVars) != null ? ref3 : []);
      ref4 = o.locals || [];
      for (j = 0, len1 = ref4.length; j < len1; j++) {
        name = ref4[j];
        o.scope.parameter(name);
      }
      prelude = [];
      if (!o.bare) {
        preludeExps = (function() {
          var k, len2, ref5, results;
          ref5 = this.expressions;
          results = [];
          for (i = k = 0, len2 = ref5.length; k < len2; i = ++k) {
            exp = ref5[i];
            if (!(exp.unwrap() instanceof Comment)) {
              break;
            }
            results.push(exp);
          }
          return results;
        }).call(this);
        rest = this.expressions.slice(preludeExps.length);
        this.expressions = preludeExps;
        if (preludeExps.length) {
          prelude = this.compileNode(merge(o, {
            indent: ''
          }));
          prelude.push(this.makeCode("\n"));
        }
        this.expressions = rest;
      }
      fragments = this.compileWithDeclarations(o);
      if (o.bare) {
        return fragments;
      }
      return [].concat(prelude, this.makeCode("(function() {\n"), fragments, this.makeCode("\n}).call(this);\n"));
    };

    Block.prototype.compileWithDeclarations = function(o) {
      var assigns, declars, exp, fragments, i, j, len1, post, ref3, ref4, ref5, rest, scope, spaced;
      fragments = [];
      post = [];
      ref3 = this.expressions;
      for (i = j = 0, len1 = ref3.length; j < len1; i = ++j) {
        exp = ref3[i];
        exp = exp.unwrap();
        if (!(exp instanceof Comment || exp instanceof Literal)) {
          break;
        }
      }
      o = merge(o, {
        level: LEVEL_TOP
      });
      if (i) {
        rest = this.expressions.splice(i, 9e9);
        ref4 = [this.spaced, false], spaced = ref4[0], this.spaced = ref4[1];
        ref5 = [this.compileNode(o), spaced], fragments = ref5[0], this.spaced = ref5[1];
        this.expressions = rest;
      }
      post = this.compileNode(o);
      scope = o.scope;
      if (scope.expressions === this) {
        declars = o.scope.hasDeclarations();
        assigns = scope.hasAssignments;
        if (declars || assigns) {
          if (i) {
            fragments.push(this.makeCode('\n'));
          }
          fragments.push(this.makeCode(this.tab + "var "));
          if (declars) {
            fragments.push(this.makeCode(scope.declaredVariables().join(', ')));
          }
          if (assigns) {
            if (declars) {
              fragments.push(this.makeCode(",\n" + (this.tab + TAB)));
            }
            fragments.push(this.makeCode(scope.assignedVariables().join(",\n" + (this.tab + TAB))));
          }
          fragments.push(this.makeCode(";\n" + (this.spaced ? '\n' : '')));
        } else if (fragments.length && post.length) {
          fragments.push(this.makeCode("\n"));
        }
      }
      return fragments.concat(post);
    };

    Block.wrap = function(nodes) {
      if (nodes.length === 1 && nodes[0] instanceof Block) {
        return nodes[0];
      }
      return new Block(nodes);
    };

    return Block;

  })(Base);

  exports.Literal = Literal = (function(superClass1) {
    extend1(Literal, superClass1);

    function Literal(value1) {
      this.value = value1;
    }

    Literal.prototype.makeReturn = function() {
      if (this.isStatement()) {
        return this;
      } else {
        return Literal.__super__.makeReturn.apply(this, arguments);
      }
    };

    Literal.prototype.isAssignable = function() {
      return IDENTIFIER.test(this.value);
    };

    Literal.prototype.isStatement = function() {
      var ref3;
      return (ref3 = this.value) === 'break' || ref3 === 'continue' || ref3 === 'debugger';
    };

    Literal.prototype.isComplex = NO;

    Literal.prototype.assigns = function(name) {
      return name === this.value;
    };

    Literal.prototype.jumps = function(o) {
      if (this.value === 'break' && !((o != null ? o.loop : void 0) || (o != null ? o.block : void 0))) {
        return this;
      }
      if (this.value === 'continue' && !(o != null ? o.loop : void 0)) {
        return this;
      }
    };

    Literal.prototype.compileNode = function(o) {
      var answer, code, ref3;
      code = this.value === 'this' ? ((ref3 = o.scope.method) != null ? ref3.bound : void 0) ? o.scope.method.context : this.value : this.value.reserved ? "\"" + this.value + "\"" : this.value;
      answer = this.isStatement() ? "" + this.tab + code + ";" : code;
      return [this.makeCode(answer)];
    };

    Literal.prototype.toString = function() {
      return ' "' + this.value + '"';
    };

    return Literal;

  })(Base);

  exports.Undefined = (function(superClass1) {
    extend1(Undefined, superClass1);

    function Undefined() {
      return Undefined.__super__.constructor.apply(this, arguments);
    }

    Undefined.prototype.isAssignable = NO;

    Undefined.prototype.isComplex = NO;

    Undefined.prototype.compileNode = function(o) {
      return [this.makeCode(o.level >= LEVEL_ACCESS ? '(void 0)' : 'void 0')];
    };

    return Undefined;

  })(Base);

  exports.Null = (function(superClass1) {
    extend1(Null, superClass1);

    function Null() {
      return Null.__super__.constructor.apply(this, arguments);
    }

    Null.prototype.isAssignable = NO;

    Null.prototype.isComplex = NO;

    Null.prototype.compileNode = function() {
      return [this.makeCode("null")];
    };

    return Null;

  })(Base);

  exports.Bool = (function(superClass1) {
    extend1(Bool, superClass1);

    Bool.prototype.isAssignable = NO;

    Bool.prototype.isComplex = NO;

    Bool.prototype.compileNode = function() {
      return [this.makeCode(this.val)];
    };

    function Bool(val1) {
      this.val = val1;
    }

    return Bool;

  })(Base);

  exports.Return = Return = (function(superClass1) {
    extend1(Return, superClass1);

    function Return(expression) {
      this.expression = expression;
    }

    Return.prototype.children = ['expression'];

    Return.prototype.isStatement = YES;

    Return.prototype.makeReturn = THIS;

    Return.prototype.jumps = THIS;

    Return.prototype.compileToFragments = function(o, level) {
      var expr, ref3;
      expr = (ref3 = this.expression) != null ? ref3.makeReturn() : void 0;
      if (expr && !(expr instanceof Return)) {
        return expr.compileToFragments(o, level);
      } else {
        return Return.__super__.compileToFragments.call(this, o, level);
      }
    };

    Return.prototype.compileNode = function(o) {
      var answer, exprIsYieldReturn, ref3;
      answer = [];
      exprIsYieldReturn = (ref3 = this.expression) != null ? typeof ref3.isYieldReturn === "function" ? ref3.isYieldReturn() : void 0 : void 0;
      if (!exprIsYieldReturn) {
        answer.push(this.makeCode(this.tab + ("return" + (this.expression ? " " : ""))));
      }
      if (this.expression) {
        answer = answer.concat(this.expression.compileToFragments(o, LEVEL_PAREN));
      }
      if (!exprIsYieldReturn) {
        answer.push(this.makeCode(";"));
      }
      return answer;
    };

    return Return;

  })(Base);

  exports.Value = Value = (function(superClass1) {
    extend1(Value, superClass1);

    function Value(base, props, tag) {
      if (!props && base instanceof Value) {
        return base;
      }
      this.base = base;
      this.properties = props || [];
      if (tag) {
        this[tag] = true;
      }
      return this;
    }

    Value.prototype.children = ['base', 'properties'];

    Value.prototype.add = function(props) {
      this.properties = this.properties.concat(props);
      return this;
    };

    Value.prototype.hasProperties = function() {
      return !!this.properties.length;
    };

    Value.prototype.bareLiteral = function(type) {
      return !this.properties.length && this.base instanceof type;
    };

    Value.prototype.isArray = function() {
      return this.bareLiteral(Arr);
    };

    Value.prototype.isRange = function() {
      return this.bareLiteral(Range);
    };

    Value.prototype.isComplex = function() {
      return this.hasProperties() || this.base.isComplex();
    };

    Value.prototype.isAssignable = function() {
      return this.hasProperties() || this.base.isAssignable();
    };

    Value.prototype.isSimpleNumber = function() {
      return this.bareLiteral(Literal) && SIMPLENUM.test(this.base.value);
    };

    Value.prototype.isString = function() {
      return this.bareLiteral(Literal) && IS_STRING.test(this.base.value);
    };

    Value.prototype.isRegex = function() {
      return this.bareLiteral(Literal) && IS_REGEX.test(this.base.value);
    };

    Value.prototype.isAtomic = function() {
      var j, len1, node, ref3;
      ref3 = this.properties.concat(this.base);
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        node = ref3[j];
        if (node.soak || node instanceof Call) {
          return false;
        }
      }
      return true;
    };

    Value.prototype.isNotCallable = function() {
      return this.isSimpleNumber() || this.isString() || this.isRegex() || this.isArray() || this.isRange() || this.isSplice() || this.isObject();
    };

    Value.prototype.isStatement = function(o) {
      return !this.properties.length && this.base.isStatement(o);
    };

    Value.prototype.assigns = function(name) {
      return !this.properties.length && this.base.assigns(name);
    };

    Value.prototype.jumps = function(o) {
      return !this.properties.length && this.base.jumps(o);
    };

    Value.prototype.isObject = function(onlyGenerated) {
      if (this.properties.length) {
        return false;
      }
      return (this.base instanceof Obj) && (!onlyGenerated || this.base.generated);
    };

    Value.prototype.isSplice = function() {
      var lastProp, ref3;
      ref3 = this.properties, lastProp = ref3[ref3.length - 1];
      return lastProp instanceof Slice;
    };

    Value.prototype.looksStatic = function(className) {
      var ref3;
      return this.base.value === className && this.properties.length === 1 && ((ref3 = this.properties[0].name) != null ? ref3.value : void 0) !== 'prototype';
    };

    Value.prototype.unwrap = function() {
      if (this.properties.length) {
        return this;
      } else {
        return this.base;
      }
    };

    Value.prototype.cacheReference = function(o) {
      var base, bref, name, nref, ref3;
      ref3 = this.properties, name = ref3[ref3.length - 1];
      if (this.properties.length < 2 && !this.base.isComplex() && !(name != null ? name.isComplex() : void 0)) {
        return [this, this];
      }
      base = new Value(this.base, this.properties.slice(0, -1));
      if (base.isComplex()) {
        bref = new Literal(o.scope.freeVariable('base'));
        base = new Value(new Parens(new Assign(bref, base)));
      }
      if (!name) {
        return [base, bref];
      }
      if (name.isComplex()) {
        nref = new Literal(o.scope.freeVariable('name'));
        name = new Index(new Assign(nref, name.index));
        nref = new Index(nref);
      }
      return [base.add(name), new Value(bref || base.base, [nref || name])];
    };

    Value.prototype.compileNode = function(o) {
      var fragments, j, len1, prop, props;
      this.base.front = this.front;
      props = this.properties;
      fragments = this.base.compileToFragments(o, (props.length ? LEVEL_ACCESS : null));
      if ((this.base instanceof Parens || props.length) && SIMPLENUM.test(fragmentsToText(fragments))) {
        fragments.push(this.makeCode('.'));
      }
      for (j = 0, len1 = props.length; j < len1; j++) {
        prop = props[j];
        fragments.push.apply(fragments, prop.compileToFragments(o));
      }
      return fragments;
    };

    Value.prototype.unfoldSoak = function(o) {
      return this.unfoldedSoak != null ? this.unfoldedSoak : this.unfoldedSoak = (function(_this) {
        return function() {
          var fst, i, ifn, j, len1, prop, ref, ref3, ref4, snd;
          if (ifn = _this.base.unfoldSoak(o)) {
            (ref3 = ifn.body.properties).push.apply(ref3, _this.properties);
            return ifn;
          }
          ref4 = _this.properties;
          for (i = j = 0, len1 = ref4.length; j < len1; i = ++j) {
            prop = ref4[i];
            if (!prop.soak) {
              continue;
            }
            prop.soak = false;
            fst = new Value(_this.base, _this.properties.slice(0, i));
            snd = new Value(_this.base, _this.properties.slice(i));
            if (fst.isComplex()) {
              ref = new Literal(o.scope.freeVariable('ref'));
              fst = new Parens(new Assign(ref, fst));
              snd.base = ref;
            }
            return new If(new Existence(fst), snd, {
              soak: true
            });
          }
          return false;
        };
      })(this)();
    };

    return Value;

  })(Base);

  exports.Comment = Comment = (function(superClass1) {
    extend1(Comment, superClass1);

    function Comment(comment1) {
      this.comment = comment1;
    }

    Comment.prototype.isStatement = YES;

    Comment.prototype.makeReturn = THIS;

    Comment.prototype.compileNode = function(o, level) {
      var code, comment;
      comment = this.comment.replace(/^(\s*)#(?=\s)/gm, "$1 *");
      code = "/*" + (multident(comment, this.tab)) + (indexOf.call(comment, '\n') >= 0 ? "\n" + this.tab : '') + " */";
      if ((level || o.level) === LEVEL_TOP) {
        code = o.indent + code;
      }
      return [this.makeCode("\n"), this.makeCode(code)];
    };

    return Comment;

  })(Base);

  exports.Call = Call = (function(superClass1) {
    extend1(Call, superClass1);

    function Call(variable, args1, soak) {
      this.args = args1 != null ? args1 : [];
      this.soak = soak;
      this.isNew = false;
      this.isSuper = variable === 'super';
      this.variable = this.isSuper ? null : variable;
      if (variable instanceof Value && variable.isNotCallable()) {
        variable.error("literal is not a function");
      }
    }

    Call.prototype.children = ['variable', 'args'];

    Call.prototype.newInstance = function() {
      var base, ref3;
      base = ((ref3 = this.variable) != null ? ref3.base : void 0) || this.variable;
      if (base instanceof Call && !base.isNew) {
        base.newInstance();
      } else {
        this.isNew = true;
      }
      return this;
    };

    Call.prototype.superReference = function(o) {
      var accesses, base, bref, klass, method, name, nref, variable;
      method = o.scope.namedMethod();
      if (method != null ? method.klass : void 0) {
        klass = method.klass, name = method.name, variable = method.variable;
        if (klass.isComplex()) {
          bref = new Literal(o.scope.parent.freeVariable('base'));
          base = new Value(new Parens(new Assign(bref, klass)));
          variable.base = base;
          variable.properties.splice(0, klass.properties.length);
        }
        if (name.isComplex() || (name instanceof Index && name.index.isAssignable())) {
          nref = new Literal(o.scope.parent.freeVariable('name'));
          name = new Index(new Assign(nref, name.index));
          variable.properties.pop();
          variable.properties.push(name);
        }
        accesses = [new Access(new Literal('__super__'))];
        if (method["static"]) {
          accesses.push(new Access(new Literal('constructor')));
        }
        accesses.push(nref != null ? new Index(nref) : name);
        return (new Value(bref != null ? bref : klass, accesses)).compile(o);
      } else if (method != null ? method.ctor : void 0) {
        return method.name + ".__super__.constructor";
      } else {
        return this.error('cannot call super outside of an instance method.');
      }
    };

    Call.prototype.superThis = function(o) {
      var method;
      method = o.scope.method;
      return (method && !method.klass && method.context) || "this";
    };

    Call.prototype.unfoldSoak = function(o) {
      var call, ifn, j, left, len1, list, ref3, ref4, rite;
      if (this.soak) {
        if (this.variable) {
          if (ifn = unfoldSoak(o, this, 'variable')) {
            return ifn;
          }
          ref3 = new Value(this.variable).cacheReference(o), left = ref3[0], rite = ref3[1];
        } else {
          left = new Literal(this.superReference(o));
          rite = new Value(left);
        }
        rite = new Call(rite, this.args);
        rite.isNew = this.isNew;
        left = new Literal("typeof " + (left.compile(o)) + " === \"function\"");
        return new If(left, new Value(rite), {
          soak: true
        });
      }
      call = this;
      list = [];
      while (true) {
        if (call.variable instanceof Call) {
          list.push(call);
          call = call.variable;
          continue;
        }
        if (!(call.variable instanceof Value)) {
          break;
        }
        list.push(call);
        if (!((call = call.variable.base) instanceof Call)) {
          break;
        }
      }
      ref4 = list.reverse();
      for (j = 0, len1 = ref4.length; j < len1; j++) {
        call = ref4[j];
        if (ifn) {
          if (call.variable instanceof Call) {
            call.variable = ifn;
          } else {
            call.variable.base = ifn;
          }
        }
        ifn = unfoldSoak(o, call, 'variable');
      }
      return ifn;
    };

    Call.prototype.compileNode = function(o) {
      var arg, argIndex, compiledArgs, compiledArray, fragments, j, len1, preface, ref3, ref4;
      if ((ref3 = this.variable) != null) {
        ref3.front = this.front;
      }
      compiledArray = Splat.compileSplattedArray(o, this.args, true);
      if (compiledArray.length) {
        return this.compileSplat(o, compiledArray);
      }
      compiledArgs = [];
      ref4 = this.args;
      for (argIndex = j = 0, len1 = ref4.length; j < len1; argIndex = ++j) {
        arg = ref4[argIndex];
        if (argIndex) {
          compiledArgs.push(this.makeCode(", "));
        }
        compiledArgs.push.apply(compiledArgs, arg.compileToFragments(o, LEVEL_LIST));
      }
      fragments = [];
      if (this.isSuper) {
        preface = this.superReference(o) + (".call(" + (this.superThis(o)));
        if (compiledArgs.length) {
          preface += ", ";
        }
        fragments.push(this.makeCode(preface));
      } else {
        if (this.isNew) {
          fragments.push(this.makeCode('new '));
        }
        fragments.push.apply(fragments, this.variable.compileToFragments(o, LEVEL_ACCESS));
        fragments.push(this.makeCode("("));
      }
      fragments.push.apply(fragments, compiledArgs);
      fragments.push(this.makeCode(")"));
      return fragments;
    };

    Call.prototype.compileSplat = function(o, splatArgs) {
      var answer, base, fun, idt, name, ref;
      if (this.isSuper) {
        return [].concat(this.makeCode((this.superReference(o)) + ".apply(" + (this.superThis(o)) + ", "), splatArgs, this.makeCode(")"));
      }
      if (this.isNew) {
        idt = this.tab + TAB;
        return [].concat(this.makeCode("(function(func, args, ctor) {\n" + idt + "ctor.prototype = func.prototype;\n" + idt + "var child = new ctor, result = func.apply(child, args);\n" + idt + "return Object(result) === result ? result : child;\n" + this.tab + "})("), this.variable.compileToFragments(o, LEVEL_LIST), this.makeCode(", "), splatArgs, this.makeCode(", function(){})"));
      }
      answer = [];
      base = new Value(this.variable);
      if ((name = base.properties.pop()) && base.isComplex()) {
        ref = o.scope.freeVariable('ref');
        answer = answer.concat(this.makeCode("(" + ref + " = "), base.compileToFragments(o, LEVEL_LIST), this.makeCode(")"), name.compileToFragments(o));
      } else {
        fun = base.compileToFragments(o, LEVEL_ACCESS);
        if (SIMPLENUM.test(fragmentsToText(fun))) {
          fun = this.wrapInBraces(fun);
        }
        if (name) {
          ref = fragmentsToText(fun);
          fun.push.apply(fun, name.compileToFragments(o));
        } else {
          ref = 'null';
        }
        answer = answer.concat(fun);
      }
      return answer = answer.concat(this.makeCode(".apply(" + ref + ", "), splatArgs, this.makeCode(")"));
    };

    return Call;

  })(Base);

  exports.Extends = Extends = (function(superClass1) {
    extend1(Extends, superClass1);

    function Extends(child1, parent1) {
      this.child = child1;
      this.parent = parent1;
    }

    Extends.prototype.children = ['child', 'parent'];

    Extends.prototype.compileToFragments = function(o) {
      return new Call(new Value(new Literal(utility('extend', o))), [this.child, this.parent]).compileToFragments(o);
    };

    return Extends;

  })(Base);

  exports.Access = Access = (function(superClass1) {
    extend1(Access, superClass1);

    function Access(name1, tag) {
      this.name = name1;
      this.name.asKey = true;
      this.soak = tag === 'soak';
    }

    Access.prototype.children = ['name'];

    Access.prototype.compileToFragments = function(o) {
      var name;
      name = this.name.compileToFragments(o);
      if (IDENTIFIER.test(fragmentsToText(name))) {
        name.unshift(this.makeCode("."));
      } else {
        name.unshift(this.makeCode("["));
        name.push(this.makeCode("]"));
      }
      return name;
    };

    Access.prototype.isComplex = NO;

    return Access;

  })(Base);

  exports.Index = Index = (function(superClass1) {
    extend1(Index, superClass1);

    function Index(index1) {
      this.index = index1;
    }

    Index.prototype.children = ['index'];

    Index.prototype.compileToFragments = function(o) {
      return [].concat(this.makeCode("["), this.index.compileToFragments(o, LEVEL_PAREN), this.makeCode("]"));
    };

    Index.prototype.isComplex = function() {
      return this.index.isComplex();
    };

    return Index;

  })(Base);

  exports.Range = Range = (function(superClass1) {
    extend1(Range, superClass1);

    Range.prototype.children = ['from', 'to'];

    function Range(from1, to1, tag) {
      this.from = from1;
      this.to = to1;
      this.exclusive = tag === 'exclusive';
      this.equals = this.exclusive ? '' : '=';
    }

    Range.prototype.compileVariables = function(o) {
      var isComplex, ref3, ref4, ref5, ref6, step;
      o = merge(o, {
        top: true
      });
      isComplex = del(o, 'isComplex');
      ref3 = this.cacheToCodeFragments(this.from.cache(o, LEVEL_LIST, isComplex)), this.fromC = ref3[0], this.fromVar = ref3[1];
      ref4 = this.cacheToCodeFragments(this.to.cache(o, LEVEL_LIST, isComplex)), this.toC = ref4[0], this.toVar = ref4[1];
      if (step = del(o, 'step')) {
        ref5 = this.cacheToCodeFragments(step.cache(o, LEVEL_LIST, isComplex)), this.step = ref5[0], this.stepVar = ref5[1];
      }
      ref6 = [this.fromVar.match(NUMBER), this.toVar.match(NUMBER)], this.fromNum = ref6[0], this.toNum = ref6[1];
      if (this.stepVar) {
        return this.stepNum = this.stepVar.match(NUMBER);
      }
    };

    Range.prototype.compileNode = function(o) {
      var cond, condPart, from, gt, idx, idxName, known, lt, namedIndex, ref3, ref4, stepPart, to, varPart;
      if (!this.fromVar) {
        this.compileVariables(o);
      }
      if (!o.index) {
        return this.compileArray(o);
      }
      known = this.fromNum && this.toNum;
      idx = del(o, 'index');
      idxName = del(o, 'name');
      namedIndex = idxName && idxName !== idx;
      varPart = idx + " = " + this.fromC;
      if (this.toC !== this.toVar) {
        varPart += ", " + this.toC;
      }
      if (this.step !== this.stepVar) {
        varPart += ", " + this.step;
      }
      ref3 = [idx + " <" + this.equals, idx + " >" + this.equals], lt = ref3[0], gt = ref3[1];
      condPart = this.stepNum ? parseNum(this.stepNum[0]) > 0 ? lt + " " + this.toVar : gt + " " + this.toVar : known ? ((ref4 = [parseNum(this.fromNum[0]), parseNum(this.toNum[0])], from = ref4[0], to = ref4[1], ref4), from <= to ? lt + " " + to : gt + " " + to) : (cond = this.stepVar ? this.stepVar + " > 0" : this.fromVar + " <= " + this.toVar, cond + " ? " + lt + " " + this.toVar + " : " + gt + " " + this.toVar);
      stepPart = this.stepVar ? idx + " += " + this.stepVar : known ? namedIndex ? from <= to ? "++" + idx : "--" + idx : from <= to ? idx + "++" : idx + "--" : namedIndex ? cond + " ? ++" + idx + " : --" + idx : cond + " ? " + idx + "++ : " + idx + "--";
      if (namedIndex) {
        varPart = idxName + " = " + varPart;
      }
      if (namedIndex) {
        stepPart = idxName + " = " + stepPart;
      }
      return [this.makeCode(varPart + "; " + condPart + "; " + stepPart)];
    };

    Range.prototype.compileArray = function(o) {
      var args, body, cond, hasArgs, i, idt, j, post, pre, range, ref3, ref4, result, results, vars;
      if (this.fromNum && this.toNum && Math.abs(this.fromNum - this.toNum) <= 20) {
        range = (function() {
          results = [];
          for (var j = ref3 = +this.fromNum, ref4 = +this.toNum; ref3 <= ref4 ? j <= ref4 : j >= ref4; ref3 <= ref4 ? j++ : j--){ results.push(j); }
          return results;
        }).apply(this);
        if (this.exclusive) {
          range.pop();
        }
        return [this.makeCode("[" + (range.join(', ')) + "]")];
      }
      idt = this.tab + TAB;
      i = o.scope.freeVariable('i', {
        single: true
      });
      result = o.scope.freeVariable('results');
      pre = "\n" + idt + result + " = [];";
      if (this.fromNum && this.toNum) {
        o.index = i;
        body = fragmentsToText(this.compileNode(o));
      } else {
        vars = (i + " = " + this.fromC) + (this.toC !== this.toVar ? ", " + this.toC : '');
        cond = this.fromVar + " <= " + this.toVar;
        body = "var " + vars + "; " + cond + " ? " + i + " <" + this.equals + " " + this.toVar + " : " + i + " >" + this.equals + " " + this.toVar + "; " + cond + " ? " + i + "++ : " + i + "--";
      }
      post = "{ " + result + ".push(" + i + "); }\n" + idt + "return " + result + ";\n" + o.indent;
      hasArgs = function(node) {
        return node != null ? node.contains(isLiteralArguments) : void 0;
      };
      if (hasArgs(this.from) || hasArgs(this.to)) {
        args = ', arguments';
      }
      return [this.makeCode("(function() {" + pre + "\n" + idt + "for (" + body + ")" + post + "}).apply(this" + (args != null ? args : '') + ")")];
    };

    return Range;

  })(Base);

  exports.Slice = Slice = (function(superClass1) {
    extend1(Slice, superClass1);

    Slice.prototype.children = ['range'];

    function Slice(range1) {
      this.range = range1;
      Slice.__super__.constructor.call(this);
    }

    Slice.prototype.compileNode = function(o) {
      var compiled, compiledText, from, fromCompiled, ref3, to, toStr;
      ref3 = this.range, to = ref3.to, from = ref3.from;
      fromCompiled = from && from.compileToFragments(o, LEVEL_PAREN) || [this.makeCode('0')];
      if (to) {
        compiled = to.compileToFragments(o, LEVEL_PAREN);
        compiledText = fragmentsToText(compiled);
        if (!(!this.range.exclusive && +compiledText === -1)) {
          toStr = ', ' + (this.range.exclusive ? compiledText : SIMPLENUM.test(compiledText) ? "" + (+compiledText + 1) : (compiled = to.compileToFragments(o, LEVEL_ACCESS), "+" + (fragmentsToText(compiled)) + " + 1 || 9e9"));
        }
      }
      return [this.makeCode(".slice(" + (fragmentsToText(fromCompiled)) + (toStr || '') + ")")];
    };

    return Slice;

  })(Base);

  exports.Obj = Obj = (function(superClass1) {
    extend1(Obj, superClass1);

    function Obj(props, generated) {
      this.generated = generated != null ? generated : false;
      this.objects = this.properties = props || [];
    }

    Obj.prototype.children = ['properties'];

    Obj.prototype.compileNode = function(o) {
      var answer, dynamicIndex, hasDynamic, i, idt, indent, j, join, k, key, l, lastNoncom, len1, len2, len3, node, oref, prop, props, ref3, value;
      props = this.properties;
      if (this.generated) {
        for (j = 0, len1 = props.length; j < len1; j++) {
          node = props[j];
          if (node instanceof Value) {
            node.error('cannot have an implicit value in an implicit object');
          }
        }
      }
      for (dynamicIndex = k = 0, len2 = props.length; k < len2; dynamicIndex = ++k) {
        prop = props[dynamicIndex];
        if ((prop.variable || prop).base instanceof Parens) {
          break;
        }
      }
      hasDynamic = dynamicIndex < props.length;
      idt = o.indent += TAB;
      lastNoncom = this.lastNonComment(this.properties);
      answer = [];
      if (hasDynamic) {
        oref = o.scope.freeVariable('obj');
        answer.push(this.makeCode("(\n" + idt + oref + " = "));
      }
      answer.push(this.makeCode("{" + (props.length === 0 || dynamicIndex === 0 ? '}' : '\n')));
      for (i = l = 0, len3 = props.length; l < len3; i = ++l) {
        prop = props[i];
        if (i === dynamicIndex) {
          if (i !== 0) {
            answer.push(this.makeCode("\n" + idt + "}"));
          }
          answer.push(this.makeCode(',\n'));
        }
        join = i === props.length - 1 || i === dynamicIndex - 1 ? '' : prop === lastNoncom || prop instanceof Comment ? '\n' : ',\n';
        indent = prop instanceof Comment ? '' : idt;
        if (hasDynamic && i < dynamicIndex) {
          indent += TAB;
        }
        if (prop instanceof Assign && prop.variable instanceof Value && prop.variable.hasProperties()) {
          prop.variable.error('invalid object key');
        }
        if (prop instanceof Value && prop["this"]) {
          prop = new Assign(prop.properties[0].name, prop, 'object');
        }
        if (!(prop instanceof Comment)) {
          if (i < dynamicIndex) {
            if (!(prop instanceof Assign)) {
              prop = new Assign(prop, prop, 'object');
            }
            (prop.variable.base || prop.variable).asKey = true;
          } else {
            if (prop instanceof Assign) {
              key = prop.variable;
              value = prop.value;
            } else {
              ref3 = prop.base.cache(o), key = ref3[0], value = ref3[1];
            }
            prop = new Assign(new Value(new Literal(oref), [new Access(key)]), value);
          }
        }
        if (indent) {
          answer.push(this.makeCode(indent));
        }
        answer.push.apply(answer, prop.compileToFragments(o, LEVEL_TOP));
        if (join) {
          answer.push(this.makeCode(join));
        }
      }
      if (hasDynamic) {
        answer.push(this.makeCode(",\n" + idt + oref + "\n" + this.tab + ")"));
      } else {
        if (props.length !== 0) {
          answer.push(this.makeCode("\n" + this.tab + "}"));
        }
      }
      if (this.front && !hasDynamic) {
        return this.wrapInBraces(answer);
      } else {
        return answer;
      }
    };

    Obj.prototype.assigns = function(name) {
      var j, len1, prop, ref3;
      ref3 = this.properties;
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        prop = ref3[j];
        if (prop.assigns(name)) {
          return true;
        }
      }
      return false;
    };

    return Obj;

  })(Base);

  exports.Arr = Arr = (function(superClass1) {
    extend1(Arr, superClass1);

    function Arr(objs) {
      this.objects = objs || [];
    }

    Arr.prototype.children = ['objects'];

    Arr.prototype.compileNode = function(o) {
      var answer, compiledObjs, fragments, index, j, len1, obj;
      if (!this.objects.length) {
        return [this.makeCode('[]')];
      }
      o.indent += TAB;
      answer = Splat.compileSplattedArray(o, this.objects);
      if (answer.length) {
        return answer;
      }
      answer = [];
      compiledObjs = (function() {
        var j, len1, ref3, results;
        ref3 = this.objects;
        results = [];
        for (j = 0, len1 = ref3.length; j < len1; j++) {
          obj = ref3[j];
          results.push(obj.compileToFragments(o, LEVEL_LIST));
        }
        return results;
      }).call(this);
      for (index = j = 0, len1 = compiledObjs.length; j < len1; index = ++j) {
        fragments = compiledObjs[index];
        if (index) {
          answer.push(this.makeCode(", "));
        }
        answer.push.apply(answer, fragments);
      }
      if (fragmentsToText(answer).indexOf('\n') >= 0) {
        answer.unshift(this.makeCode("[\n" + o.indent));
        answer.push(this.makeCode("\n" + this.tab + "]"));
      } else {
        answer.unshift(this.makeCode("["));
        answer.push(this.makeCode("]"));
      }
      return answer;
    };

    Arr.prototype.assigns = function(name) {
      var j, len1, obj, ref3;
      ref3 = this.objects;
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        obj = ref3[j];
        if (obj.assigns(name)) {
          return true;
        }
      }
      return false;
    };

    return Arr;

  })(Base);

  exports.Class = Class = (function(superClass1) {
    extend1(Class, superClass1);

    function Class(variable1, parent1, body1) {
      this.variable = variable1;
      this.parent = parent1;
      this.body = body1 != null ? body1 : new Block;
      this.boundFuncs = [];
      this.body.classBody = true;
    }

    Class.prototype.children = ['variable', 'parent', 'body'];

    Class.prototype.determineName = function() {
      var decl, ref3, tail;
      if (!this.variable) {
        return null;
      }
      ref3 = this.variable.properties, tail = ref3[ref3.length - 1];
      decl = tail ? tail instanceof Access && tail.name.value : this.variable.base.value;
      if (indexOf.call(STRICT_PROSCRIBED, decl) >= 0) {
        this.variable.error("class variable name may not be " + decl);
      }
      return decl && (decl = IDENTIFIER.test(decl) && decl);
    };

    Class.prototype.setContext = function(name) {
      return this.body.traverseChildren(false, function(node) {
        if (node.classBody) {
          return false;
        }
        if (node instanceof Literal && node.value === 'this') {
          return node.value = name;
        } else if (node instanceof Code) {
          if (node.bound) {
            return node.context = name;
          }
        }
      });
    };

    Class.prototype.addBoundFunctions = function(o) {
      var bvar, j, len1, lhs, ref3;
      ref3 = this.boundFuncs;
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        bvar = ref3[j];
        lhs = (new Value(new Literal("this"), [new Access(bvar)])).compile(o);
        this.ctor.body.unshift(new Literal(lhs + " = " + (utility('bind', o)) + "(" + lhs + ", this)"));
      }
    };

    Class.prototype.addProperties = function(node, name, o) {
      var acc, assign, base, exprs, func, props;
      props = node.base.properties.slice(0);
      exprs = (function() {
        var results;
        results = [];
        while (assign = props.shift()) {
          if (assign instanceof Assign) {
            base = assign.variable.base;
            delete assign.context;
            func = assign.value;
            if (base.value === 'constructor') {
              if (this.ctor) {
                assign.error('cannot define more than one constructor in a class');
              }
              if (func.bound) {
                assign.error('cannot define a constructor as a bound function');
              }
              if (func instanceof Code) {
                assign = this.ctor = func;
              } else {
                this.externalCtor = o.classScope.freeVariable('class');
                assign = new Assign(new Literal(this.externalCtor), func);
              }
            } else {
              if (assign.variable["this"]) {
                func["static"] = true;
              } else {
                acc = base.isComplex() ? new Index(base) : new Access(base);
                assign.variable = new Value(new Literal(name), [new Access(new Literal('prototype')), acc]);
                if (func instanceof Code && func.bound) {
                  this.boundFuncs.push(base);
                  func.bound = false;
                }
              }
            }
          }
          results.push(assign);
        }
        return results;
      }).call(this);
      return compact(exprs);
    };

    Class.prototype.walkBody = function(name, o) {
      return this.traverseChildren(false, (function(_this) {
        return function(child) {
          var cont, exps, i, j, len1, node, ref3;
          cont = true;
          if (child instanceof Class) {
            return false;
          }
          if (child instanceof Block) {
            ref3 = exps = child.expressions;
            for (i = j = 0, len1 = ref3.length; j < len1; i = ++j) {
              node = ref3[i];
              if (node instanceof Assign && node.variable.looksStatic(name)) {
                node.value["static"] = true;
              } else if (node instanceof Value && node.isObject(true)) {
                cont = false;
                exps[i] = _this.addProperties(node, name, o);
              }
            }
            child.expressions = exps = flatten(exps);
          }
          return cont && !(child instanceof Class);
        };
      })(this));
    };

    Class.prototype.hoistDirectivePrologue = function() {
      var expressions, index, node;
      index = 0;
      expressions = this.body.expressions;
      while ((node = expressions[index]) && node instanceof Comment || node instanceof Value && node.isString()) {
        ++index;
      }
      return this.directives = expressions.splice(0, index);
    };

    Class.prototype.ensureConstructor = function(name) {
      if (!this.ctor) {
        this.ctor = new Code;
        if (this.externalCtor) {
          this.ctor.body.push(new Literal(this.externalCtor + ".apply(this, arguments)"));
        } else if (this.parent) {
          this.ctor.body.push(new Literal(name + ".__super__.constructor.apply(this, arguments)"));
        }
        this.ctor.body.makeReturn();
        this.body.expressions.unshift(this.ctor);
      }
      this.ctor.ctor = this.ctor.name = name;
      this.ctor.klass = null;
      return this.ctor.noReturn = true;
    };

    Class.prototype.compileNode = function(o) {
      var args, argumentsNode, func, jumpNode, klass, lname, name, ref3, superClass;
      if (jumpNode = this.body.jumps()) {
        jumpNode.error('Class bodies cannot contain pure statements');
      }
      if (argumentsNode = this.body.contains(isLiteralArguments)) {
        argumentsNode.error("Class bodies shouldn't reference arguments");
      }
      name = this.determineName() || '_Class';
      if (name.reserved) {
        name = "_" + name;
      }
      lname = new Literal(name);
      func = new Code([], Block.wrap([this.body]));
      args = [];
      o.classScope = func.makeScope(o.scope);
      this.hoistDirectivePrologue();
      this.setContext(name);
      this.walkBody(name, o);
      this.ensureConstructor(name);
      this.addBoundFunctions(o);
      this.body.spaced = true;
      this.body.expressions.push(lname);
      if (this.parent) {
        superClass = new Literal(o.classScope.freeVariable('superClass', {
          reserve: false
        }));
        this.body.expressions.unshift(new Extends(lname, superClass));
        func.params.push(new Param(superClass));
        args.push(this.parent);
      }
      (ref3 = this.body.expressions).unshift.apply(ref3, this.directives);
      klass = new Parens(new Call(func, args));
      if (this.variable) {
        klass = new Assign(this.variable, klass);
      }
      return klass.compileToFragments(o);
    };

    return Class;

  })(Base);

  exports.Assign = Assign = (function(superClass1) {
    extend1(Assign, superClass1);

    function Assign(variable1, value1, context, options) {
      var forbidden, name, ref3;
      this.variable = variable1;
      this.value = value1;
      this.context = context;
      this.param = options && options.param;
      this.subpattern = options && options.subpattern;
      forbidden = (ref3 = (name = this.variable.unwrapAll().value), indexOf.call(STRICT_PROSCRIBED, ref3) >= 0);
      if (forbidden && this.context !== 'object') {
        this.variable.error("variable name may not be \"" + name + "\"");
      }
    }

    Assign.prototype.children = ['variable', 'value'];

    Assign.prototype.isStatement = function(o) {
      return (o != null ? o.level : void 0) === LEVEL_TOP && (this.context != null) && indexOf.call(this.context, "?") >= 0;
    };

    Assign.prototype.assigns = function(name) {
      return this[this.context === 'object' ? 'value' : 'variable'].assigns(name);
    };

    Assign.prototype.unfoldSoak = function(o) {
      return unfoldSoak(o, this, 'variable');
    };

    Assign.prototype.compileNode = function(o) {
      var answer, compiledName, isValue, j, name, properties, prototype, ref3, ref4, ref5, ref6, ref7, val, varBase;
      if (isValue = this.variable instanceof Value) {
        if (this.variable.isArray() || this.variable.isObject()) {
          return this.compilePatternMatch(o);
        }
        if (this.variable.isSplice()) {
          return this.compileSplice(o);
        }
        if ((ref3 = this.context) === '||=' || ref3 === '&&=' || ref3 === '?=') {
          return this.compileConditional(o);
        }
        if ((ref4 = this.context) === '**=' || ref4 === '//=' || ref4 === '%%=') {
          return this.compileSpecialMath(o);
        }
      }
      if (this.value instanceof Code) {
        if (this.value["static"]) {
          this.value.klass = this.variable.base;
          this.value.name = this.variable.properties[0];
          this.value.variable = this.variable;
        } else if (((ref5 = this.variable.properties) != null ? ref5.length : void 0) >= 2) {
          ref6 = this.variable.properties, properties = 3 <= ref6.length ? slice.call(ref6, 0, j = ref6.length - 2) : (j = 0, []), prototype = ref6[j++], name = ref6[j++];
          if (((ref7 = prototype.name) != null ? ref7.value : void 0) === 'prototype') {
            this.value.klass = new Value(this.variable.base, properties);
            this.value.name = name;
            this.value.variable = this.variable;
          }
        }
      }
      if (!this.context) {
        varBase = this.variable.unwrapAll();
        if (!varBase.isAssignable()) {
          this.variable.error("\"" + (this.variable.compile(o)) + "\" cannot be assigned");
        }
        if (!(typeof varBase.hasProperties === "function" ? varBase.hasProperties() : void 0)) {
          if (this.param) {
            o.scope.add(varBase.value, 'var');
          } else {
            o.scope.find(varBase.value);
          }
        }
      }
      val = this.value.compileToFragments(o, LEVEL_LIST);
      compiledName = this.variable.compileToFragments(o, LEVEL_LIST);
      if (this.context === 'object') {
        return compiledName.concat(this.makeCode(": "), val);
      }
      answer = compiledName.concat(this.makeCode(" " + (this.context || '=') + " "), val);
      if (o.level <= LEVEL_LIST) {
        return answer;
      } else {
        return this.wrapInBraces(answer);
      }
    };

    Assign.prototype.compilePatternMatch = function(o) {
      var acc, assigns, code, expandedIdx, fragments, i, idx, isObject, ivar, j, len1, name, obj, objects, olen, ref, ref3, ref4, ref5, ref6, ref7, ref8, rest, top, val, value, vvar, vvarText;
      top = o.level === LEVEL_TOP;
      value = this.value;
      objects = this.variable.base.objects;
      if (!(olen = objects.length)) {
        code = value.compileToFragments(o);
        if (o.level >= LEVEL_OP) {
          return this.wrapInBraces(code);
        } else {
          return code;
        }
      }
      isObject = this.variable.isObject();
      if (top && olen === 1 && !((obj = objects[0]) instanceof Splat)) {
        if (obj instanceof Assign) {
          ref3 = obj, (ref4 = ref3.variable, idx = ref4.base), obj = ref3.value;
        } else {
          idx = isObject ? obj["this"] ? obj.properties[0].name : obj : new Literal(0);
        }
        acc = IDENTIFIER.test(idx.unwrap().value || 0);
        value = new Value(value);
        value.properties.push(new (acc ? Access : Index)(idx));
        if (ref5 = obj.unwrap().value, indexOf.call(RESERVED, ref5) >= 0) {
          obj.error("assignment to a reserved word: " + (obj.compile(o)));
        }
        return new Assign(obj, value, null, {
          param: this.param
        }).compileToFragments(o, LEVEL_TOP);
      }
      vvar = value.compileToFragments(o, LEVEL_LIST);
      vvarText = fragmentsToText(vvar);
      assigns = [];
      expandedIdx = false;
      if (!IDENTIFIER.test(vvarText) || this.variable.assigns(vvarText)) {
        assigns.push([this.makeCode((ref = o.scope.freeVariable('ref')) + " = ")].concat(slice.call(vvar)));
        vvar = [this.makeCode(ref)];
        vvarText = ref;
      }
      for (i = j = 0, len1 = objects.length; j < len1; i = ++j) {
        obj = objects[i];
        idx = i;
        if (isObject) {
          if (obj instanceof Assign) {
            ref6 = obj, (ref7 = ref6.variable, idx = ref7.base), obj = ref6.value;
          } else {
            if (obj.base instanceof Parens) {
              ref8 = new Value(obj.unwrapAll()).cacheReference(o), obj = ref8[0], idx = ref8[1];
            } else {
              idx = obj["this"] ? obj.properties[0].name : obj;
            }
          }
        }
        if (!expandedIdx && obj instanceof Splat) {
          name = obj.name.unwrap().value;
          obj = obj.unwrap();
          val = olen + " <= " + vvarText + ".length ? " + (utility('slice', o)) + ".call(" + vvarText + ", " + i;
          if (rest = olen - i - 1) {
            ivar = o.scope.freeVariable('i', {
              single: true
            });
            val += ", " + ivar + " = " + vvarText + ".length - " + rest + ") : (" + ivar + " = " + i + ", [])";
          } else {
            val += ") : []";
          }
          val = new Literal(val);
          expandedIdx = ivar + "++";
        } else if (!expandedIdx && obj instanceof Expansion) {
          if (rest = olen - i - 1) {
            if (rest === 1) {
              expandedIdx = vvarText + ".length - 1";
            } else {
              ivar = o.scope.freeVariable('i', {
                single: true
              });
              val = new Literal(ivar + " = " + vvarText + ".length - " + rest);
              expandedIdx = ivar + "++";
              assigns.push(val.compileToFragments(o, LEVEL_LIST));
            }
          }
          continue;
        } else {
          name = obj.unwrap().value;
          if (obj instanceof Splat || obj instanceof Expansion) {
            obj.error("multiple splats/expansions are disallowed in an assignment");
          }
          if (typeof idx === 'number') {
            idx = new Literal(expandedIdx || idx);
            acc = false;
          } else {
            acc = isObject && IDENTIFIER.test(idx.unwrap().value || 0);
          }
          val = new Value(new Literal(vvarText), [new (acc ? Access : Index)(idx)]);
        }
        if ((name != null) && indexOf.call(RESERVED, name) >= 0) {
          obj.error("assignment to a reserved word: " + (obj.compile(o)));
        }
        assigns.push(new Assign(obj, val, null, {
          param: this.param,
          subpattern: true
        }).compileToFragments(o, LEVEL_LIST));
      }
      if (!(top || this.subpattern)) {
        assigns.push(vvar);
      }
      fragments = this.joinFragmentArrays(assigns, ', ');
      if (o.level < LEVEL_LIST) {
        return fragments;
      } else {
        return this.wrapInBraces(fragments);
      }
    };

    Assign.prototype.compileConditional = function(o) {
      var fragments, left, ref3, right;
      ref3 = this.variable.cacheReference(o), left = ref3[0], right = ref3[1];
      if (!left.properties.length && left.base instanceof Literal && left.base.value !== "this" && !o.scope.check(left.base.value)) {
        this.variable.error("the variable \"" + left.base.value + "\" can't be assigned with " + this.context + " because it has not been declared before");
      }
      if (indexOf.call(this.context, "?") >= 0) {
        o.isExistentialEquals = true;
        return new If(new Existence(left), right, {
          type: 'if'
        }).addElse(new Assign(right, this.value, '=')).compileToFragments(o);
      } else {
        fragments = new Op(this.context.slice(0, -1), left, new Assign(right, this.value, '=')).compileToFragments(o);
        if (o.level <= LEVEL_LIST) {
          return fragments;
        } else {
          return this.wrapInBraces(fragments);
        }
      }
    };

    Assign.prototype.compileSpecialMath = function(o) {
      var left, ref3, right;
      ref3 = this.variable.cacheReference(o), left = ref3[0], right = ref3[1];
      return new Assign(left, new Op(this.context.slice(0, -1), right, this.value)).compileToFragments(o);
    };

    Assign.prototype.compileSplice = function(o) {
      var answer, exclusive, from, fromDecl, fromRef, name, ref3, ref4, ref5, to, valDef, valRef;
      ref3 = this.variable.properties.pop().range, from = ref3.from, to = ref3.to, exclusive = ref3.exclusive;
      name = this.variable.compile(o);
      if (from) {
        ref4 = this.cacheToCodeFragments(from.cache(o, LEVEL_OP)), fromDecl = ref4[0], fromRef = ref4[1];
      } else {
        fromDecl = fromRef = '0';
      }
      if (to) {
        if (from instanceof Value && from.isSimpleNumber() && to instanceof Value && to.isSimpleNumber()) {
          to = to.compile(o) - fromRef;
          if (!exclusive) {
            to += 1;
          }
        } else {
          to = to.compile(o, LEVEL_ACCESS) + ' - ' + fromRef;
          if (!exclusive) {
            to += ' + 1';
          }
        }
      } else {
        to = "9e9";
      }
      ref5 = this.value.cache(o, LEVEL_LIST), valDef = ref5[0], valRef = ref5[1];
      answer = [].concat(this.makeCode("[].splice.apply(" + name + ", [" + fromDecl + ", " + to + "].concat("), valDef, this.makeCode(")), "), valRef);
      if (o.level > LEVEL_TOP) {
        return this.wrapInBraces(answer);
      } else {
        return answer;
      }
    };

    return Assign;

  })(Base);

  exports.Code = Code = (function(superClass1) {
    extend1(Code, superClass1);

    function Code(params, body, tag) {
      this.params = params || [];
      this.body = body || new Block;
      this.bound = tag === 'boundfunc';
      this.isGenerator = !!this.body.contains(function(node) {
        var ref3;
        return node instanceof Op && ((ref3 = node.operator) === 'yield' || ref3 === 'yield*');
      });
    }

    Code.prototype.children = ['params', 'body'];

    Code.prototype.isStatement = function() {
      return !!this.ctor;
    };

    Code.prototype.jumps = NO;

    Code.prototype.makeScope = function(parentScope) {
      return new Scope(parentScope, this.body, this);
    };

    Code.prototype.compileNode = function(o) {
      var answer, boundfunc, code, exprs, i, j, k, l, len1, len2, len3, len4, len5, len6, lit, m, p, param, params, q, r, ref, ref3, ref4, ref5, ref6, ref7, ref8, splats, uniqs, val, wasEmpty, wrapper;
      if (this.bound && ((ref3 = o.scope.method) != null ? ref3.bound : void 0)) {
        this.context = o.scope.method.context;
      }
      if (this.bound && !this.context) {
        this.context = '_this';
        wrapper = new Code([new Param(new Literal(this.context))], new Block([this]));
        boundfunc = new Call(wrapper, [new Literal('this')]);
        boundfunc.updateLocationDataIfMissing(this.locationData);
        return boundfunc.compileNode(o);
      }
      o.scope = del(o, 'classScope') || this.makeScope(o.scope);
      o.scope.shared = del(o, 'sharedScope');
      o.indent += TAB;
      delete o.bare;
      delete o.isExistentialEquals;
      params = [];
      exprs = [];
      ref4 = this.params;
      for (j = 0, len1 = ref4.length; j < len1; j++) {
        param = ref4[j];
        if (!(param instanceof Expansion)) {
          o.scope.parameter(param.asReference(o));
        }
      }
      ref5 = this.params;
      for (k = 0, len2 = ref5.length; k < len2; k++) {
        param = ref5[k];
        if (!(param.splat || param instanceof Expansion)) {
          continue;
        }
        ref6 = this.params;
        for (l = 0, len3 = ref6.length; l < len3; l++) {
          p = ref6[l];
          if (!(p instanceof Expansion) && p.name.value) {
            o.scope.add(p.name.value, 'var', true);
          }
        }
        splats = new Assign(new Value(new Arr((function() {
          var len4, m, ref7, results;
          ref7 = this.params;
          results = [];
          for (m = 0, len4 = ref7.length; m < len4; m++) {
            p = ref7[m];
            results.push(p.asReference(o));
          }
          return results;
        }).call(this))), new Value(new Literal('arguments')));
        break;
      }
      ref7 = this.params;
      for (m = 0, len4 = ref7.length; m < len4; m++) {
        param = ref7[m];
        if (param.isComplex()) {
          val = ref = param.asReference(o);
          if (param.value) {
            val = new Op('?', ref, param.value);
          }
          exprs.push(new Assign(new Value(param.name), val, '=', {
            param: true
          }));
        } else {
          ref = param;
          if (param.value) {
            lit = new Literal(ref.name.value + ' == null');
            val = new Assign(new Value(param.name), param.value, '=');
            exprs.push(new If(lit, val));
          }
        }
        if (!splats) {
          params.push(ref);
        }
      }
      wasEmpty = this.body.isEmpty();
      if (splats) {
        exprs.unshift(splats);
      }
      if (exprs.length) {
        (ref8 = this.body.expressions).unshift.apply(ref8, exprs);
      }
      for (i = q = 0, len5 = params.length; q < len5; i = ++q) {
        p = params[i];
        params[i] = p.compileToFragments(o);
        o.scope.parameter(fragmentsToText(params[i]));
      }
      uniqs = [];
      this.eachParamName(function(name, node) {
        if (indexOf.call(uniqs, name) >= 0) {
          node.error("multiple parameters named " + name);
        }
        return uniqs.push(name);
      });
      if (!(wasEmpty || this.noReturn)) {
        this.body.makeReturn();
      }
      code = 'function';
      if (this.isGenerator) {
        code += '*';
      }
      if (this.ctor) {
        code += ' ' + this.name;
      }
      code += '(';
      answer = [this.makeCode(code)];
      for (i = r = 0, len6 = params.length; r < len6; i = ++r) {
        p = params[i];
        if (i) {
          answer.push(this.makeCode(", "));
        }
        answer.push.apply(answer, p);
      }
      answer.push(this.makeCode(') {'));
      if (!this.body.isEmpty()) {
        answer = answer.concat(this.makeCode("\n"), this.body.compileWithDeclarations(o), this.makeCode("\n" + this.tab));
      }
      answer.push(this.makeCode('}'));
      if (this.ctor) {
        return [this.makeCode(this.tab)].concat(slice.call(answer));
      }
      if (this.front || (o.level >= LEVEL_ACCESS)) {
        return this.wrapInBraces(answer);
      } else {
        return answer;
      }
    };

    Code.prototype.eachParamName = function(iterator) {
      var j, len1, param, ref3, results;
      ref3 = this.params;
      results = [];
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        param = ref3[j];
        results.push(param.eachName(iterator));
      }
      return results;
    };

    Code.prototype.traverseChildren = function(crossScope, func) {
      if (crossScope) {
        return Code.__super__.traverseChildren.call(this, crossScope, func);
      }
    };

    return Code;

  })(Base);

  exports.Param = Param = (function(superClass1) {
    extend1(Param, superClass1);

    function Param(name1, value1, splat) {
      var name, ref3;
      this.name = name1;
      this.value = value1;
      this.splat = splat;
      if (ref3 = (name = this.name.unwrapAll().value), indexOf.call(STRICT_PROSCRIBED, ref3) >= 0) {
        this.name.error("parameter name \"" + name + "\" is not allowed");
      }
    }

    Param.prototype.children = ['name', 'value'];

    Param.prototype.compileToFragments = function(o) {
      return this.name.compileToFragments(o, LEVEL_LIST);
    };

    Param.prototype.asReference = function(o) {
      var name, node;
      if (this.reference) {
        return this.reference;
      }
      node = this.name;
      if (node["this"]) {
        name = node.properties[0].name.value;
        if (name.reserved) {
          name = "_" + name;
        }
        node = new Literal(o.scope.freeVariable(name));
      } else if (node.isComplex()) {
        node = new Literal(o.scope.freeVariable('arg'));
      }
      node = new Value(node);
      if (this.splat) {
        node = new Splat(node);
      }
      node.updateLocationDataIfMissing(this.locationData);
      return this.reference = node;
    };

    Param.prototype.isComplex = function() {
      return this.name.isComplex();
    };

    Param.prototype.eachName = function(iterator, name) {
      var atParam, j, len1, node, obj, ref3;
      if (name == null) {
        name = this.name;
      }
      atParam = function(obj) {
        return iterator("@" + obj.properties[0].name.value, obj);
      };
      if (name instanceof Literal) {
        return iterator(name.value, name);
      }
      if (name instanceof Value) {
        return atParam(name);
      }
      ref3 = name.objects;
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        obj = ref3[j];
        if (obj instanceof Assign) {
          this.eachName(iterator, obj.value.unwrap());
        } else if (obj instanceof Splat) {
          node = obj.name.unwrap();
          iterator(node.value, node);
        } else if (obj instanceof Value) {
          if (obj.isArray() || obj.isObject()) {
            this.eachName(iterator, obj.base);
          } else if (obj["this"]) {
            atParam(obj);
          } else {
            iterator(obj.base.value, obj.base);
          }
        } else if (!(obj instanceof Expansion)) {
          obj.error("illegal parameter " + (obj.compile()));
        }
      }
    };

    return Param;

  })(Base);

  exports.Splat = Splat = (function(superClass1) {
    extend1(Splat, superClass1);

    Splat.prototype.children = ['name'];

    Splat.prototype.isAssignable = YES;

    function Splat(name) {
      this.name = name.compile ? name : new Literal(name);
    }

    Splat.prototype.assigns = function(name) {
      return this.name.assigns(name);
    };

    Splat.prototype.compileToFragments = function(o) {
      return this.name.compileToFragments(o);
    };

    Splat.prototype.unwrap = function() {
      return this.name;
    };

    Splat.compileSplattedArray = function(o, list, apply) {
      var args, base, compiledNode, concatPart, fragments, i, index, j, last, len1, node;
      index = -1;
      while ((node = list[++index]) && !(node instanceof Splat)) {
        continue;
      }
      if (index >= list.length) {
        return [];
      }
      if (list.length === 1) {
        node = list[0];
        fragments = node.compileToFragments(o, LEVEL_LIST);
        if (apply) {
          return fragments;
        }
        return [].concat(node.makeCode((utility('slice', o)) + ".call("), fragments, node.makeCode(")"));
      }
      args = list.slice(index);
      for (i = j = 0, len1 = args.length; j < len1; i = ++j) {
        node = args[i];
        compiledNode = node.compileToFragments(o, LEVEL_LIST);
        args[i] = node instanceof Splat ? [].concat(node.makeCode((utility('slice', o)) + ".call("), compiledNode, node.makeCode(")")) : [].concat(node.makeCode("["), compiledNode, node.makeCode("]"));
      }
      if (index === 0) {
        node = list[0];
        concatPart = node.joinFragmentArrays(args.slice(1), ', ');
        return args[0].concat(node.makeCode(".concat("), concatPart, node.makeCode(")"));
      }
      base = (function() {
        var k, len2, ref3, results;
        ref3 = list.slice(0, index);
        results = [];
        for (k = 0, len2 = ref3.length; k < len2; k++) {
          node = ref3[k];
          results.push(node.compileToFragments(o, LEVEL_LIST));
        }
        return results;
      })();
      base = list[0].joinFragmentArrays(base, ', ');
      concatPart = list[index].joinFragmentArrays(args, ', ');
      last = list[list.length - 1];
      return [].concat(list[0].makeCode("["), base, list[index].makeCode("].concat("), concatPart, last.makeCode(")"));
    };

    return Splat;

  })(Base);

  exports.Expansion = Expansion = (function(superClass1) {
    extend1(Expansion, superClass1);

    function Expansion() {
      return Expansion.__super__.constructor.apply(this, arguments);
    }

    Expansion.prototype.isComplex = NO;

    Expansion.prototype.compileNode = function(o) {
      return this.error('Expansion must be used inside a destructuring assignment or parameter list');
    };

    Expansion.prototype.asReference = function(o) {
      return this;
    };

    Expansion.prototype.eachName = function(iterator) {};

    return Expansion;

  })(Base);

  exports.While = While = (function(superClass1) {
    extend1(While, superClass1);

    function While(condition, options) {
      this.condition = (options != null ? options.invert : void 0) ? condition.invert() : condition;
      this.guard = options != null ? options.guard : void 0;
    }

    While.prototype.children = ['condition', 'guard', 'body'];

    While.prototype.isStatement = YES;

    While.prototype.makeReturn = function(res) {
      if (res) {
        return While.__super__.makeReturn.apply(this, arguments);
      } else {
        this.returns = !this.jumps({
          loop: true
        });
        return this;
      }
    };

    While.prototype.addBody = function(body1) {
      this.body = body1;
      return this;
    };

    While.prototype.jumps = function() {
      var expressions, j, jumpNode, len1, node;
      expressions = this.body.expressions;
      if (!expressions.length) {
        return false;
      }
      for (j = 0, len1 = expressions.length; j < len1; j++) {
        node = expressions[j];
        if (jumpNode = node.jumps({
          loop: true
        })) {
          return jumpNode;
        }
      }
      return false;
    };

    While.prototype.compileNode = function(o) {
      var answer, body, rvar, set;
      o.indent += TAB;
      set = '';
      body = this.body;
      if (body.isEmpty()) {
        body = this.makeCode('');
      } else {
        if (this.returns) {
          body.makeReturn(rvar = o.scope.freeVariable('results'));
          set = "" + this.tab + rvar + " = [];\n";
        }
        if (this.guard) {
          if (body.expressions.length > 1) {
            body.expressions.unshift(new If((new Parens(this.guard)).invert(), new Literal("continue")));
          } else {
            if (this.guard) {
              body = Block.wrap([new If(this.guard, body)]);
            }
          }
        }
        body = [].concat(this.makeCode("\n"), body.compileToFragments(o, LEVEL_TOP), this.makeCode("\n" + this.tab));
      }
      answer = [].concat(this.makeCode(set + this.tab + "while ("), this.condition.compileToFragments(o, LEVEL_PAREN), this.makeCode(") {"), body, this.makeCode("}"));
      if (this.returns) {
        answer.push(this.makeCode("\n" + this.tab + "return " + rvar + ";"));
      }
      return answer;
    };

    return While;

  })(Base);

  exports.Op = Op = (function(superClass1) {
    var CONVERSIONS, INVERSIONS;

    extend1(Op, superClass1);

    function Op(op, first, second, flip) {
      if (op === 'in') {
        return new In(first, second);
      }
      if (op === 'do') {
        return this.generateDo(first);
      }
      if (op === 'new') {
        if (first instanceof Call && !first["do"] && !first.isNew) {
          return first.newInstance();
        }
        if (first instanceof Code && first.bound || first["do"]) {
          first = new Parens(first);
        }
      }
      this.operator = CONVERSIONS[op] || op;
      this.first = first;
      this.second = second;
      this.flip = !!flip;
      return this;
    }

    CONVERSIONS = {
      '==': '===',
      '!=': '!==',
      'of': 'in',
      'yieldfrom': 'yield*'
    };

    INVERSIONS = {
      '!==': '===',
      '===': '!=='
    };

    Op.prototype.children = ['first', 'second'];

    Op.prototype.isSimpleNumber = NO;

    Op.prototype.isYield = function() {
      var ref3;
      return (ref3 = this.operator) === 'yield' || ref3 === 'yield*';
    };

    Op.prototype.isYieldReturn = function() {
      return this.isYield() && this.first instanceof Return;
    };

    Op.prototype.isUnary = function() {
      return !this.second;
    };

    Op.prototype.isComplex = function() {
      var ref3;
      return !(this.isUnary() && ((ref3 = this.operator) === '+' || ref3 === '-') && this.first instanceof Value && this.first.isSimpleNumber());
    };

    Op.prototype.isChainable = function() {
      var ref3;
      return (ref3 = this.operator) === '<' || ref3 === '>' || ref3 === '>=' || ref3 === '<=' || ref3 === '===' || ref3 === '!==';
    };

    Op.prototype.invert = function() {
      var allInvertable, curr, fst, op, ref3;
      if (this.isChainable() && this.first.isChainable()) {
        allInvertable = true;
        curr = this;
        while (curr && curr.operator) {
          allInvertable && (allInvertable = curr.operator in INVERSIONS);
          curr = curr.first;
        }
        if (!allInvertable) {
          return new Parens(this).invert();
        }
        curr = this;
        while (curr && curr.operator) {
          curr.invert = !curr.invert;
          curr.operator = INVERSIONS[curr.operator];
          curr = curr.first;
        }
        return this;
      } else if (op = INVERSIONS[this.operator]) {
        this.operator = op;
        if (this.first.unwrap() instanceof Op) {
          this.first.invert();
        }
        return this;
      } else if (this.second) {
        return new Parens(this).invert();
      } else if (this.operator === '!' && (fst = this.first.unwrap()) instanceof Op && ((ref3 = fst.operator) === '!' || ref3 === 'in' || ref3 === 'instanceof')) {
        return fst;
      } else {
        return new Op('!', this);
      }
    };

    Op.prototype.unfoldSoak = function(o) {
      var ref3;
      return ((ref3 = this.operator) === '++' || ref3 === '--' || ref3 === 'delete') && unfoldSoak(o, this, 'first');
    };

    Op.prototype.generateDo = function(exp) {
      var call, func, j, len1, param, passedParams, ref, ref3;
      passedParams = [];
      func = exp instanceof Assign && (ref = exp.value.unwrap()) instanceof Code ? ref : exp;
      ref3 = func.params || [];
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        param = ref3[j];
        if (param.value) {
          passedParams.push(param.value);
          delete param.value;
        } else {
          passedParams.push(param);
        }
      }
      call = new Call(exp, passedParams);
      call["do"] = true;
      return call;
    };

    Op.prototype.compileNode = function(o) {
      var answer, isChain, lhs, ref3, ref4, rhs;
      isChain = this.isChainable() && this.first.isChainable();
      if (!isChain) {
        this.first.front = this.front;
      }
      if (this.operator === 'delete' && o.scope.check(this.first.unwrapAll().value)) {
        this.error('delete operand may not be argument or var');
      }
      if (((ref3 = this.operator) === '--' || ref3 === '++') && (ref4 = this.first.unwrapAll().value, indexOf.call(STRICT_PROSCRIBED, ref4) >= 0)) {
        this.error("cannot increment/decrement \"" + (this.first.unwrapAll().value) + "\"");
      }
      if (this.isYield()) {
        return this.compileYield(o);
      }
      if (this.isUnary()) {
        return this.compileUnary(o);
      }
      if (isChain) {
        return this.compileChain(o);
      }
      switch (this.operator) {
        case '?':
          return this.compileExistence(o);
        case '**':
          return this.compilePower(o);
        case '//':
          return this.compileFloorDivision(o);
        case '%%':
          return this.compileModulo(o);
        default:
          lhs = this.first.compileToFragments(o, LEVEL_OP);
          rhs = this.second.compileToFragments(o, LEVEL_OP);
          answer = [].concat(lhs, this.makeCode(" " + this.operator + " "), rhs);
          if (o.level <= LEVEL_OP) {
            return answer;
          } else {
            return this.wrapInBraces(answer);
          }
      }
    };

    Op.prototype.compileChain = function(o) {
      var fragments, fst, ref3, shared;
      ref3 = this.first.second.cache(o), this.first.second = ref3[0], shared = ref3[1];
      fst = this.first.compileToFragments(o, LEVEL_OP);
      fragments = fst.concat(this.makeCode(" " + (this.invert ? '&&' : '||') + " "), shared.compileToFragments(o), this.makeCode(" " + this.operator + " "), this.second.compileToFragments(o, LEVEL_OP));
      return this.wrapInBraces(fragments);
    };

    Op.prototype.compileExistence = function(o) {
      var fst, ref;
      if (this.first.isComplex()) {
        ref = new Literal(o.scope.freeVariable('ref'));
        fst = new Parens(new Assign(ref, this.first));
      } else {
        fst = this.first;
        ref = fst;
      }
      return new If(new Existence(fst), ref, {
        type: 'if'
      }).addElse(this.second).compileToFragments(o);
    };

    Op.prototype.compileUnary = function(o) {
      var op, parts, plusMinus;
      parts = [];
      op = this.operator;
      parts.push([this.makeCode(op)]);
      if (op === '!' && this.first instanceof Existence) {
        this.first.negated = !this.first.negated;
        return this.first.compileToFragments(o);
      }
      if (o.level >= LEVEL_ACCESS) {
        return (new Parens(this)).compileToFragments(o);
      }
      plusMinus = op === '+' || op === '-';
      if ((op === 'new' || op === 'typeof' || op === 'delete') || plusMinus && this.first instanceof Op && this.first.operator === op) {
        parts.push([this.makeCode(' ')]);
      }
      if ((plusMinus && this.first instanceof Op) || (op === 'new' && this.first.isStatement(o))) {
        this.first = new Parens(this.first);
      }
      parts.push(this.first.compileToFragments(o, LEVEL_OP));
      if (this.flip) {
        parts.reverse();
      }
      return this.joinFragmentArrays(parts, '');
    };

    Op.prototype.compileYield = function(o) {
      var op, parts;
      parts = [];
      op = this.operator;
      if (o.scope.parent == null) {
        this.error('yield statements must occur within a function generator.');
      }
      if (indexOf.call(Object.keys(this.first), 'expression') >= 0 && !(this.first instanceof Throw)) {
        if (this.isYieldReturn()) {
          parts.push(this.first.compileToFragments(o, LEVEL_TOP));
        } else if (this.first.expression != null) {
          parts.push(this.first.expression.compileToFragments(o, LEVEL_OP));
        }
      } else {
        parts.push([this.makeCode("(" + op + " ")]);
        parts.push(this.first.compileToFragments(o, LEVEL_OP));
        parts.push([this.makeCode(")")]);
      }
      return this.joinFragmentArrays(parts, '');
    };

    Op.prototype.compilePower = function(o) {
      var pow;
      pow = new Value(new Literal('Math'), [new Access(new Literal('pow'))]);
      return new Call(pow, [this.first, this.second]).compileToFragments(o);
    };

    Op.prototype.compileFloorDivision = function(o) {
      var div, floor;
      floor = new Value(new Literal('Math'), [new Access(new Literal('floor'))]);
      div = new Op('/', this.first, this.second);
      return new Call(floor, [div]).compileToFragments(o);
    };

    Op.prototype.compileModulo = function(o) {
      var mod;
      mod = new Value(new Literal(utility('modulo', o)));
      return new Call(mod, [this.first, this.second]).compileToFragments(o);
    };

    Op.prototype.toString = function(idt) {
      return Op.__super__.toString.call(this, idt, this.constructor.name + ' ' + this.operator);
    };

    return Op;

  })(Base);

  exports.In = In = (function(superClass1) {
    extend1(In, superClass1);

    function In(object, array) {
      this.object = object;
      this.array = array;
    }

    In.prototype.children = ['object', 'array'];

    In.prototype.invert = NEGATE;

    In.prototype.compileNode = function(o) {
      var hasSplat, j, len1, obj, ref3;
      if (this.array instanceof Value && this.array.isArray() && this.array.base.objects.length) {
        ref3 = this.array.base.objects;
        for (j = 0, len1 = ref3.length; j < len1; j++) {
          obj = ref3[j];
          if (!(obj instanceof Splat)) {
            continue;
          }
          hasSplat = true;
          break;
        }
        if (!hasSplat) {
          return this.compileOrTest(o);
        }
      }
      return this.compileLoopTest(o);
    };

    In.prototype.compileOrTest = function(o) {
      var cmp, cnj, i, item, j, len1, ref, ref3, ref4, ref5, sub, tests;
      ref3 = this.object.cache(o, LEVEL_OP), sub = ref3[0], ref = ref3[1];
      ref4 = this.negated ? [' !== ', ' && '] : [' === ', ' || '], cmp = ref4[0], cnj = ref4[1];
      tests = [];
      ref5 = this.array.base.objects;
      for (i = j = 0, len1 = ref5.length; j < len1; i = ++j) {
        item = ref5[i];
        if (i) {
          tests.push(this.makeCode(cnj));
        }
        tests = tests.concat((i ? ref : sub), this.makeCode(cmp), item.compileToFragments(o, LEVEL_ACCESS));
      }
      if (o.level < LEVEL_OP) {
        return tests;
      } else {
        return this.wrapInBraces(tests);
      }
    };

    In.prototype.compileLoopTest = function(o) {
      var fragments, ref, ref3, sub;
      ref3 = this.object.cache(o, LEVEL_LIST), sub = ref3[0], ref = ref3[1];
      fragments = [].concat(this.makeCode(utility('indexOf', o) + ".call("), this.array.compileToFragments(o, LEVEL_LIST), this.makeCode(", "), ref, this.makeCode(") " + (this.negated ? '< 0' : '>= 0')));
      if (fragmentsToText(sub) === fragmentsToText(ref)) {
        return fragments;
      }
      fragments = sub.concat(this.makeCode(', '), fragments);
      if (o.level < LEVEL_LIST) {
        return fragments;
      } else {
        return this.wrapInBraces(fragments);
      }
    };

    In.prototype.toString = function(idt) {
      return In.__super__.toString.call(this, idt, this.constructor.name + (this.negated ? '!' : ''));
    };

    return In;

  })(Base);

  exports.Try = Try = (function(superClass1) {
    extend1(Try, superClass1);

    function Try(attempt, errorVariable, recovery, ensure) {
      this.attempt = attempt;
      this.errorVariable = errorVariable;
      this.recovery = recovery;
      this.ensure = ensure;
    }

    Try.prototype.children = ['attempt', 'recovery', 'ensure'];

    Try.prototype.isStatement = YES;

    Try.prototype.jumps = function(o) {
      var ref3;
      return this.attempt.jumps(o) || ((ref3 = this.recovery) != null ? ref3.jumps(o) : void 0);
    };

    Try.prototype.makeReturn = function(res) {
      if (this.attempt) {
        this.attempt = this.attempt.makeReturn(res);
      }
      if (this.recovery) {
        this.recovery = this.recovery.makeReturn(res);
      }
      return this;
    };

    Try.prototype.compileNode = function(o) {
      var catchPart, ensurePart, placeholder, tryPart;
      o.indent += TAB;
      tryPart = this.attempt.compileToFragments(o, LEVEL_TOP);
      catchPart = this.recovery ? (placeholder = new Literal('_error'), this.errorVariable ? this.recovery.unshift(new Assign(this.errorVariable, placeholder)) : void 0, [].concat(this.makeCode(" catch ("), placeholder.compileToFragments(o), this.makeCode(") {\n"), this.recovery.compileToFragments(o, LEVEL_TOP), this.makeCode("\n" + this.tab + "}"))) : !(this.ensure || this.recovery) ? [this.makeCode(' catch (_error) {}')] : [];
      ensurePart = this.ensure ? [].concat(this.makeCode(" finally {\n"), this.ensure.compileToFragments(o, LEVEL_TOP), this.makeCode("\n" + this.tab + "}")) : [];
      return [].concat(this.makeCode(this.tab + "try {\n"), tryPart, this.makeCode("\n" + this.tab + "}"), catchPart, ensurePart);
    };

    return Try;

  })(Base);

  exports.Throw = Throw = (function(superClass1) {
    extend1(Throw, superClass1);

    function Throw(expression) {
      this.expression = expression;
    }

    Throw.prototype.children = ['expression'];

    Throw.prototype.isStatement = YES;

    Throw.prototype.jumps = NO;

    Throw.prototype.makeReturn = THIS;

    Throw.prototype.compileNode = function(o) {
      return [].concat(this.makeCode(this.tab + "throw "), this.expression.compileToFragments(o), this.makeCode(";"));
    };

    return Throw;

  })(Base);

  exports.Existence = Existence = (function(superClass1) {
    extend1(Existence, superClass1);

    function Existence(expression) {
      this.expression = expression;
    }

    Existence.prototype.children = ['expression'];

    Existence.prototype.invert = NEGATE;

    Existence.prototype.compileNode = function(o) {
      var cmp, cnj, code, ref3;
      this.expression.front = this.front;
      code = this.expression.compile(o, LEVEL_OP);
      if (IDENTIFIER.test(code) && !o.scope.check(code)) {
        ref3 = this.negated ? ['===', '||'] : ['!==', '&&'], cmp = ref3[0], cnj = ref3[1];
        code = "typeof " + code + " " + cmp + " \"undefined\" " + cnj + " " + code + " " + cmp + " null";
      } else {
        code = code + " " + (this.negated ? '==' : '!=') + " null";
      }
      return [this.makeCode(o.level <= LEVEL_COND ? code : "(" + code + ")")];
    };

    return Existence;

  })(Base);

  exports.Parens = Parens = (function(superClass1) {
    extend1(Parens, superClass1);

    function Parens(body1) {
      this.body = body1;
    }

    Parens.prototype.children = ['body'];

    Parens.prototype.unwrap = function() {
      return this.body;
    };

    Parens.prototype.isComplex = function() {
      return this.body.isComplex();
    };

    Parens.prototype.compileNode = function(o) {
      var bare, expr, fragments;
      expr = this.body.unwrap();
      if (expr instanceof Value && expr.isAtomic()) {
        expr.front = this.front;
        return expr.compileToFragments(o);
      }
      fragments = expr.compileToFragments(o, LEVEL_PAREN);
      bare = o.level < LEVEL_OP && (expr instanceof Op || expr instanceof Call || (expr instanceof For && expr.returns));
      if (bare) {
        return fragments;
      } else {
        return this.wrapInBraces(fragments);
      }
    };

    return Parens;

  })(Base);

  exports.For = For = (function(superClass1) {
    extend1(For, superClass1);

    function For(body, source) {
      var ref3;
      this.source = source.source, this.guard = source.guard, this.step = source.step, this.name = source.name, this.index = source.index;
      this.body = Block.wrap([body]);
      this.own = !!source.own;
      this.object = !!source.object;
      if (this.object) {
        ref3 = [this.index, this.name], this.name = ref3[0], this.index = ref3[1];
      }
      if (this.index instanceof Value) {
        this.index.error('index cannot be a pattern matching expression');
      }
      this.range = this.source instanceof Value && this.source.base instanceof Range && !this.source.properties.length;
      this.pattern = this.name instanceof Value;
      if (this.range && this.index) {
        this.index.error('indexes do not apply to range loops');
      }
      if (this.range && this.pattern) {
        this.name.error('cannot pattern match over range loops');
      }
      if (this.own && !this.object) {
        this.name.error('cannot use own with for-in');
      }
      this.returns = false;
    }

    For.prototype.children = ['body', 'source', 'guard', 'step'];

    For.prototype.compileNode = function(o) {
      var body, bodyFragments, compare, compareDown, declare, declareDown, defPart, defPartFragments, down, forPartFragments, guardPart, idt1, increment, index, ivar, kvar, kvarAssign, last, lvar, name, namePart, ref, ref3, ref4, resultPart, returnResult, rvar, scope, source, step, stepNum, stepVar, svar, varPart;
      body = Block.wrap([this.body]);
      ref3 = body.expressions, last = ref3[ref3.length - 1];
      if ((last != null ? last.jumps() : void 0) instanceof Return) {
        this.returns = false;
      }
      source = this.range ? this.source.base : this.source;
      scope = o.scope;
      if (!this.pattern) {
        name = this.name && (this.name.compile(o, LEVEL_LIST));
      }
      index = this.index && (this.index.compile(o, LEVEL_LIST));
      if (name && !this.pattern) {
        scope.find(name);
      }
      if (index) {
        scope.find(index);
      }
      if (this.returns) {
        rvar = scope.freeVariable('results');
      }
      ivar = (this.object && index) || scope.freeVariable('i', {
        single: true
      });
      kvar = (this.range && name) || index || ivar;
      kvarAssign = kvar !== ivar ? kvar + " = " : "";
      if (this.step && !this.range) {
        ref4 = this.cacheToCodeFragments(this.step.cache(o, LEVEL_LIST, isComplexOrAssignable)), step = ref4[0], stepVar = ref4[1];
        stepNum = stepVar.match(NUMBER);
      }
      if (this.pattern) {
        name = ivar;
      }
      varPart = '';
      guardPart = '';
      defPart = '';
      idt1 = this.tab + TAB;
      if (this.range) {
        forPartFragments = source.compileToFragments(merge(o, {
          index: ivar,
          name: name,
          step: this.step,
          isComplex: isComplexOrAssignable
        }));
      } else {
        svar = this.source.compile(o, LEVEL_LIST);
        if ((name || this.own) && !IDENTIFIER.test(svar)) {
          defPart += "" + this.tab + (ref = scope.freeVariable('ref')) + " = " + svar + ";\n";
          svar = ref;
        }
        if (name && !this.pattern) {
          namePart = name + " = " + svar + "[" + kvar + "]";
        }
        if (!this.object) {
          if (step !== stepVar) {
            defPart += "" + this.tab + step + ";\n";
          }
          if (!(this.step && stepNum && (down = parseNum(stepNum[0]) < 0))) {
            lvar = scope.freeVariable('len');
          }
          declare = "" + kvarAssign + ivar + " = 0, " + lvar + " = " + svar + ".length";
          declareDown = "" + kvarAssign + ivar + " = " + svar + ".length - 1";
          compare = ivar + " < " + lvar;
          compareDown = ivar + " >= 0";
          if (this.step) {
            if (stepNum) {
              if (down) {
                compare = compareDown;
                declare = declareDown;
              }
            } else {
              compare = stepVar + " > 0 ? " + compare + " : " + compareDown;
              declare = "(" + stepVar + " > 0 ? (" + declare + ") : " + declareDown + ")";
            }
            increment = ivar + " += " + stepVar;
          } else {
            increment = "" + (kvar !== ivar ? "++" + ivar : ivar + "++");
          }
          forPartFragments = [this.makeCode(declare + "; " + compare + "; " + kvarAssign + increment)];
        }
      }
      if (this.returns) {
        resultPart = "" + this.tab + rvar + " = [];\n";
        returnResult = "\n" + this.tab + "return " + rvar + ";";
        body.makeReturn(rvar);
      }
      if (this.guard) {
        if (body.expressions.length > 1) {
          body.expressions.unshift(new If((new Parens(this.guard)).invert(), new Literal("continue")));
        } else {
          if (this.guard) {
            body = Block.wrap([new If(this.guard, body)]);
          }
        }
      }
      if (this.pattern) {
        body.expressions.unshift(new Assign(this.name, new Literal(svar + "[" + kvar + "]")));
      }
      defPartFragments = [].concat(this.makeCode(defPart), this.pluckDirectCall(o, body));
      if (namePart) {
        varPart = "\n" + idt1 + namePart + ";";
      }
      if (this.object) {
        forPartFragments = [this.makeCode(kvar + " in " + svar)];
        if (this.own) {
          guardPart = "\n" + idt1 + "if (!" + (utility('hasProp', o)) + ".call(" + svar + ", " + kvar + ")) continue;";
        }
      }
      bodyFragments = body.compileToFragments(merge(o, {
        indent: idt1
      }), LEVEL_TOP);
      if (bodyFragments && (bodyFragments.length > 0)) {
        bodyFragments = [].concat(this.makeCode("\n"), bodyFragments, this.makeCode("\n"));
      }
      return [].concat(defPartFragments, this.makeCode("" + (resultPart || '') + this.tab + "for ("), forPartFragments, this.makeCode(") {" + guardPart + varPart), bodyFragments, this.makeCode(this.tab + "}" + (returnResult || '')));
    };

    For.prototype.pluckDirectCall = function(o, body) {
      var base, defs, expr, fn, idx, j, len1, ref, ref3, ref4, ref5, ref6, ref7, ref8, ref9, val;
      defs = [];
      ref3 = body.expressions;
      for (idx = j = 0, len1 = ref3.length; j < len1; idx = ++j) {
        expr = ref3[idx];
        expr = expr.unwrapAll();
        if (!(expr instanceof Call)) {
          continue;
        }
        val = (ref4 = expr.variable) != null ? ref4.unwrapAll() : void 0;
        if (!((val instanceof Code) || (val instanceof Value && ((ref5 = val.base) != null ? ref5.unwrapAll() : void 0) instanceof Code && val.properties.length === 1 && ((ref6 = (ref7 = val.properties[0].name) != null ? ref7.value : void 0) === 'call' || ref6 === 'apply')))) {
          continue;
        }
        fn = ((ref8 = val.base) != null ? ref8.unwrapAll() : void 0) || val;
        ref = new Literal(o.scope.freeVariable('fn'));
        base = new Value(ref);
        if (val.base) {
          ref9 = [base, val], val.base = ref9[0], base = ref9[1];
        }
        body.expressions[idx] = new Call(base, expr.args);
        defs = defs.concat(this.makeCode(this.tab), new Assign(ref, fn).compileToFragments(o, LEVEL_TOP), this.makeCode(';\n'));
      }
      return defs;
    };

    return For;

  })(While);

  exports.Switch = Switch = (function(superClass1) {
    extend1(Switch, superClass1);

    function Switch(subject, cases, otherwise) {
      this.subject = subject;
      this.cases = cases;
      this.otherwise = otherwise;
    }

    Switch.prototype.children = ['subject', 'cases', 'otherwise'];

    Switch.prototype.isStatement = YES;

    Switch.prototype.jumps = function(o) {
      var block, conds, j, jumpNode, len1, ref3, ref4, ref5;
      if (o == null) {
        o = {
          block: true
        };
      }
      ref3 = this.cases;
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        ref4 = ref3[j], conds = ref4[0], block = ref4[1];
        if (jumpNode = block.jumps(o)) {
          return jumpNode;
        }
      }
      return (ref5 = this.otherwise) != null ? ref5.jumps(o) : void 0;
    };

    Switch.prototype.makeReturn = function(res) {
      var j, len1, pair, ref3, ref4;
      ref3 = this.cases;
      for (j = 0, len1 = ref3.length; j < len1; j++) {
        pair = ref3[j];
        pair[1].makeReturn(res);
      }
      if (res) {
        this.otherwise || (this.otherwise = new Block([new Literal('void 0')]));
      }
      if ((ref4 = this.otherwise) != null) {
        ref4.makeReturn(res);
      }
      return this;
    };

    Switch.prototype.compileNode = function(o) {
      var block, body, cond, conditions, expr, fragments, i, idt1, idt2, j, k, len1, len2, ref3, ref4, ref5;
      idt1 = o.indent + TAB;
      idt2 = o.indent = idt1 + TAB;
      fragments = [].concat(this.makeCode(this.tab + "switch ("), (this.subject ? this.subject.compileToFragments(o, LEVEL_PAREN) : this.makeCode("false")), this.makeCode(") {\n"));
      ref3 = this.cases;
      for (i = j = 0, len1 = ref3.length; j < len1; i = ++j) {
        ref4 = ref3[i], conditions = ref4[0], block = ref4[1];
        ref5 = flatten([conditions]);
        for (k = 0, len2 = ref5.length; k < len2; k++) {
          cond = ref5[k];
          if (!this.subject) {
            cond = cond.invert();
          }
          fragments = fragments.concat(this.makeCode(idt1 + "case "), cond.compileToFragments(o, LEVEL_PAREN), this.makeCode(":\n"));
        }
        if ((body = block.compileToFragments(o, LEVEL_TOP)).length > 0) {
          fragments = fragments.concat(body, this.makeCode('\n'));
        }
        if (i === this.cases.length - 1 && !this.otherwise) {
          break;
        }
        expr = this.lastNonComment(block.expressions);
        if (expr instanceof Return || (expr instanceof Literal && expr.jumps() && expr.value !== 'debugger')) {
          continue;
        }
        fragments.push(cond.makeCode(idt2 + 'break;\n'));
      }
      if (this.otherwise && this.otherwise.expressions.length) {
        fragments.push.apply(fragments, [this.makeCode(idt1 + "default:\n")].concat(slice.call(this.otherwise.compileToFragments(o, LEVEL_TOP)), [this.makeCode("\n")]));
      }
      fragments.push(this.makeCode(this.tab + '}'));
      return fragments;
    };

    return Switch;

  })(Base);

  exports.If = If = (function(superClass1) {
    extend1(If, superClass1);

    function If(condition, body1, options) {
      this.body = body1;
      if (options == null) {
        options = {};
      }
      this.condition = options.type === 'unless' ? condition.invert() : condition;
      this.elseBody = null;
      this.isChain = false;
      this.soak = options.soak;
    }

    If.prototype.children = ['condition', 'body', 'elseBody'];

    If.prototype.bodyNode = function() {
      var ref3;
      return (ref3 = this.body) != null ? ref3.unwrap() : void 0;
    };

    If.prototype.elseBodyNode = function() {
      var ref3;
      return (ref3 = this.elseBody) != null ? ref3.unwrap() : void 0;
    };

    If.prototype.addElse = function(elseBody) {
      if (this.isChain) {
        this.elseBodyNode().addElse(elseBody);
      } else {
        this.isChain = elseBody instanceof If;
        this.elseBody = this.ensureBlock(elseBody);
        this.elseBody.updateLocationDataIfMissing(elseBody.locationData);
      }
      return this;
    };

    If.prototype.isStatement = function(o) {
      var ref3;
      return (o != null ? o.level : void 0) === LEVEL_TOP || this.bodyNode().isStatement(o) || ((ref3 = this.elseBodyNode()) != null ? ref3.isStatement(o) : void 0);
    };

    If.prototype.jumps = function(o) {
      var ref3;
      return this.body.jumps(o) || ((ref3 = this.elseBody) != null ? ref3.jumps(o) : void 0);
    };

    If.prototype.compileNode = function(o) {
      if (this.isStatement(o)) {
        return this.compileStatement(o);
      } else {
        return this.compileExpression(o);
      }
    };

    If.prototype.makeReturn = function(res) {
      if (res) {
        this.elseBody || (this.elseBody = new Block([new Literal('void 0')]));
      }
      this.body && (this.body = new Block([this.body.makeReturn(res)]));
      this.elseBody && (this.elseBody = new Block([this.elseBody.makeReturn(res)]));
      return this;
    };

    If.prototype.ensureBlock = function(node) {
      if (node instanceof Block) {
        return node;
      } else {
        return new Block([node]);
      }
    };

    If.prototype.compileStatement = function(o) {
      var answer, body, child, cond, exeq, ifPart, indent;
      child = del(o, 'chainChild');
      exeq = del(o, 'isExistentialEquals');
      if (exeq) {
        return new If(this.condition.invert(), this.elseBodyNode(), {
          type: 'if'
        }).compileToFragments(o);
      }
      indent = o.indent + TAB;
      cond = this.condition.compileToFragments(o, LEVEL_PAREN);
      body = this.ensureBlock(this.body).compileToFragments(merge(o, {
        indent: indent
      }));
      ifPart = [].concat(this.makeCode("if ("), cond, this.makeCode(") {\n"), body, this.makeCode("\n" + this.tab + "}"));
      if (!child) {
        ifPart.unshift(this.makeCode(this.tab));
      }
      if (!this.elseBody) {
        return ifPart;
      }
      answer = ifPart.concat(this.makeCode(' else '));
      if (this.isChain) {
        o.chainChild = true;
        answer = answer.concat(this.elseBody.unwrap().compileToFragments(o, LEVEL_TOP));
      } else {
        answer = answer.concat(this.makeCode("{\n"), this.elseBody.compileToFragments(merge(o, {
          indent: indent
        }), LEVEL_TOP), this.makeCode("\n" + this.tab + "}"));
      }
      return answer;
    };

    If.prototype.compileExpression = function(o) {
      var alt, body, cond, fragments;
      cond = this.condition.compileToFragments(o, LEVEL_COND);
      body = this.bodyNode().compileToFragments(o, LEVEL_LIST);
      alt = this.elseBodyNode() ? this.elseBodyNode().compileToFragments(o, LEVEL_LIST) : [this.makeCode('void 0')];
      fragments = cond.concat(this.makeCode(" ? "), body, this.makeCode(" : "), alt);
      if (o.level >= LEVEL_COND) {
        return this.wrapInBraces(fragments);
      } else {
        return fragments;
      }
    };

    If.prototype.unfoldSoak = function() {
      return this.soak && this;
    };

    return If;

  })(Base);

  UTILITIES = {
    extend: function(o) {
      return "function(child, parent) { for (var key in parent) { if (" + (utility('hasProp', o)) + ".call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; }";
    },
    bind: function() {
      return 'function(fn, me){ return function(){ return fn.apply(me, arguments); }; }';
    },
    indexOf: function() {
      return "[].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; }";
    },
    modulo: function() {
      return "function(a, b) { return (+a % (b = +b) + b) % b; }";
    },
    hasProp: function() {
      return '{}.hasOwnProperty';
    },
    slice: function() {
      return '[].slice';
    }
  };

  LEVEL_TOP = 1;

  LEVEL_PAREN = 2;

  LEVEL_LIST = 3;

  LEVEL_COND = 4;

  LEVEL_OP = 5;

  LEVEL_ACCESS = 6;

  TAB = '  ';

  IDENTIFIER = /^(?!\d)[$\w\x7f-\uffff]+$/;

  SIMPLENUM = /^[+-]?\d+$/;

  HEXNUM = /^[+-]?0x[\da-f]+/i;

  NUMBER = /^[+-]?(?:0x[\da-f]+|\d*\.?\d+(?:e[+-]?\d+)?)$/i;

  IS_STRING = /^['"]/;

  IS_REGEX = /^\//;

  utility = function(name, o) {
    var ref, root;
    root = o.scope.root;
    if (name in root.utilities) {
      return root.utilities[name];
    } else {
      ref = root.freeVariable(name);
      root.assign(ref, UTILITIES[name](o));
      return root.utilities[name] = ref;
    }
  };

  multident = function(code, tab) {
    code = code.replace(/\n/g, '$&' + tab);
    return code.replace(/\s+$/, '');
  };

  parseNum = function(x) {
    if (x == null) {
      return 0;
    } else if (x.match(HEXNUM)) {
      return parseInt(x, 16);
    } else {
      return parseFloat(x);
    }
  };

  isLiteralArguments = function(node) {
    return node instanceof Literal && node.value === 'arguments' && !node.asKey;
  };

  isLiteralThis = function(node) {
    return (node instanceof Literal && node.value === 'this' && !node.asKey) || (node instanceof Code && node.bound) || (node instanceof Call && node.isSuper);
  };

  isComplexOrAssignable = function(node) {
    return node.isComplex() || (typeof node.isAssignable === "function" ? node.isAssignable() : void 0);
  };

  unfoldSoak = function(o, parent, name) {
    var ifn;
    if (!(ifn = parent[name].unfoldSoak(o))) {
      return;
    }
    parent[name] = ifn.body;
    ifn.body = new Value(parent);
    return ifn;
  };

}).call(this);

},{"./helpers":21,"./lexer":22,"./scope":27}],24:[function(require,module,exports){
(function (process){
/* parser generated by jison 0.4.15 */
/*
  Returns a Parser object of the following structure:

  Parser: {
    yy: {}
  }

  Parser.prototype: {
    yy: {},
    trace: function(),
    symbols_: {associative list: name ==> number},
    terminals_: {associative list: number ==> name},
    productions_: [...],
    performAction: function anonymous(yytext, yyleng, yylineno, yy, yystate, $$, _$),
    table: [...],
    defaultActions: {...},
    parseError: function(str, hash),
    parse: function(input),

    lexer: {
        EOF: 1,
        parseError: function(str, hash),
        setInput: function(input),
        input: function(),
        unput: function(str),
        more: function(),
        less: function(n),
        pastInput: function(),
        upcomingInput: function(),
        showPosition: function(),
        test_match: function(regex_match_array, rule_index),
        next: function(),
        lex: function(),
        begin: function(condition),
        popState: function(),
        _currentRules: function(),
        topState: function(),
        pushState: function(condition),

        options: {
            ranges: boolean           (optional: true ==> token location info will include a .range[] member)
            flex: boolean             (optional: true ==> flex-like lexing behaviour where the rules are tested exhaustively to find the longest match)
            backtrack_lexer: boolean  (optional: true ==> lexer regexes are tested in order and for each matching regex the action code is invoked; the lexer terminates the scan when a token is returned by the action code)
        },

        performAction: function(yy, yy_, $avoiding_name_collisions, YY_START),
        rules: [...],
        conditions: {associative list: name ==> set},
    }
  }


  token location info (@$, _$, etc.): {
    first_line: n,
    last_line: n,
    first_column: n,
    last_column: n,
    range: [start_number, end_number]       (where the numbers are indexes into the input string, regular zero-based)
  }


  the parseError function receives a 'hash' object with these members for lexer and parser errors: {
    text:        (matched text)
    token:       (the produced terminal token, if any)
    line:        (yylineno)
  }
  while parser (grammar) errors will also provide these members, i.e. parser errors deliver a superset of attributes: {
    loc:         (yylloc)
    expected:    (string describing the set of expected tokens)
    recoverable: (boolean: TRUE when the parser has a error recovery rule available for this particular error)
  }
*/
var parser = (function(){
var o=function(k,v,o,l){for(o=o||{},l=k.length;l--;o[k[l]]=v);return o},$V0=[1,20],$V1=[1,75],$V2=[1,71],$V3=[1,76],$V4=[1,77],$V5=[1,73],$V6=[1,74],$V7=[1,50],$V8=[1,52],$V9=[1,53],$Va=[1,54],$Vb=[1,55],$Vc=[1,45],$Vd=[1,46],$Ve=[1,27],$Vf=[1,60],$Vg=[1,61],$Vh=[1,70],$Vi=[1,43],$Vj=[1,26],$Vk=[1,58],$Vl=[1,59],$Vm=[1,57],$Vn=[1,38],$Vo=[1,44],$Vp=[1,56],$Vq=[1,65],$Vr=[1,66],$Vs=[1,67],$Vt=[1,68],$Vu=[1,42],$Vv=[1,64],$Vw=[1,29],$Vx=[1,30],$Vy=[1,31],$Vz=[1,32],$VA=[1,33],$VB=[1,34],$VC=[1,35],$VD=[1,78],$VE=[1,6,26,34,108],$VF=[1,88],$VG=[1,81],$VH=[1,80],$VI=[1,79],$VJ=[1,82],$VK=[1,83],$VL=[1,84],$VM=[1,85],$VN=[1,86],$VO=[1,87],$VP=[1,91],$VQ=[1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132,135,136,141,142,143,144,145,146,147],$VR=[1,97],$VS=[1,98],$VT=[1,99],$VU=[1,100],$VV=[1,102],$VW=[1,103],$VX=[1,96],$VY=[2,112],$VZ=[1,6,25,26,34,55,60,63,72,73,74,75,77,79,80,84,90,91,92,97,99,108,110,111,112,116,117,132,135,136,141,142,143,144,145,146,147],$V_=[2,79],$V$=[1,108],$V01=[2,58],$V11=[1,112],$V21=[1,117],$V31=[1,118],$V41=[1,120],$V51=[1,6,25,26,34,46,55,60,63,72,73,74,75,77,79,80,84,90,91,92,97,99,108,110,111,112,116,117,132,135,136,141,142,143,144,145,146,147],$V61=[2,76],$V71=[1,6,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132,135,136,141,142,143,144,145,146,147],$V81=[1,155],$V91=[1,157],$Va1=[1,152],$Vb1=[1,6,25,26,34,46,55,60,63,72,73,74,75,77,79,80,84,86,90,91,92,97,99,108,110,111,112,116,117,132,135,136,139,140,141,142,143,144,145,146,147,148],$Vc1=[2,95],$Vd1=[1,6,25,26,34,49,55,60,63,72,73,74,75,77,79,80,84,90,91,92,97,99,108,110,111,112,116,117,132,135,136,141,142,143,144,145,146,147],$Ve1=[1,6,25,26,34,46,49,55,60,63,72,73,74,75,77,79,80,84,86,90,91,92,97,99,108,110,111,112,116,117,123,124,132,135,136,139,140,141,142,143,144,145,146,147,148],$Vf1=[1,206],$Vg1=[1,205],$Vh1=[1,6,25,26,34,38,55,60,63,72,73,74,75,77,79,80,84,90,91,92,97,99,108,110,111,112,116,117,132,135,136,141,142,143,144,145,146,147],$Vi1=[2,56],$Vj1=[1,216],$Vk1=[6,25,26,55,60],$Vl1=[6,25,26,46,55,60,63],$Vm1=[1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132,135,136,142,144,145,146,147],$Vn1=[1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132],$Vo1=[72,73,74,75,77,80,90,91],$Vp1=[1,235],$Vq1=[2,133],$Vr1=[1,6,25,26,34,46,55,60,63,72,73,74,75,77,79,80,84,90,91,92,97,99,108,110,111,112,116,117,123,124,132,135,136,141,142,143,144,145,146,147],$Vs1=[1,244],$Vt1=[6,25,26,60,92,97],$Vu1=[1,6,25,26,34,55,60,63,79,84,92,97,99,108,117,132],$Vv1=[1,6,25,26,34,55,60,63,79,84,92,97,99,108,111,117,132],$Vw1=[123,124],$Vx1=[60,123,124],$Vy1=[1,255],$Vz1=[6,25,26,60,84],$VA1=[6,25,26,49,60,84],$VB1=[1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132,135,136,144,145,146,147],$VC1=[11,28,30,32,33,36,37,40,41,42,43,44,51,52,53,57,58,79,82,85,89,94,95,96,102,106,107,110,112,114,116,125,131,133,134,135,136,137,139,140],$VD1=[2,122],$VE1=[6,25,26],$VF1=[2,57],$VG1=[1,268],$VH1=[1,269],$VI1=[1,6,25,26,34,55,60,63,79,84,92,97,99,104,105,108,110,111,112,116,117,127,129,132,135,136,141,142,143,144,145,146,147],$VJ1=[26,127,129],$VK1=[1,6,26,34,55,60,63,79,84,92,97,99,108,111,117,132],$VL1=[2,71],$VM1=[1,291],$VN1=[1,292],$VO1=[1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,127,132,135,136,141,142,143,144,145,146,147],$VP1=[1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,112,116,117,132],$VQ1=[1,303],$VR1=[1,304],$VS1=[6,25,26,60],$VT1=[1,6,25,26,34,55,60,63,79,84,92,97,99,104,108,110,111,112,116,117,132,135,136,141,142,143,144,145,146,147],$VU1=[25,60];
var parser = {trace: function trace() { },
yy: {},
symbols_: {"error":2,"Root":3,"Body":4,"Line":5,"TERMINATOR":6,"Expression":7,"Statement":8,"Return":9,"Comment":10,"STATEMENT":11,"Value":12,"Invocation":13,"Code":14,"Operation":15,"Assign":16,"If":17,"Try":18,"While":19,"For":20,"Switch":21,"Class":22,"Throw":23,"Block":24,"INDENT":25,"OUTDENT":26,"Identifier":27,"IDENTIFIER":28,"AlphaNumeric":29,"NUMBER":30,"String":31,"STRING":32,"STRING_START":33,"STRING_END":34,"Regex":35,"REGEX":36,"REGEX_START":37,"REGEX_END":38,"Literal":39,"JS":40,"DEBUGGER":41,"UNDEFINED":42,"NULL":43,"BOOL":44,"Assignable":45,"=":46,"AssignObj":47,"ObjAssignable":48,":":49,"ThisProperty":50,"RETURN":51,"HERECOMMENT":52,"PARAM_START":53,"ParamList":54,"PARAM_END":55,"FuncGlyph":56,"->":57,"=>":58,"OptComma":59,",":60,"Param":61,"ParamVar":62,"...":63,"Array":64,"Object":65,"Splat":66,"SimpleAssignable":67,"Accessor":68,"Parenthetical":69,"Range":70,"This":71,".":72,"?.":73,"::":74,"?::":75,"Index":76,"INDEX_START":77,"IndexValue":78,"INDEX_END":79,"INDEX_SOAK":80,"Slice":81,"{":82,"AssignList":83,"}":84,"CLASS":85,"EXTENDS":86,"OptFuncExist":87,"Arguments":88,"SUPER":89,"FUNC_EXIST":90,"CALL_START":91,"CALL_END":92,"ArgList":93,"THIS":94,"@":95,"[":96,"]":97,"RangeDots":98,"..":99,"Arg":100,"SimpleArgs":101,"TRY":102,"Catch":103,"FINALLY":104,"CATCH":105,"THROW":106,"(":107,")":108,"WhileSource":109,"WHILE":110,"WHEN":111,"UNTIL":112,"Loop":113,"LOOP":114,"ForBody":115,"FOR":116,"BY":117,"ForStart":118,"ForSource":119,"ForVariables":120,"OWN":121,"ForValue":122,"FORIN":123,"FOROF":124,"SWITCH":125,"Whens":126,"ELSE":127,"When":128,"LEADING_WHEN":129,"IfBlock":130,"IF":131,"POST_IF":132,"UNARY":133,"UNARY_MATH":134,"-":135,"+":136,"YIELD":137,"FROM":138,"--":139,"++":140,"?":141,"MATH":142,"**":143,"SHIFT":144,"COMPARE":145,"LOGIC":146,"RELATION":147,"COMPOUND_ASSIGN":148,"$accept":0,"$end":1},
terminals_: {2:"error",6:"TERMINATOR",11:"STATEMENT",25:"INDENT",26:"OUTDENT",28:"IDENTIFIER",30:"NUMBER",32:"STRING",33:"STRING_START",34:"STRING_END",36:"REGEX",37:"REGEX_START",38:"REGEX_END",40:"JS",41:"DEBUGGER",42:"UNDEFINED",43:"NULL",44:"BOOL",46:"=",49:":",51:"RETURN",52:"HERECOMMENT",53:"PARAM_START",55:"PARAM_END",57:"->",58:"=>",60:",",63:"...",72:".",73:"?.",74:"::",75:"?::",77:"INDEX_START",79:"INDEX_END",80:"INDEX_SOAK",82:"{",84:"}",85:"CLASS",86:"EXTENDS",89:"SUPER",90:"FUNC_EXIST",91:"CALL_START",92:"CALL_END",94:"THIS",95:"@",96:"[",97:"]",99:"..",102:"TRY",104:"FINALLY",105:"CATCH",106:"THROW",107:"(",108:")",110:"WHILE",111:"WHEN",112:"UNTIL",114:"LOOP",116:"FOR",117:"BY",121:"OWN",123:"FORIN",124:"FOROF",125:"SWITCH",127:"ELSE",129:"LEADING_WHEN",131:"IF",132:"POST_IF",133:"UNARY",134:"UNARY_MATH",135:"-",136:"+",137:"YIELD",138:"FROM",139:"--",140:"++",141:"?",142:"MATH",143:"**",144:"SHIFT",145:"COMPARE",146:"LOGIC",147:"RELATION",148:"COMPOUND_ASSIGN"},
productions_: [0,[3,0],[3,1],[4,1],[4,3],[4,2],[5,1],[5,1],[8,1],[8,1],[8,1],[7,1],[7,1],[7,1],[7,1],[7,1],[7,1],[7,1],[7,1],[7,1],[7,1],[7,1],[7,1],[24,2],[24,3],[27,1],[29,1],[29,1],[31,1],[31,3],[35,1],[35,3],[39,1],[39,1],[39,1],[39,1],[39,1],[39,1],[39,1],[16,3],[16,4],[16,5],[47,1],[47,3],[47,5],[47,1],[48,1],[48,1],[48,1],[9,2],[9,1],[10,1],[14,5],[14,2],[56,1],[56,1],[59,0],[59,1],[54,0],[54,1],[54,3],[54,4],[54,6],[61,1],[61,2],[61,3],[61,1],[62,1],[62,1],[62,1],[62,1],[66,2],[67,1],[67,2],[67,2],[67,1],[45,1],[45,1],[45,1],[12,1],[12,1],[12,1],[12,1],[12,1],[68,2],[68,2],[68,2],[68,2],[68,1],[68,1],[76,3],[76,2],[78,1],[78,1],[65,4],[83,0],[83,1],[83,3],[83,4],[83,6],[22,1],[22,2],[22,3],[22,4],[22,2],[22,3],[22,4],[22,5],[13,3],[13,3],[13,1],[13,2],[87,0],[87,1],[88,2],[88,4],[71,1],[71,1],[50,2],[64,2],[64,4],[98,1],[98,1],[70,5],[81,3],[81,2],[81,2],[81,1],[93,1],[93,3],[93,4],[93,4],[93,6],[100,1],[100,1],[100,1],[101,1],[101,3],[18,2],[18,3],[18,4],[18,5],[103,3],[103,3],[103,2],[23,2],[69,3],[69,5],[109,2],[109,4],[109,2],[109,4],[19,2],[19,2],[19,2],[19,1],[113,2],[113,2],[20,2],[20,2],[20,2],[115,2],[115,4],[115,2],[118,2],[118,3],[122,1],[122,1],[122,1],[122,1],[120,1],[120,3],[119,2],[119,2],[119,4],[119,4],[119,4],[119,6],[119,6],[21,5],[21,7],[21,4],[21,6],[126,1],[126,2],[128,3],[128,4],[130,3],[130,5],[17,1],[17,3],[17,3],[17,3],[15,2],[15,2],[15,2],[15,2],[15,2],[15,2],[15,3],[15,2],[15,2],[15,2],[15,2],[15,2],[15,3],[15,3],[15,3],[15,3],[15,3],[15,3],[15,3],[15,3],[15,3],[15,5],[15,4],[15,3]],
performAction: function anonymous(yytext, yyleng, yylineno, yy, yystate /* action[1] */, $$ /* vstack */, _$ /* lstack */) {
/* this == yyval */

var $0 = $$.length - 1;
switch (yystate) {
case 1:
return this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Block);
break;
case 2:
return this.$ = $$[$0];
break;
case 3:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(yy.Block.wrap([$$[$0]]));
break;
case 4:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])($$[$0-2].push($$[$0]));
break;
case 5:
this.$ = $$[$0-1];
break;
case 6: case 7: case 8: case 9: case 11: case 12: case 13: case 14: case 15: case 16: case 17: case 18: case 19: case 20: case 21: case 22: case 27: case 32: case 34: case 45: case 46: case 47: case 48: case 56: case 57: case 67: case 68: case 69: case 70: case 75: case 76: case 79: case 83: case 89: case 133: case 134: case 136: case 166: case 167: case 183: case 189:
this.$ = $$[$0];
break;
case 10: case 25: case 26: case 28: case 30: case 33: case 35:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Literal($$[$0]));
break;
case 23:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Block);
break;
case 24: case 31: case 90:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])($$[$0-1]);
break;
case 29: case 146:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Parens($$[$0-1]));
break;
case 36:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Undefined);
break;
case 37:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Null);
break;
case 38:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Bool($$[$0]));
break;
case 39:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Assign($$[$0-2], $$[$0]));
break;
case 40:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])(new yy.Assign($$[$0-3], $$[$0]));
break;
case 41:
this.$ = yy.addLocationDataFn(_$[$0-4], _$[$0])(new yy.Assign($$[$0-4], $$[$0-1]));
break;
case 42: case 72: case 77: case 78: case 80: case 81: case 82: case 168: case 169:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Value($$[$0]));
break;
case 43:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Assign(yy.addLocationDataFn(_$[$0-2])(new yy.Value($$[$0-2])), $$[$0], 'object'));
break;
case 44:
this.$ = yy.addLocationDataFn(_$[$0-4], _$[$0])(new yy.Assign(yy.addLocationDataFn(_$[$0-4])(new yy.Value($$[$0-4])), $$[$0-1], 'object'));
break;
case 49:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Return($$[$0]));
break;
case 50:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Return);
break;
case 51:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Comment($$[$0]));
break;
case 52:
this.$ = yy.addLocationDataFn(_$[$0-4], _$[$0])(new yy.Code($$[$0-3], $$[$0], $$[$0-1]));
break;
case 53:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Code([], $$[$0], $$[$0-1]));
break;
case 54:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])('func');
break;
case 55:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])('boundfunc');
break;
case 58: case 95:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])([]);
break;
case 59: case 96: case 128: case 170:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])([$$[$0]]);
break;
case 60: case 97: case 129:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])($$[$0-2].concat($$[$0]));
break;
case 61: case 98: case 130:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])($$[$0-3].concat($$[$0]));
break;
case 62: case 99: case 132:
this.$ = yy.addLocationDataFn(_$[$0-5], _$[$0])($$[$0-5].concat($$[$0-2]));
break;
case 63:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Param($$[$0]));
break;
case 64:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Param($$[$0-1], null, true));
break;
case 65:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Param($$[$0-2], $$[$0]));
break;
case 66: case 135:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Expansion);
break;
case 71:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Splat($$[$0-1]));
break;
case 73:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])($$[$0-1].add($$[$0]));
break;
case 74:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Value($$[$0-1], [].concat($$[$0])));
break;
case 84:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Access($$[$0]));
break;
case 85:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Access($$[$0], 'soak'));
break;
case 86:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])([yy.addLocationDataFn(_$[$0-1])(new yy.Access(new yy.Literal('prototype'))), yy.addLocationDataFn(_$[$0])(new yy.Access($$[$0]))]);
break;
case 87:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])([yy.addLocationDataFn(_$[$0-1])(new yy.Access(new yy.Literal('prototype'), 'soak')), yy.addLocationDataFn(_$[$0])(new yy.Access($$[$0]))]);
break;
case 88:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Access(new yy.Literal('prototype')));
break;
case 91:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(yy.extend($$[$0], {
          soak: true
        }));
break;
case 92:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Index($$[$0]));
break;
case 93:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Slice($$[$0]));
break;
case 94:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])(new yy.Obj($$[$0-2], $$[$0-3].generated));
break;
case 100:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Class);
break;
case 101:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Class(null, null, $$[$0]));
break;
case 102:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Class(null, $$[$0]));
break;
case 103:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])(new yy.Class(null, $$[$0-1], $$[$0]));
break;
case 104:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Class($$[$0]));
break;
case 105:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Class($$[$0-1], null, $$[$0]));
break;
case 106:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])(new yy.Class($$[$0-2], $$[$0]));
break;
case 107:
this.$ = yy.addLocationDataFn(_$[$0-4], _$[$0])(new yy.Class($$[$0-3], $$[$0-1], $$[$0]));
break;
case 108: case 109:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Call($$[$0-2], $$[$0], $$[$0-1]));
break;
case 110:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Call('super', [new yy.Splat(new yy.Literal('arguments'))]));
break;
case 111:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Call('super', $$[$0]));
break;
case 112:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(false);
break;
case 113:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(true);
break;
case 114:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])([]);
break;
case 115: case 131:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])($$[$0-2]);
break;
case 116: case 117:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Value(new yy.Literal('this')));
break;
case 118:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Value(yy.addLocationDataFn(_$[$0-1])(new yy.Literal('this')), [yy.addLocationDataFn(_$[$0])(new yy.Access($$[$0]))], 'this'));
break;
case 119:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Arr([]));
break;
case 120:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])(new yy.Arr($$[$0-2]));
break;
case 121:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])('inclusive');
break;
case 122:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])('exclusive');
break;
case 123:
this.$ = yy.addLocationDataFn(_$[$0-4], _$[$0])(new yy.Range($$[$0-3], $$[$0-1], $$[$0-2]));
break;
case 124:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Range($$[$0-2], $$[$0], $$[$0-1]));
break;
case 125:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Range($$[$0-1], null, $$[$0]));
break;
case 126:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Range(null, $$[$0], $$[$0-1]));
break;
case 127:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])(new yy.Range(null, null, $$[$0]));
break;
case 137:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])([].concat($$[$0-2], $$[$0]));
break;
case 138:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Try($$[$0]));
break;
case 139:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Try($$[$0-1], $$[$0][0], $$[$0][1]));
break;
case 140:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])(new yy.Try($$[$0-2], null, null, $$[$0]));
break;
case 141:
this.$ = yy.addLocationDataFn(_$[$0-4], _$[$0])(new yy.Try($$[$0-3], $$[$0-2][0], $$[$0-2][1], $$[$0]));
break;
case 142:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])([$$[$0-1], $$[$0]]);
break;
case 143:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])([yy.addLocationDataFn(_$[$0-1])(new yy.Value($$[$0-1])), $$[$0]]);
break;
case 144:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])([null, $$[$0]]);
break;
case 145:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Throw($$[$0]));
break;
case 147:
this.$ = yy.addLocationDataFn(_$[$0-4], _$[$0])(new yy.Parens($$[$0-2]));
break;
case 148:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.While($$[$0]));
break;
case 149:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])(new yy.While($$[$0-2], {
          guard: $$[$0]
        }));
break;
case 150:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.While($$[$0], {
          invert: true
        }));
break;
case 151:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])(new yy.While($$[$0-2], {
          invert: true,
          guard: $$[$0]
        }));
break;
case 152:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])($$[$0-1].addBody($$[$0]));
break;
case 153: case 154:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])($$[$0].addBody(yy.addLocationDataFn(_$[$0-1])(yy.Block.wrap([$$[$0-1]]))));
break;
case 155:
this.$ = yy.addLocationDataFn(_$[$0], _$[$0])($$[$0]);
break;
case 156:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.While(yy.addLocationDataFn(_$[$0-1])(new yy.Literal('true'))).addBody($$[$0]));
break;
case 157:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.While(yy.addLocationDataFn(_$[$0-1])(new yy.Literal('true'))).addBody(yy.addLocationDataFn(_$[$0])(yy.Block.wrap([$$[$0]]))));
break;
case 158: case 159:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.For($$[$0-1], $$[$0]));
break;
case 160:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.For($$[$0], $$[$0-1]));
break;
case 161:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])({
          source: yy.addLocationDataFn(_$[$0])(new yy.Value($$[$0]))
        });
break;
case 162:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])({
          source: yy.addLocationDataFn(_$[$0-2])(new yy.Value($$[$0-2])),
          step: $$[$0]
        });
break;
case 163:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])((function () {
        $$[$0].own = $$[$0-1].own;
        $$[$0].name = $$[$0-1][0];
        $$[$0].index = $$[$0-1][1];
        return $$[$0];
      }()));
break;
case 164:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])($$[$0]);
break;
case 165:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])((function () {
        $$[$0].own = true;
        return $$[$0];
      }()));
break;
case 171:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])([$$[$0-2], $$[$0]]);
break;
case 172:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])({
          source: $$[$0]
        });
break;
case 173:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])({
          source: $$[$0],
          object: true
        });
break;
case 174:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])({
          source: $$[$0-2],
          guard: $$[$0]
        });
break;
case 175:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])({
          source: $$[$0-2],
          guard: $$[$0],
          object: true
        });
break;
case 176:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])({
          source: $$[$0-2],
          step: $$[$0]
        });
break;
case 177:
this.$ = yy.addLocationDataFn(_$[$0-5], _$[$0])({
          source: $$[$0-4],
          guard: $$[$0-2],
          step: $$[$0]
        });
break;
case 178:
this.$ = yy.addLocationDataFn(_$[$0-5], _$[$0])({
          source: $$[$0-4],
          step: $$[$0-2],
          guard: $$[$0]
        });
break;
case 179:
this.$ = yy.addLocationDataFn(_$[$0-4], _$[$0])(new yy.Switch($$[$0-3], $$[$0-1]));
break;
case 180:
this.$ = yy.addLocationDataFn(_$[$0-6], _$[$0])(new yy.Switch($$[$0-5], $$[$0-3], $$[$0-1]));
break;
case 181:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])(new yy.Switch(null, $$[$0-1]));
break;
case 182:
this.$ = yy.addLocationDataFn(_$[$0-5], _$[$0])(new yy.Switch(null, $$[$0-3], $$[$0-1]));
break;
case 184:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])($$[$0-1].concat($$[$0]));
break;
case 185:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])([[$$[$0-1], $$[$0]]]);
break;
case 186:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])([[$$[$0-2], $$[$0-1]]]);
break;
case 187:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.If($$[$0-1], $$[$0], {
          type: $$[$0-2]
        }));
break;
case 188:
this.$ = yy.addLocationDataFn(_$[$0-4], _$[$0])($$[$0-4].addElse(yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.If($$[$0-1], $$[$0], {
          type: $$[$0-2]
        }))));
break;
case 190:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])($$[$0-2].addElse($$[$0]));
break;
case 191: case 192:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.If($$[$0], yy.addLocationDataFn(_$[$0-2])(yy.Block.wrap([$$[$0-2]])), {
          type: $$[$0-1],
          statement: true
        }));
break;
case 193: case 194: case 197: case 198:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Op($$[$0-1], $$[$0]));
break;
case 195:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Op('-', $$[$0]));
break;
case 196:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Op('+', $$[$0]));
break;
case 199:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Op($$[$0-2].concat($$[$0-1]), $$[$0]));
break;
case 200:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Op('--', $$[$0]));
break;
case 201:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Op('++', $$[$0]));
break;
case 202:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Op('--', $$[$0-1], null, true));
break;
case 203:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Op('++', $$[$0-1], null, true));
break;
case 204:
this.$ = yy.addLocationDataFn(_$[$0-1], _$[$0])(new yy.Existence($$[$0-1]));
break;
case 205:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Op('+', $$[$0-2], $$[$0]));
break;
case 206:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Op('-', $$[$0-2], $$[$0]));
break;
case 207: case 208: case 209: case 210: case 211:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Op($$[$0-1], $$[$0-2], $$[$0]));
break;
case 212:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])((function () {
        if ($$[$0-1].charAt(0) === '!') {
          return new yy.Op($$[$0-1].slice(1), $$[$0-2], $$[$0]).invert();
        } else {
          return new yy.Op($$[$0-1], $$[$0-2], $$[$0]);
        }
      }()));
break;
case 213:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Assign($$[$0-2], $$[$0], $$[$0-1]));
break;
case 214:
this.$ = yy.addLocationDataFn(_$[$0-4], _$[$0])(new yy.Assign($$[$0-4], $$[$0-1], $$[$0-3]));
break;
case 215:
this.$ = yy.addLocationDataFn(_$[$0-3], _$[$0])(new yy.Assign($$[$0-3], $$[$0], $$[$0-2]));
break;
case 216:
this.$ = yy.addLocationDataFn(_$[$0-2], _$[$0])(new yy.Extends($$[$0-2], $$[$0]));
break;
}
},
table: [{1:[2,1],3:1,4:2,5:3,7:4,8:5,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{1:[3]},{1:[2,2],6:$VD},o($VE,[2,3]),o($VE,[2,6],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($VE,[2,7],{118:69,109:92,115:93,110:$Vq,112:$Vr,116:$Vt,132:$VP}),o($VQ,[2,11],{87:94,68:95,76:101,72:$VR,73:$VS,74:$VT,75:$VU,77:$VV,80:$VW,90:$VX,91:$VY}),o($VQ,[2,12],{76:101,87:104,68:105,72:$VR,73:$VS,74:$VT,75:$VU,77:$VV,80:$VW,90:$VX,91:$VY}),o($VQ,[2,13]),o($VQ,[2,14]),o($VQ,[2,15]),o($VQ,[2,16]),o($VQ,[2,17]),o($VQ,[2,18]),o($VQ,[2,19]),o($VQ,[2,20]),o($VQ,[2,21]),o($VQ,[2,22]),o($VQ,[2,8]),o($VQ,[2,9]),o($VQ,[2,10]),o($VZ,$V_,{46:[1,106]}),o($VZ,[2,80]),o($VZ,[2,81]),o($VZ,[2,82]),o($VZ,[2,83]),o([1,6,25,26,34,38,55,60,63,72,73,74,75,77,79,80,84,90,92,97,99,108,110,111,112,116,117,132,135,136,141,142,143,144,145,146,147],[2,110],{88:107,91:$V$}),o([6,25,55,60],$V01,{54:109,61:110,62:111,27:113,50:114,64:115,65:116,28:$V1,63:$V11,82:$Vh,95:$V21,96:$V31}),{24:119,25:$V41},{7:121,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:123,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:124,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:125,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:127,8:126,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,138:[1,128],139:$VB,140:$VC},{12:130,13:131,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:132,50:63,64:47,65:48,67:129,69:23,70:24,71:25,82:$Vh,89:$Vj,94:$Vk,95:$Vl,96:$Vm,107:$Vp},{12:130,13:131,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:132,50:63,64:47,65:48,67:133,69:23,70:24,71:25,82:$Vh,89:$Vj,94:$Vk,95:$Vl,96:$Vm,107:$Vp},o($V51,$V61,{86:[1,137],139:[1,134],140:[1,135],148:[1,136]}),o($VQ,[2,189],{127:[1,138]}),{24:139,25:$V41},{24:140,25:$V41},o($VQ,[2,155]),{24:141,25:$V41},{7:142,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,25:[1,143],27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($V71,[2,100],{39:22,69:23,70:24,71:25,64:47,65:48,29:49,35:51,27:62,50:63,31:72,12:130,13:131,45:132,24:144,67:146,25:$V41,28:$V1,30:$V2,32:$V3,33:$V4,36:$V5,37:$V6,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,82:$Vh,86:[1,145],89:$Vj,94:$Vk,95:$Vl,96:$Vm,107:$Vp}),{7:147,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o([1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132,141,142,143,144,145,146,147],[2,50],{12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,9:18,10:19,45:21,39:22,69:23,70:24,71:25,56:28,67:36,130:37,109:39,113:40,115:41,64:47,65:48,29:49,35:51,27:62,50:63,118:69,31:72,8:122,7:148,11:$V0,28:$V1,30:$V2,32:$V3,33:$V4,36:$V5,37:$V6,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,51:$Vc,52:$Vd,53:$Ve,57:$Vf,58:$Vg,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,114:$Vs,125:$Vu,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC}),o($VQ,[2,51]),o($V51,[2,77]),o($V51,[2,78]),o($VZ,[2,32]),o($VZ,[2,33]),o($VZ,[2,34]),o($VZ,[2,35]),o($VZ,[2,36]),o($VZ,[2,37]),o($VZ,[2,38]),{4:149,5:3,7:4,8:5,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,25:[1,150],27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:151,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,25:$V81,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,63:$V91,64:47,65:48,66:156,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,93:153,94:$Vk,95:$Vl,96:$Vm,97:$Va1,100:154,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VZ,[2,116]),o($VZ,[2,117],{27:158,28:$V1}),{25:[2,54]},{25:[2,55]},o($Vb1,[2,72]),o($Vb1,[2,75]),{7:159,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:160,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:161,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:163,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,24:162,25:$V41,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{27:168,28:$V1,50:169,64:170,65:171,70:164,82:$Vh,95:$V21,96:$Vm,120:165,121:[1,166],122:167},{119:172,123:[1,173],124:[1,174]},o([6,25,60,84],$Vc1,{31:72,83:175,47:176,48:177,10:178,27:179,29:180,50:181,28:$V1,30:$V2,32:$V3,33:$V4,52:$Vd,95:$V21}),o($Vd1,[2,26]),o($Vd1,[2,27]),o($VZ,[2,30]),{12:130,13:182,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:132,50:63,64:47,65:48,67:183,69:23,70:24,71:25,82:$Vh,89:$Vj,94:$Vk,95:$Vl,96:$Vm,107:$Vp},o($Ve1,[2,25]),o($Vd1,[2,28]),{4:184,5:3,7:4,8:5,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VE,[2,5],{7:4,8:5,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,9:18,10:19,45:21,39:22,69:23,70:24,71:25,56:28,67:36,130:37,109:39,113:40,115:41,64:47,65:48,29:49,35:51,27:62,50:63,118:69,31:72,5:185,11:$V0,28:$V1,30:$V2,32:$V3,33:$V4,36:$V5,37:$V6,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,51:$Vc,52:$Vd,53:$Ve,57:$Vf,58:$Vg,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,110:$Vq,112:$Vr,114:$Vs,116:$Vt,125:$Vu,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC}),o($VQ,[2,204]),{7:186,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:187,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:188,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:189,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:190,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:191,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:192,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:193,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:194,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VQ,[2,154]),o($VQ,[2,159]),{7:195,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VQ,[2,153]),o($VQ,[2,158]),{88:196,91:$V$},o($Vb1,[2,73]),{91:[2,113]},{27:197,28:$V1},{27:198,28:$V1},o($Vb1,[2,88],{27:199,28:$V1}),{27:200,28:$V1},o($Vb1,[2,89]),{7:202,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,63:$Vf1,64:47,65:48,67:36,69:23,70:24,71:25,78:201,81:203,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,98:204,99:$Vg1,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{76:207,77:$VV,80:$VW},{88:208,91:$V$},o($Vb1,[2,74]),{6:[1,210],7:209,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,25:[1,211],27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($Vh1,[2,111]),{7:214,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,25:$V81,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,63:$V91,64:47,65:48,66:156,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,92:[1,212],93:213,94:$Vk,95:$Vl,96:$Vm,100:154,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o([6,25],$Vi1,{59:217,55:[1,215],60:$Vj1}),o($Vk1,[2,59]),o($Vk1,[2,63],{46:[1,219],63:[1,218]}),o($Vk1,[2,66]),o($Vl1,[2,67]),o($Vl1,[2,68]),o($Vl1,[2,69]),o($Vl1,[2,70]),{27:158,28:$V1},{7:214,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,25:$V81,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,63:$V91,64:47,65:48,66:156,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,93:153,94:$Vk,95:$Vl,96:$Vm,97:$Va1,100:154,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VQ,[2,53]),{4:221,5:3,7:4,8:5,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,26:[1,220],27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o([1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132,135,136,142,143,144,145,146,147],[2,193],{118:69,109:89,115:90,141:$VI}),{109:92,110:$Vq,112:$Vr,115:93,116:$Vt,118:69,132:$VP},o($Vm1,[2,194],{118:69,109:89,115:90,141:$VI,143:$VK}),o($Vm1,[2,195],{118:69,109:89,115:90,141:$VI,143:$VK}),o($Vm1,[2,196],{118:69,109:89,115:90,141:$VI,143:$VK}),o($VQ,[2,197],{118:69,109:92,115:93}),o($Vn1,[2,198],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{7:222,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VQ,[2,200],{72:$V61,73:$V61,74:$V61,75:$V61,77:$V61,80:$V61,90:$V61,91:$V61}),{68:95,72:$VR,73:$VS,74:$VT,75:$VU,76:101,77:$VV,80:$VW,87:94,90:$VX,91:$VY},{68:105,72:$VR,73:$VS,74:$VT,75:$VU,76:101,77:$VV,80:$VW,87:104,90:$VX,91:$VY},o($Vo1,$V_),o($VQ,[2,201],{72:$V61,73:$V61,74:$V61,75:$V61,77:$V61,80:$V61,90:$V61,91:$V61}),o($VQ,[2,202]),o($VQ,[2,203]),{6:[1,225],7:223,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,25:[1,224],27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:226,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{24:227,25:$V41,131:[1,228]},o($VQ,[2,138],{103:229,104:[1,230],105:[1,231]}),o($VQ,[2,152]),o($VQ,[2,160]),{25:[1,232],109:89,110:$Vq,112:$Vr,115:90,116:$Vt,118:69,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO},{126:233,128:234,129:$Vp1},o($VQ,[2,101]),{7:236,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($V71,[2,104],{24:237,25:$V41,72:$V61,73:$V61,74:$V61,75:$V61,77:$V61,80:$V61,90:$V61,91:$V61,86:[1,238]}),o($Vn1,[2,145],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vn1,[2,49],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{6:$VD,108:[1,239]},{4:240,5:3,7:4,8:5,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o([6,25,60,97],$Vq1,{118:69,109:89,115:90,98:241,63:[1,242],99:$Vg1,110:$Vq,112:$Vr,116:$Vt,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vr1,[2,119]),o([6,25,97],$Vi1,{59:243,60:$Vs1}),o($Vt1,[2,128]),{7:214,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,25:$V81,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,63:$V91,64:47,65:48,66:156,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,93:245,94:$Vk,95:$Vl,96:$Vm,100:154,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($Vt1,[2,134]),o($Vt1,[2,135]),o($Ve1,[2,118]),{24:246,25:$V41,109:89,110:$Vq,112:$Vr,115:90,116:$Vt,118:69,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO},o($Vu1,[2,148],{118:69,109:89,115:90,110:$Vq,111:[1,247],112:$Vr,116:$Vt,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vu1,[2,150],{118:69,109:89,115:90,110:$Vq,111:[1,248],112:$Vr,116:$Vt,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($VQ,[2,156]),o($Vv1,[2,157],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o([1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,132,135,136,141,142,143,144,145,146,147],[2,161],{117:[1,249]}),o($Vw1,[2,164]),{27:168,28:$V1,50:169,64:170,65:171,82:$Vh,95:$V21,96:$V31,120:250,122:167},o($Vw1,[2,170],{60:[1,251]}),o($Vx1,[2,166]),o($Vx1,[2,167]),o($Vx1,[2,168]),o($Vx1,[2,169]),o($VQ,[2,163]),{7:252,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:253,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o([6,25,84],$Vi1,{59:254,60:$Vy1}),o($Vz1,[2,96]),o($Vz1,[2,42],{49:[1,256]}),o($Vz1,[2,45]),o($VA1,[2,46]),o($VA1,[2,47]),o($VA1,[2,48]),{38:[1,257],68:105,72:$VR,73:$VS,74:$VT,75:$VU,76:101,77:$VV,80:$VW,87:104,90:$VX,91:$VY},o($Vo1,$V61),{6:$VD,34:[1,258]},o($VE,[2,4]),o($VB1,[2,205],{118:69,109:89,115:90,141:$VI,142:$VJ,143:$VK}),o($VB1,[2,206],{118:69,109:89,115:90,141:$VI,142:$VJ,143:$VK}),o($Vm1,[2,207],{118:69,109:89,115:90,141:$VI,143:$VK}),o($Vm1,[2,208],{118:69,109:89,115:90,141:$VI,143:$VK}),o([1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132,144,145,146,147],[2,209],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK}),o([1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132,145,146],[2,210],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,147:$VO}),o([1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132,146],[2,211],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,147:$VO}),o([1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,117,132,145,146,147],[2,212],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL}),o($Vv1,[2,192],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vv1,[2,191],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vh1,[2,108]),o($Vb1,[2,84]),o($Vb1,[2,85]),o($Vb1,[2,86]),o($Vb1,[2,87]),{79:[1,259]},{63:$Vf1,79:[2,92],98:260,99:$Vg1,109:89,110:$Vq,112:$Vr,115:90,116:$Vt,118:69,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO},{79:[2,93]},{7:261,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,79:[2,127],82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VC1,[2,121]),o($VC1,$VD1),o($Vb1,[2,91]),o($Vh1,[2,109]),o($Vn1,[2,39],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{7:262,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:263,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($Vh1,[2,114]),o([6,25,92],$Vi1,{59:264,60:$Vs1}),o($Vt1,$Vq1,{118:69,109:89,115:90,63:[1,265],110:$Vq,112:$Vr,116:$Vt,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{56:266,57:$Vf,58:$Vg},o($VE1,$VF1,{62:111,27:113,50:114,64:115,65:116,61:267,28:$V1,63:$V11,82:$Vh,95:$V21,96:$V31}),{6:$VG1,25:$VH1},o($Vk1,[2,64]),{7:270,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VI1,[2,23]),{6:$VD,26:[1,271]},o($Vn1,[2,199],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vn1,[2,213],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{7:272,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:273,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($Vn1,[2,216],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($VQ,[2,190]),{7:274,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VQ,[2,139],{104:[1,275]}),{24:276,25:$V41},{24:279,25:$V41,27:277,28:$V1,65:278,82:$Vh},{126:280,128:234,129:$Vp1},{26:[1,281],127:[1,282],128:283,129:$Vp1},o($VJ1,[2,183]),{7:285,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,101:284,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VK1,[2,102],{118:69,109:89,115:90,24:286,25:$V41,110:$Vq,112:$Vr,116:$Vt,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($VQ,[2,105]),{7:287,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VZ,[2,146]),{6:$VD,26:[1,288]},{7:289,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o([11,28,30,32,33,36,37,40,41,42,43,44,51,52,53,57,58,82,85,89,94,95,96,102,106,107,110,112,114,116,125,131,133,134,135,136,137,139,140],$VD1,{6:$VL1,25:$VL1,60:$VL1,97:$VL1}),{6:$VM1,25:$VN1,97:[1,290]},o([6,25,26,92,97],$VF1,{12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,9:18,10:19,45:21,39:22,69:23,70:24,71:25,56:28,67:36,130:37,109:39,113:40,115:41,64:47,65:48,29:49,35:51,27:62,50:63,118:69,31:72,8:122,66:156,7:214,100:293,11:$V0,28:$V1,30:$V2,32:$V3,33:$V4,36:$V5,37:$V6,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,51:$Vc,52:$Vd,53:$Ve,57:$Vf,58:$Vg,63:$V91,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,110:$Vq,112:$Vr,114:$Vs,116:$Vt,125:$Vu,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC}),o($VE1,$Vi1,{59:294,60:$Vs1}),o($VO1,[2,187]),{7:295,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:296,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:297,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($Vw1,[2,165]),{27:168,28:$V1,50:169,64:170,65:171,82:$Vh,95:$V21,96:$V31,122:298},o([1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,112,116,132],[2,172],{118:69,109:89,115:90,111:[1,299],117:[1,300],135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($VP1,[2,173],{118:69,109:89,115:90,111:[1,301],135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{6:$VQ1,25:$VR1,84:[1,302]},o([6,25,26,84],$VF1,{31:72,48:177,10:178,27:179,29:180,50:181,47:305,28:$V1,30:$V2,32:$V3,33:$V4,52:$Vd,95:$V21}),{7:306,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,25:[1,307],27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VZ,[2,31]),o($Vd1,[2,29]),o($Vb1,[2,90]),{7:308,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,79:[2,125],82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{79:[2,126],109:89,110:$Vq,112:$Vr,115:90,116:$Vt,118:69,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO},o($Vn1,[2,40],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{26:[1,309],109:89,110:$Vq,112:$Vr,115:90,116:$Vt,118:69,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO},{6:$VM1,25:$VN1,92:[1,310]},o($Vt1,$VL1),{24:311,25:$V41},o($Vk1,[2,60]),{27:113,28:$V1,50:114,61:312,62:111,63:$V11,64:115,65:116,82:$Vh,95:$V21,96:$V31},o($VS1,$V01,{61:110,62:111,27:113,50:114,64:115,65:116,54:313,28:$V1,63:$V11,82:$Vh,95:$V21,96:$V31}),o($Vk1,[2,65],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($VI1,[2,24]),{26:[1,314],109:89,110:$Vq,112:$Vr,115:90,116:$Vt,118:69,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO},o($Vn1,[2,215],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{24:315,25:$V41,109:89,110:$Vq,112:$Vr,115:90,116:$Vt,118:69,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO},{24:316,25:$V41},o($VQ,[2,140]),{24:317,25:$V41},{24:318,25:$V41},o($VT1,[2,144]),{26:[1,319],127:[1,320],128:283,129:$Vp1},o($VQ,[2,181]),{24:321,25:$V41},o($VJ1,[2,184]),{24:322,25:$V41,60:[1,323]},o($VU1,[2,136],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($VQ,[2,103]),o($VK1,[2,106],{118:69,109:89,115:90,24:324,25:$V41,110:$Vq,112:$Vr,116:$Vt,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{108:[1,325]},{97:[1,326],109:89,110:$Vq,112:$Vr,115:90,116:$Vt,118:69,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO},o($Vr1,[2,120]),{7:214,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,63:$V91,64:47,65:48,66:156,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,100:327,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:214,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,25:$V81,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,63:$V91,64:47,65:48,66:156,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,93:328,94:$Vk,95:$Vl,96:$Vm,100:154,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($Vt1,[2,129]),{6:$VM1,25:$VN1,26:[1,329]},o($Vv1,[2,149],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vv1,[2,151],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vv1,[2,162],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vw1,[2,171]),{7:330,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:331,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:332,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($Vr1,[2,94]),{10:178,27:179,28:$V1,29:180,30:$V2,31:72,32:$V3,33:$V4,47:333,48:177,50:181,52:$Vd,95:$V21},o($VS1,$Vc1,{31:72,47:176,48:177,10:178,27:179,29:180,50:181,83:334,28:$V1,30:$V2,32:$V3,33:$V4,52:$Vd,95:$V21}),o($Vz1,[2,97]),o($Vz1,[2,43],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{7:335,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{79:[2,124],109:89,110:$Vq,112:$Vr,115:90,116:$Vt,118:69,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO},o($VQ,[2,41]),o($Vh1,[2,115]),o($VQ,[2,52]),o($Vk1,[2,61]),o($VE1,$Vi1,{59:336,60:$Vj1}),o($VQ,[2,214]),o($VO1,[2,188]),o($VQ,[2,141]),o($VT1,[2,142]),o($VT1,[2,143]),o($VQ,[2,179]),{24:337,25:$V41},{26:[1,338]},o($VJ1,[2,185],{6:[1,339]}),{7:340,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},o($VQ,[2,107]),o($VZ,[2,147]),o($VZ,[2,123]),o($Vt1,[2,130]),o($VE1,$Vi1,{59:341,60:$Vs1}),o($Vt1,[2,131]),o([1,6,25,26,34,55,60,63,79,84,92,97,99,108,110,111,112,116,132],[2,174],{118:69,109:89,115:90,117:[1,342],135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($VP1,[2,176],{118:69,109:89,115:90,111:[1,343],135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vn1,[2,175],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vz1,[2,98]),o($VE1,$Vi1,{59:344,60:$Vy1}),{26:[1,345],109:89,110:$Vq,112:$Vr,115:90,116:$Vt,118:69,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO},{6:$VG1,25:$VH1,26:[1,346]},{26:[1,347]},o($VQ,[2,182]),o($VJ1,[2,186]),o($VU1,[2,137],{118:69,109:89,115:90,110:$Vq,112:$Vr,116:$Vt,132:$VF,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),{6:$VM1,25:$VN1,26:[1,348]},{7:349,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{7:350,8:122,9:18,10:19,11:$V0,12:6,13:7,14:8,15:9,16:10,17:11,18:12,19:13,20:14,21:15,22:16,23:17,27:62,28:$V1,29:49,30:$V2,31:72,32:$V3,33:$V4,35:51,36:$V5,37:$V6,39:22,40:$V7,41:$V8,42:$V9,43:$Va,44:$Vb,45:21,50:63,51:$Vc,52:$Vd,53:$Ve,56:28,57:$Vf,58:$Vg,64:47,65:48,67:36,69:23,70:24,71:25,82:$Vh,85:$Vi,89:$Vj,94:$Vk,95:$Vl,96:$Vm,102:$Vn,106:$Vo,107:$Vp,109:39,110:$Vq,112:$Vr,113:40,114:$Vs,115:41,116:$Vt,118:69,125:$Vu,130:37,131:$Vv,133:$Vw,134:$Vx,135:$Vy,136:$Vz,137:$VA,139:$VB,140:$VC},{6:$VQ1,25:$VR1,26:[1,351]},o($Vz1,[2,44]),o($Vk1,[2,62]),o($VQ,[2,180]),o($Vt1,[2,132]),o($Vn1,[2,177],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vn1,[2,178],{118:69,109:89,115:90,135:$VG,136:$VH,141:$VI,142:$VJ,143:$VK,144:$VL,145:$VM,146:$VN,147:$VO}),o($Vz1,[2,99])],
defaultActions: {60:[2,54],61:[2,55],96:[2,113],203:[2,93]},
parseError: function parseError(str, hash) {
    if (hash.recoverable) {
        this.trace(str);
    } else {
        throw new Error(str);
    }
},
parse: function parse(input) {
    var self = this, stack = [0], tstack = [], vstack = [null], lstack = [], table = this.table, yytext = '', yylineno = 0, yyleng = 0, recovering = 0, TERROR = 2, EOF = 1;
    var args = lstack.slice.call(arguments, 1);
    var lexer = Object.create(this.lexer);
    var sharedState = { yy: {} };
    for (var k in this.yy) {
        if (Object.prototype.hasOwnProperty.call(this.yy, k)) {
            sharedState.yy[k] = this.yy[k];
        }
    }
    lexer.setInput(input, sharedState.yy);
    sharedState.yy.lexer = lexer;
    sharedState.yy.parser = this;
    if (typeof lexer.yylloc == 'undefined') {
        lexer.yylloc = {};
    }
    var yyloc = lexer.yylloc;
    lstack.push(yyloc);
    var ranges = lexer.options && lexer.options.ranges;
    if (typeof sharedState.yy.parseError === 'function') {
        this.parseError = sharedState.yy.parseError;
    } else {
        this.parseError = Object.getPrototypeOf(this).parseError;
    }
    function popStack(n) {
        stack.length = stack.length - 2 * n;
        vstack.length = vstack.length - n;
        lstack.length = lstack.length - n;
    }
    _token_stack:
        function lex() {
            var token;
            token = lexer.lex() || EOF;
            if (typeof token !== 'number') {
                token = self.symbols_[token] || token;
            }
            return token;
        }
    var symbol, preErrorSymbol, state, action, a, r, yyval = {}, p, len, newState, expected;
    while (true) {
        state = stack[stack.length - 1];
        if (this.defaultActions[state]) {
            action = this.defaultActions[state];
        } else {
            if (symbol === null || typeof symbol == 'undefined') {
                symbol = lex();
            }
            action = table[state] && table[state][symbol];
        }
                    if (typeof action === 'undefined' || !action.length || !action[0]) {
                var errStr = '';
                expected = [];
                for (p in table[state]) {
                    if (this.terminals_[p] && p > TERROR) {
                        expected.push('\'' + this.terminals_[p] + '\'');
                    }
                }
                if (lexer.showPosition) {
                    errStr = 'Parse error on line ' + (yylineno + 1) + ':\n' + lexer.showPosition() + '\nExpecting ' + expected.join(', ') + ', got \'' + (this.terminals_[symbol] || symbol) + '\'';
                } else {
                    errStr = 'Parse error on line ' + (yylineno + 1) + ': Unexpected ' + (symbol == EOF ? 'end of input' : '\'' + (this.terminals_[symbol] || symbol) + '\'');
                }
                this.parseError(errStr, {
                    text: lexer.match,
                    token: this.terminals_[symbol] || symbol,
                    line: lexer.yylineno,
                    loc: yyloc,
                    expected: expected
                });
            }
        if (action[0] instanceof Array && action.length > 1) {
            throw new Error('Parse Error: multiple actions possible at state: ' + state + ', token: ' + symbol);
        }
        switch (action[0]) {
        case 1:
            stack.push(symbol);
            vstack.push(lexer.yytext);
            lstack.push(lexer.yylloc);
            stack.push(action[1]);
            symbol = null;
            if (!preErrorSymbol) {
                yyleng = lexer.yyleng;
                yytext = lexer.yytext;
                yylineno = lexer.yylineno;
                yyloc = lexer.yylloc;
                if (recovering > 0) {
                    recovering--;
                }
            } else {
                symbol = preErrorSymbol;
                preErrorSymbol = null;
            }
            break;
        case 2:
            len = this.productions_[action[1]][1];
            yyval.$ = vstack[vstack.length - len];
            yyval._$ = {
                first_line: lstack[lstack.length - (len || 1)].first_line,
                last_line: lstack[lstack.length - 1].last_line,
                first_column: lstack[lstack.length - (len || 1)].first_column,
                last_column: lstack[lstack.length - 1].last_column
            };
            if (ranges) {
                yyval._$.range = [
                    lstack[lstack.length - (len || 1)].range[0],
                    lstack[lstack.length - 1].range[1]
                ];
            }
            r = this.performAction.apply(yyval, [
                yytext,
                yyleng,
                yylineno,
                sharedState.yy,
                action[1],
                vstack,
                lstack
            ].concat(args));
            if (typeof r !== 'undefined') {
                return r;
            }
            if (len) {
                stack = stack.slice(0, -1 * len * 2);
                vstack = vstack.slice(0, -1 * len);
                lstack = lstack.slice(0, -1 * len);
            }
            stack.push(this.productions_[action[1]][0]);
            vstack.push(yyval.$);
            lstack.push(yyval._$);
            newState = table[stack[stack.length - 2]][stack[stack.length - 1]];
            stack.push(newState);
            break;
        case 3:
            return true;
        }
    }
    return true;
}};

function Parser () {
  this.yy = {};
}
Parser.prototype = parser;parser.Parser = Parser;
return new Parser;
})();


if (typeof require !== 'undefined' && typeof exports !== 'undefined') {
exports.parser = parser;
exports.Parser = parser.Parser;
exports.parse = function () { return parser.parse.apply(parser, arguments); };
exports.main = function commonjsMain(args) {
    if (!args[1]) {
        console.log('Usage: '+args[0]+' FILE');
        process.exit(1);
    }
    var source = require('fs').readFileSync(require('path').normalize(args[1]), "utf8");
    return exports.parser.parse(source);
};
if (typeof module !== 'undefined' && require.main === module) {
  exports.main(process.argv.slice(1));
}
}
}).call(this,require('_process'))
},{"_process":8,"fs":2,"path":7}],25:[function(require,module,exports){
// Generated by CoffeeScript 1.9.3
(function() {
  var CoffeeScript, Module, binary, child_process, ext, findExtension, fork, helpers, i, len, loadFile, path, ref;

  CoffeeScript = require('./coffee-script');

  child_process = require('child_process');

  helpers = require('./helpers');

  path = require('path');

  loadFile = function(module, filename) {
    var answer;
    answer = CoffeeScript._compileFile(filename, false);
    return module._compile(answer, filename);
  };

  if (require.extensions) {
    ref = CoffeeScript.FILE_EXTENSIONS;
    for (i = 0, len = ref.length; i < len; i++) {
      ext = ref[i];
      require.extensions[ext] = loadFile;
    }
    Module = require('module');
    findExtension = function(filename) {
      var curExtension, extensions;
      extensions = path.basename(filename).split('.');
      if (extensions[0] === '') {
        extensions.shift();
      }
      while (extensions.shift()) {
        curExtension = '.' + extensions.join('.');
        if (Module._extensions[curExtension]) {
          return curExtension;
        }
      }
      return '.js';
    };
    Module.prototype.load = function(filename) {
      var extension;
      this.filename = filename;
      this.paths = Module._nodeModulePaths(path.dirname(filename));
      extension = findExtension(filename);
      Module._extensions[extension](this, filename);
      return this.loaded = true;
    };
  }

  if (child_process) {
    fork = child_process.fork;
    binary = require.resolve('../../bin/coffee');
    child_process.fork = function(path, args, options) {
      if (helpers.isCoffee(path)) {
        if (!Array.isArray(args)) {
          options = args || {};
          args = [];
        }
        args = [path].concat(args);
        path = binary;
      }
      return fork(path, args, options);
    };
  }

}).call(this);

},{"./coffee-script":20,"./helpers":21,"child_process":2,"module":2,"path":7}],26:[function(require,module,exports){
// Generated by CoffeeScript 1.9.3
(function() {
  var BALANCED_PAIRS, CALL_CLOSERS, EXPRESSION_CLOSE, EXPRESSION_END, EXPRESSION_START, IMPLICIT_CALL, IMPLICIT_END, IMPLICIT_FUNC, IMPLICIT_UNSPACED_CALL, INVERSES, LINEBREAKS, SINGLE_CLOSERS, SINGLE_LINERS, generate, k, left, len, ref, rite,
    indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; },
    slice = [].slice;

  generate = function(tag, value, origin) {
    var tok;
    tok = [tag, value];
    tok.generated = true;
    if (origin) {
      tok.origin = origin;
    }
    return tok;
  };

  exports.Rewriter = (function() {
    function Rewriter() {}

    Rewriter.prototype.rewrite = function(tokens1) {
      this.tokens = tokens1;
      this.removeLeadingNewlines();
      this.closeOpenCalls();
      this.closeOpenIndexes();
      this.normalizeLines();
      this.tagPostfixConditionals();
      this.addImplicitBracesAndParens();
      this.addLocationDataToGeneratedTokens();
      return this.tokens;
    };

    Rewriter.prototype.scanTokens = function(block) {
      var i, token, tokens;
      tokens = this.tokens;
      i = 0;
      while (token = tokens[i]) {
        i += block.call(this, token, i, tokens);
      }
      return true;
    };

    Rewriter.prototype.detectEnd = function(i, condition, action) {
      var levels, ref, ref1, token, tokens;
      tokens = this.tokens;
      levels = 0;
      while (token = tokens[i]) {
        if (levels === 0 && condition.call(this, token, i)) {
          return action.call(this, token, i);
        }
        if (!token || levels < 0) {
          return action.call(this, token, i - 1);
        }
        if (ref = token[0], indexOf.call(EXPRESSION_START, ref) >= 0) {
          levels += 1;
        } else if (ref1 = token[0], indexOf.call(EXPRESSION_END, ref1) >= 0) {
          levels -= 1;
        }
        i += 1;
      }
      return i - 1;
    };

    Rewriter.prototype.removeLeadingNewlines = function() {
      var i, k, len, ref, tag;
      ref = this.tokens;
      for (i = k = 0, len = ref.length; k < len; i = ++k) {
        tag = ref[i][0];
        if (tag !== 'TERMINATOR') {
          break;
        }
      }
      if (i) {
        return this.tokens.splice(0, i);
      }
    };

    Rewriter.prototype.closeOpenCalls = function() {
      var action, condition;
      condition = function(token, i) {
        var ref;
        return ((ref = token[0]) === ')' || ref === 'CALL_END') || token[0] === 'OUTDENT' && this.tag(i - 1) === ')';
      };
      action = function(token, i) {
        return this.tokens[token[0] === 'OUTDENT' ? i - 1 : i][0] = 'CALL_END';
      };
      return this.scanTokens(function(token, i) {
        if (token[0] === 'CALL_START') {
          this.detectEnd(i + 1, condition, action);
        }
        return 1;
      });
    };

    Rewriter.prototype.closeOpenIndexes = function() {
      var action, condition;
      condition = function(token, i) {
        var ref;
        return (ref = token[0]) === ']' || ref === 'INDEX_END';
      };
      action = function(token, i) {
        return token[0] = 'INDEX_END';
      };
      return this.scanTokens(function(token, i) {
        if (token[0] === 'INDEX_START') {
          this.detectEnd(i + 1, condition, action);
        }
        return 1;
      });
    };

    Rewriter.prototype.indexOfTag = function() {
      var fuzz, i, j, k, pattern, ref, ref1;
      i = arguments[0], pattern = 2 <= arguments.length ? slice.call(arguments, 1) : [];
      fuzz = 0;
      for (j = k = 0, ref = pattern.length; 0 <= ref ? k < ref : k > ref; j = 0 <= ref ? ++k : --k) {
        while (this.tag(i + j + fuzz) === 'HERECOMMENT') {
          fuzz += 2;
        }
        if (pattern[j] == null) {
          continue;
        }
        if (typeof pattern[j] === 'string') {
          pattern[j] = [pattern[j]];
        }
        if (ref1 = this.tag(i + j + fuzz), indexOf.call(pattern[j], ref1) < 0) {
          return -1;
        }
      }
      return i + j + fuzz - 1;
    };

    Rewriter.prototype.looksObjectish = function(j) {
      var end, index;
      if (this.indexOfTag(j, '@', null, ':') > -1 || this.indexOfTag(j, null, ':') > -1) {
        return true;
      }
      index = this.indexOfTag(j, EXPRESSION_START);
      if (index > -1) {
        end = null;
        this.detectEnd(index + 1, (function(token) {
          var ref;
          return ref = token[0], indexOf.call(EXPRESSION_END, ref) >= 0;
        }), (function(token, i) {
          return end = i;
        }));
        if (this.tag(end + 1) === ':') {
          return true;
        }
      }
      return false;
    };

    Rewriter.prototype.findTagsBackwards = function(i, tags) {
      var backStack, ref, ref1, ref2, ref3, ref4, ref5;
      backStack = [];
      while (i >= 0 && (backStack.length || (ref2 = this.tag(i), indexOf.call(tags, ref2) < 0) && ((ref3 = this.tag(i), indexOf.call(EXPRESSION_START, ref3) < 0) || this.tokens[i].generated) && (ref4 = this.tag(i), indexOf.call(LINEBREAKS, ref4) < 0))) {
        if (ref = this.tag(i), indexOf.call(EXPRESSION_END, ref) >= 0) {
          backStack.push(this.tag(i));
        }
        if ((ref1 = this.tag(i), indexOf.call(EXPRESSION_START, ref1) >= 0) && backStack.length) {
          backStack.pop();
        }
        i -= 1;
      }
      return ref5 = this.tag(i), indexOf.call(tags, ref5) >= 0;
    };

    Rewriter.prototype.addImplicitBracesAndParens = function() {
      var stack, start;
      stack = [];
      start = null;
      return this.scanTokens(function(token, i, tokens) {
        var endImplicitCall, endImplicitObject, forward, inImplicit, inImplicitCall, inImplicitControl, inImplicitObject, newLine, nextTag, offset, prevTag, prevToken, ref, ref1, ref2, ref3, ref4, ref5, s, sameLine, stackIdx, stackTag, stackTop, startIdx, startImplicitCall, startImplicitObject, startsLine, tag;
        tag = token[0];
        prevTag = (prevToken = i > 0 ? tokens[i - 1] : [])[0];
        nextTag = (i < tokens.length - 1 ? tokens[i + 1] : [])[0];
        stackTop = function() {
          return stack[stack.length - 1];
        };
        startIdx = i;
        forward = function(n) {
          return i - startIdx + n;
        };
        inImplicit = function() {
          var ref, ref1;
          return (ref = stackTop()) != null ? (ref1 = ref[2]) != null ? ref1.ours : void 0 : void 0;
        };
        inImplicitCall = function() {
          var ref;
          return inImplicit() && ((ref = stackTop()) != null ? ref[0] : void 0) === '(';
        };
        inImplicitObject = function() {
          var ref;
          return inImplicit() && ((ref = stackTop()) != null ? ref[0] : void 0) === '{';
        };
        inImplicitControl = function() {
          var ref;
          return inImplicit && ((ref = stackTop()) != null ? ref[0] : void 0) === 'CONTROL';
        };
        startImplicitCall = function(j) {
          var idx;
          idx = j != null ? j : i;
          stack.push([
            '(', idx, {
              ours: true
            }
          ]);
          tokens.splice(idx, 0, generate('CALL_START', '('));
          if (j == null) {
            return i += 1;
          }
        };
        endImplicitCall = function() {
          stack.pop();
          tokens.splice(i, 0, generate('CALL_END', ')', ['', 'end of input', token[2]]));
          return i += 1;
        };
        startImplicitObject = function(j, startsLine) {
          var idx, val;
          if (startsLine == null) {
            startsLine = true;
          }
          idx = j != null ? j : i;
          stack.push([
            '{', idx, {
              sameLine: true,
              startsLine: startsLine,
              ours: true
            }
          ]);
          val = new String('{');
          val.generated = true;
          tokens.splice(idx, 0, generate('{', val, token));
          if (j == null) {
            return i += 1;
          }
        };
        endImplicitObject = function(j) {
          j = j != null ? j : i;
          stack.pop();
          tokens.splice(j, 0, generate('}', '}', token));
          return i += 1;
        };
        if (inImplicitCall() && (tag === 'IF' || tag === 'TRY' || tag === 'FINALLY' || tag === 'CATCH' || tag === 'CLASS' || tag === 'SWITCH')) {
          stack.push([
            'CONTROL', i, {
              ours: true
            }
          ]);
          return forward(1);
        }
        if (tag === 'INDENT' && inImplicit()) {
          if (prevTag !== '=>' && prevTag !== '->' && prevTag !== '[' && prevTag !== '(' && prevTag !== ',' && prevTag !== '{' && prevTag !== 'TRY' && prevTag !== 'ELSE' && prevTag !== '=') {
            while (inImplicitCall()) {
              endImplicitCall();
            }
          }
          if (inImplicitControl()) {
            stack.pop();
          }
          stack.push([tag, i]);
          return forward(1);
        }
        if (indexOf.call(EXPRESSION_START, tag) >= 0) {
          stack.push([tag, i]);
          return forward(1);
        }
        if (indexOf.call(EXPRESSION_END, tag) >= 0) {
          while (inImplicit()) {
            if (inImplicitCall()) {
              endImplicitCall();
            } else if (inImplicitObject()) {
              endImplicitObject();
            } else {
              stack.pop();
            }
          }
          start = stack.pop();
        }
        if ((indexOf.call(IMPLICIT_FUNC, tag) >= 0 && token.spaced || tag === '?' && i > 0 && !tokens[i - 1].spaced) && (indexOf.call(IMPLICIT_CALL, nextTag) >= 0 || indexOf.call(IMPLICIT_UNSPACED_CALL, nextTag) >= 0 && !((ref = tokens[i + 1]) != null ? ref.spaced : void 0) && !((ref1 = tokens[i + 1]) != null ? ref1.newLine : void 0))) {
          if (tag === '?') {
            tag = token[0] = 'FUNC_EXIST';
          }
          startImplicitCall(i + 1);
          return forward(2);
        }
        if (indexOf.call(IMPLICIT_FUNC, tag) >= 0 && this.indexOfTag(i + 1, 'INDENT') > -1 && this.looksObjectish(i + 2) && !this.findTagsBackwards(i, ['CLASS', 'EXTENDS', 'IF', 'CATCH', 'SWITCH', 'LEADING_WHEN', 'FOR', 'WHILE', 'UNTIL'])) {
          startImplicitCall(i + 1);
          stack.push(['INDENT', i + 2]);
          return forward(3);
        }
        if (tag === ':') {
          s = (function() {
            var ref2;
            switch (false) {
              case ref2 = this.tag(i - 1), indexOf.call(EXPRESSION_END, ref2) < 0:
                return start[1];
              case this.tag(i - 2) !== '@':
                return i - 2;
              default:
                return i - 1;
            }
          }).call(this);
          while (this.tag(s - 2) === 'HERECOMMENT') {
            s -= 2;
          }
          this.insideForDeclaration = nextTag === 'FOR';
          startsLine = s === 0 || (ref2 = this.tag(s - 1), indexOf.call(LINEBREAKS, ref2) >= 0) || tokens[s - 1].newLine;
          if (stackTop()) {
            ref3 = stackTop(), stackTag = ref3[0], stackIdx = ref3[1];
            if ((stackTag === '{' || stackTag === 'INDENT' && this.tag(stackIdx - 1) === '{') && (startsLine || this.tag(s - 1) === ',' || this.tag(s - 1) === '{')) {
              return forward(1);
            }
          }
          startImplicitObject(s, !!startsLine);
          return forward(2);
        }
        if (inImplicitObject() && indexOf.call(LINEBREAKS, tag) >= 0) {
          stackTop()[2].sameLine = false;
        }
        newLine = prevTag === 'OUTDENT' || prevToken.newLine;
        if (indexOf.call(IMPLICIT_END, tag) >= 0 || indexOf.call(CALL_CLOSERS, tag) >= 0 && newLine) {
          while (inImplicit()) {
            ref4 = stackTop(), stackTag = ref4[0], stackIdx = ref4[1], (ref5 = ref4[2], sameLine = ref5.sameLine, startsLine = ref5.startsLine);
            if (inImplicitCall() && prevTag !== ',') {
              endImplicitCall();
            } else if (inImplicitObject() && !this.insideForDeclaration && sameLine && tag !== 'TERMINATOR' && prevTag !== ':') {
              endImplicitObject();
            } else if (inImplicitObject() && tag === 'TERMINATOR' && prevTag !== ',' && !(startsLine && this.looksObjectish(i + 1))) {
              if (nextTag === 'HERECOMMENT') {
                return forward(1);
              }
              endImplicitObject();
            } else {
              break;
            }
          }
        }
        if (tag === ',' && !this.looksObjectish(i + 1) && inImplicitObject() && !this.insideForDeclaration && (nextTag !== 'TERMINATOR' || !this.looksObjectish(i + 2))) {
          offset = nextTag === 'OUTDENT' ? 1 : 0;
          while (inImplicitObject()) {
            endImplicitObject(i + offset);
          }
        }
        return forward(1);
      });
    };

    Rewriter.prototype.addLocationDataToGeneratedTokens = function() {
      return this.scanTokens(function(token, i, tokens) {
        var column, line, nextLocation, prevLocation, ref, ref1;
        if (token[2]) {
          return 1;
        }
        if (!(token.generated || token.explicit)) {
          return 1;
        }
        if (token[0] === '{' && (nextLocation = (ref = tokens[i + 1]) != null ? ref[2] : void 0)) {
          line = nextLocation.first_line, column = nextLocation.first_column;
        } else if (prevLocation = (ref1 = tokens[i - 1]) != null ? ref1[2] : void 0) {
          line = prevLocation.last_line, column = prevLocation.last_column;
        } else {
          line = column = 0;
        }
        token[2] = {
          first_line: line,
          first_column: column,
          last_line: line,
          last_column: column
        };
        return 1;
      });
    };

    Rewriter.prototype.normalizeLines = function() {
      var action, condition, indent, outdent, starter;
      starter = indent = outdent = null;
      condition = function(token, i) {
        var ref, ref1, ref2, ref3;
        return token[1] !== ';' && (ref = token[0], indexOf.call(SINGLE_CLOSERS, ref) >= 0) && !(token[0] === 'TERMINATOR' && (ref1 = this.tag(i + 1), indexOf.call(EXPRESSION_CLOSE, ref1) >= 0)) && !(token[0] === 'ELSE' && starter !== 'THEN') && !(((ref2 = token[0]) === 'CATCH' || ref2 === 'FINALLY') && (starter === '->' || starter === '=>')) || (ref3 = token[0], indexOf.call(CALL_CLOSERS, ref3) >= 0) && this.tokens[i - 1].newLine;
      };
      action = function(token, i) {
        return this.tokens.splice((this.tag(i - 1) === ',' ? i - 1 : i), 0, outdent);
      };
      return this.scanTokens(function(token, i, tokens) {
        var j, k, ref, ref1, ref2, tag;
        tag = token[0];
        if (tag === 'TERMINATOR') {
          if (this.tag(i + 1) === 'ELSE' && this.tag(i - 1) !== 'OUTDENT') {
            tokens.splice.apply(tokens, [i, 1].concat(slice.call(this.indentation())));
            return 1;
          }
          if (ref = this.tag(i + 1), indexOf.call(EXPRESSION_CLOSE, ref) >= 0) {
            tokens.splice(i, 1);
            return 0;
          }
        }
        if (tag === 'CATCH') {
          for (j = k = 1; k <= 2; j = ++k) {
            if (!((ref1 = this.tag(i + j)) === 'OUTDENT' || ref1 === 'TERMINATOR' || ref1 === 'FINALLY')) {
              continue;
            }
            tokens.splice.apply(tokens, [i + j, 0].concat(slice.call(this.indentation())));
            return 2 + j;
          }
        }
        if (indexOf.call(SINGLE_LINERS, tag) >= 0 && this.tag(i + 1) !== 'INDENT' && !(tag === 'ELSE' && this.tag(i + 1) === 'IF')) {
          starter = tag;
          ref2 = this.indentation(tokens[i]), indent = ref2[0], outdent = ref2[1];
          if (starter === 'THEN') {
            indent.fromThen = true;
          }
          tokens.splice(i + 1, 0, indent);
          this.detectEnd(i + 2, condition, action);
          if (tag === 'THEN') {
            tokens.splice(i, 1);
          }
          return 1;
        }
        return 1;
      });
    };

    Rewriter.prototype.tagPostfixConditionals = function() {
      var action, condition, original;
      original = null;
      condition = function(token, i) {
        var prevTag, tag;
        tag = token[0];
        prevTag = this.tokens[i - 1][0];
        return tag === 'TERMINATOR' || (tag === 'INDENT' && indexOf.call(SINGLE_LINERS, prevTag) < 0);
      };
      action = function(token, i) {
        if (token[0] !== 'INDENT' || (token.generated && !token.fromThen)) {
          return original[0] = 'POST_' + original[0];
        }
      };
      return this.scanTokens(function(token, i) {
        if (token[0] !== 'IF') {
          return 1;
        }
        original = token;
        this.detectEnd(i + 1, condition, action);
        return 1;
      });
    };

    Rewriter.prototype.indentation = function(origin) {
      var indent, outdent;
      indent = ['INDENT', 2];
      outdent = ['OUTDENT', 2];
      if (origin) {
        indent.generated = outdent.generated = true;
        indent.origin = outdent.origin = origin;
      } else {
        indent.explicit = outdent.explicit = true;
      }
      return [indent, outdent];
    };

    Rewriter.prototype.generate = generate;

    Rewriter.prototype.tag = function(i) {
      var ref;
      return (ref = this.tokens[i]) != null ? ref[0] : void 0;
    };

    return Rewriter;

  })();

  BALANCED_PAIRS = [['(', ')'], ['[', ']'], ['{', '}'], ['INDENT', 'OUTDENT'], ['CALL_START', 'CALL_END'], ['PARAM_START', 'PARAM_END'], ['INDEX_START', 'INDEX_END'], ['STRING_START', 'STRING_END'], ['REGEX_START', 'REGEX_END']];

  exports.INVERSES = INVERSES = {};

  EXPRESSION_START = [];

  EXPRESSION_END = [];

  for (k = 0, len = BALANCED_PAIRS.length; k < len; k++) {
    ref = BALANCED_PAIRS[k], left = ref[0], rite = ref[1];
    EXPRESSION_START.push(INVERSES[rite] = left);
    EXPRESSION_END.push(INVERSES[left] = rite);
  }

  EXPRESSION_CLOSE = ['CATCH', 'THEN', 'ELSE', 'FINALLY'].concat(EXPRESSION_END);

  IMPLICIT_FUNC = ['IDENTIFIER', 'SUPER', ')', 'CALL_END', ']', 'INDEX_END', '@', 'THIS'];

  IMPLICIT_CALL = ['IDENTIFIER', 'NUMBER', 'STRING', 'STRING_START', 'JS', 'REGEX', 'REGEX_START', 'NEW', 'PARAM_START', 'CLASS', 'IF', 'TRY', 'SWITCH', 'THIS', 'BOOL', 'NULL', 'UNDEFINED', 'UNARY', 'YIELD', 'UNARY_MATH', 'SUPER', 'THROW', '@', '->', '=>', '[', '(', '{', '--', '++'];

  IMPLICIT_UNSPACED_CALL = ['+', '-'];

  IMPLICIT_END = ['POST_IF', 'FOR', 'WHILE', 'UNTIL', 'WHEN', 'BY', 'LOOP', 'TERMINATOR'];

  SINGLE_LINERS = ['ELSE', '->', '=>', 'TRY', 'FINALLY', 'THEN'];

  SINGLE_CLOSERS = ['TERMINATOR', 'CATCH', 'FINALLY', 'ELSE', 'OUTDENT', 'LEADING_WHEN'];

  LINEBREAKS = ['TERMINATOR', 'INDENT', 'OUTDENT'];

  CALL_CLOSERS = ['.', '?.', '::', '?::'];

}).call(this);

},{}],27:[function(require,module,exports){
// Generated by CoffeeScript 1.9.3
(function() {
  var Scope,
    indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  exports.Scope = Scope = (function() {
    function Scope(parent, expressions, method, referencedVars) {
      var ref, ref1;
      this.parent = parent;
      this.expressions = expressions;
      this.method = method;
      this.referencedVars = referencedVars;
      this.variables = [
        {
          name: 'arguments',
          type: 'arguments'
        }
      ];
      this.positions = {};
      if (!this.parent) {
        this.utilities = {};
      }
      this.root = (ref = (ref1 = this.parent) != null ? ref1.root : void 0) != null ? ref : this;
    }

    Scope.prototype.add = function(name, type, immediate) {
      if (this.shared && !immediate) {
        return this.parent.add(name, type, immediate);
      }
      if (Object.prototype.hasOwnProperty.call(this.positions, name)) {
        return this.variables[this.positions[name]].type = type;
      } else {
        return this.positions[name] = this.variables.push({
          name: name,
          type: type
        }) - 1;
      }
    };

    Scope.prototype.namedMethod = function() {
      var ref;
      if (((ref = this.method) != null ? ref.name : void 0) || !this.parent) {
        return this.method;
      }
      return this.parent.namedMethod();
    };

    Scope.prototype.find = function(name) {
      if (this.check(name)) {
        return true;
      }
      this.add(name, 'var');
      return false;
    };

    Scope.prototype.parameter = function(name) {
      if (this.shared && this.parent.check(name, true)) {
        return;
      }
      return this.add(name, 'param');
    };

    Scope.prototype.check = function(name) {
      var ref;
      return !!(this.type(name) || ((ref = this.parent) != null ? ref.check(name) : void 0));
    };

    Scope.prototype.temporary = function(name, index, single) {
      if (single == null) {
        single = false;
      }
      if (single) {
        return (index + parseInt(name, 36)).toString(36).replace(/\d/g, 'a');
      } else {
        return name + (index || '');
      }
    };

    Scope.prototype.type = function(name) {
      var i, len, ref, v;
      ref = this.variables;
      for (i = 0, len = ref.length; i < len; i++) {
        v = ref[i];
        if (v.name === name) {
          return v.type;
        }
      }
      return null;
    };

    Scope.prototype.freeVariable = function(name, options) {
      var index, ref, temp;
      if (options == null) {
        options = {};
      }
      index = 0;
      while (true) {
        temp = this.temporary(name, index, options.single);
        if (!(this.check(temp) || indexOf.call(this.root.referencedVars, temp) >= 0)) {
          break;
        }
        index++;
      }
      if ((ref = options.reserve) != null ? ref : true) {
        this.add(temp, 'var', true);
      }
      return temp;
    };

    Scope.prototype.assign = function(name, value) {
      this.add(name, {
        value: value,
        assigned: true
      }, true);
      return this.hasAssignments = true;
    };

    Scope.prototype.hasDeclarations = function() {
      return !!this.declaredVariables().length;
    };

    Scope.prototype.declaredVariables = function() {
      var v;
      return ((function() {
        var i, len, ref, results;
        ref = this.variables;
        results = [];
        for (i = 0, len = ref.length; i < len; i++) {
          v = ref[i];
          if (v.type === 'var') {
            results.push(v.name);
          }
        }
        return results;
      }).call(this)).sort();
    };

    Scope.prototype.assignedVariables = function() {
      var i, len, ref, results, v;
      ref = this.variables;
      results = [];
      for (i = 0, len = ref.length; i < len; i++) {
        v = ref[i];
        if (v.type.assigned) {
          results.push(v.name + " = " + v.type.value);
        }
      }
      return results;
    };

    return Scope;

  })();

}).call(this);

},{}],28:[function(require,module,exports){
// Generated by CoffeeScript 1.9.3
(function() {
  var LineMap, SourceMap;

  LineMap = (function() {
    function LineMap(line1) {
      this.line = line1;
      this.columns = [];
    }

    LineMap.prototype.add = function(column, arg, options) {
      var sourceColumn, sourceLine;
      sourceLine = arg[0], sourceColumn = arg[1];
      if (options == null) {
        options = {};
      }
      if (this.columns[column] && options.noReplace) {
        return;
      }
      return this.columns[column] = {
        line: this.line,
        column: column,
        sourceLine: sourceLine,
        sourceColumn: sourceColumn
      };
    };

    LineMap.prototype.sourceLocation = function(column) {
      var mapping;
      while (!((mapping = this.columns[column]) || (column <= 0))) {
        column--;
      }
      return mapping && [mapping.sourceLine, mapping.sourceColumn];
    };

    return LineMap;

  })();

  SourceMap = (function() {
    var BASE64_CHARS, VLQ_CONTINUATION_BIT, VLQ_SHIFT, VLQ_VALUE_MASK;

    function SourceMap() {
      this.lines = [];
    }

    SourceMap.prototype.add = function(sourceLocation, generatedLocation, options) {
      var base, column, line, lineMap;
      if (options == null) {
        options = {};
      }
      line = generatedLocation[0], column = generatedLocation[1];
      lineMap = ((base = this.lines)[line] || (base[line] = new LineMap(line)));
      return lineMap.add(column, sourceLocation, options);
    };

    SourceMap.prototype.sourceLocation = function(arg) {
      var column, line, lineMap;
      line = arg[0], column = arg[1];
      while (!((lineMap = this.lines[line]) || (line <= 0))) {
        line--;
      }
      return lineMap && lineMap.sourceLocation(column);
    };

    SourceMap.prototype.generate = function(options, code) {
      var buffer, i, j, lastColumn, lastSourceColumn, lastSourceLine, len, len1, lineMap, lineNumber, mapping, needComma, ref, ref1, v3, writingline;
      if (options == null) {
        options = {};
      }
      if (code == null) {
        code = null;
      }
      writingline = 0;
      lastColumn = 0;
      lastSourceLine = 0;
      lastSourceColumn = 0;
      needComma = false;
      buffer = "";
      ref = this.lines;
      for (lineNumber = i = 0, len = ref.length; i < len; lineNumber = ++i) {
        lineMap = ref[lineNumber];
        if (lineMap) {
          ref1 = lineMap.columns;
          for (j = 0, len1 = ref1.length; j < len1; j++) {
            mapping = ref1[j];
            if (!(mapping)) {
              continue;
            }
            while (writingline < mapping.line) {
              lastColumn = 0;
              needComma = false;
              buffer += ";";
              writingline++;
            }
            if (needComma) {
              buffer += ",";
              needComma = false;
            }
            buffer += this.encodeVlq(mapping.column - lastColumn);
            lastColumn = mapping.column;
            buffer += this.encodeVlq(0);
            buffer += this.encodeVlq(mapping.sourceLine - lastSourceLine);
            lastSourceLine = mapping.sourceLine;
            buffer += this.encodeVlq(mapping.sourceColumn - lastSourceColumn);
            lastSourceColumn = mapping.sourceColumn;
            needComma = true;
          }
        }
      }
      v3 = {
        version: 3,
        file: options.generatedFile || '',
        sourceRoot: options.sourceRoot || '',
        sources: options.sourceFiles || [''],
        names: [],
        mappings: buffer
      };
      if (options.inline) {
        v3.sourcesContent = [code];
      }
      return JSON.stringify(v3, null, 2);
    };

    VLQ_SHIFT = 5;

    VLQ_CONTINUATION_BIT = 1 << VLQ_SHIFT;

    VLQ_VALUE_MASK = VLQ_CONTINUATION_BIT - 1;

    SourceMap.prototype.encodeVlq = function(value) {
      var answer, nextChunk, signBit, valueToEncode;
      answer = '';
      signBit = value < 0 ? 1 : 0;
      valueToEncode = (Math.abs(value) << 1) + signBit;
      while (valueToEncode || !answer) {
        nextChunk = valueToEncode & VLQ_VALUE_MASK;
        valueToEncode = valueToEncode >> VLQ_SHIFT;
        if (valueToEncode) {
          nextChunk |= VLQ_CONTINUATION_BIT;
        }
        answer += this.encodeBase64(nextChunk);
      }
      return answer;
    };

    BASE64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';

    SourceMap.prototype.encodeBase64 = function(value) {
      return BASE64_CHARS[value] || (function() {
        throw new Error("Cannot Base64 encode value: " + value);
      })();
    };

    return SourceMap;

  })();

  module.exports = SourceMap;

}).call(this);

},{}],29:[function(require,module,exports){
(function (global){
/*
 * hi-base64 v0.1.3
 * https://github.com/emn178/hi-base64
 *
 * Copyright 2014-2015, emn178@gmail.com
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
 */
;(function(root, undefined) {
  'use strict';

  var BASE64_ENCODE_CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'.split('');
  var BASE64_DECODE_CHAR = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
    'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 
    'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 
    'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 
    'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 
    'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 
    'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, 
    '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63, '-': 62,
    '_': 63
  };

  var encodeAsBytes = function(str) {
    var bytes = [];
    for (var i = 0;i < str.length; i++) {
      var c = str.charCodeAt(i);
      if (c < 0x80) {
        bytes[bytes.length] = c;
      } else if (c < 0x800) {
        bytes[bytes.length] = 0xc0 | (c >> 6);
        bytes[bytes.length] = 0x80 | (c & 0x3f);
      } else if (c < 0xd800 || c >= 0xe000) {
        bytes[bytes.length] = 0xe0 | (c >> 12);
        bytes[bytes.length] = 0x80 | ((c >> 6) & 0x3f);
        bytes[bytes.length] = 0x80 | (c & 0x3f);
      } else {
        c = 0x10000 + (((c & 0x3ff) << 10) | (str.charCodeAt(++i) & 0x3ff));
        bytes[bytes.length] = 0xf0 | (c >> 18);
        bytes[bytes.length] = 0x80 | ((c >> 12) & 0x3f);
        bytes[bytes.length] = 0x80 | ((c >> 6) & 0x3f);
        bytes[bytes.length] = 0x80 | (c & 0x3f);
      }
    }
    return bytes;
  };

  var decodeAsBytes = function(base64Str) {
    var v1, v2, v3, v4, bytes = [], index = 0, length = base64Str.length;
    if(base64Str.charAt(length - 2) == '=') {
      length -= 2;
    } else if(base64Str.charAt(length - 1) == '=') {
      length -= 1;
    }

    // 4 char to 3 bytes
    for(var i = 0, count = length >> 2 << 2;i < count;) {
      v1 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
      v2 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
      v3 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
      v4 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
      bytes[index++] = (v1 << 2 | v2 >>> 4) & 255;
      bytes[index++] = (v2 << 4 | v3 >>> 2) & 255;
      bytes[index++] = (v3 << 6 | v4) & 255;
    }

    // remain bytes
    var remain = length - count;
    if(remain == 2) {
      v1 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
      v2 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
      bytes[index++] = (v1 << 2 | v2 >>> 4) & 255;
    } else if(remain == 3) {
      v1 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
      v2 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
      v3 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
      bytes[index++] = (v1 << 2 | v2 >>> 4) & 255;
      bytes[index++] = (v2 << 4 | v3 >>> 2) & 255;
    }
    return bytes;
  };

  if(typeof(module) != 'undefined') {
    root = global;
  }
  var btoa = root.btoa, atob = root.atob, utf8Base64Encode, utf8Base64Decode;
  // node.js
  if(!root.HI_BASE64_TEST && typeof(module) != 'undefined') {
    var Buffer = require('buffer').Buffer;
    btoa = function(str) {
      return new Buffer(str, 'ascii').toString('base64');
    };

    utf8Base64Encode = function(str) {
      return new Buffer(str).toString('base64');
    };

    atob = function(base64Str) {
      return new Buffer(base64Str, 'base64').toString('ascii');
    };

    utf8Base64Decode = function(base64Str) {
      return new Buffer(base64Str, 'base64').toString();
    };
  } else if(!btoa) {
    btoa = function(str) {
      var v1, v2, v3, base64Str = '', length = str.length;
      for(var i = 0, count = parseInt(length / 3) * 3;i < count;) {
        v1 = str.charCodeAt(i++);
        v2 = str.charCodeAt(i++);
        v3 = str.charCodeAt(i++);
        base64Str += BASE64_ENCODE_CHAR[v1 >>> 2] +
                     BASE64_ENCODE_CHAR[(v1 << 4 | v2 >>> 4) & 63] +
                     BASE64_ENCODE_CHAR[(v2 << 2 | v3 >>> 6) & 63] +
                     BASE64_ENCODE_CHAR[v3 & 63];
      }
      
      // remain char
      var remain = length - count;
      if(remain == 1) {
        v1 = str.charCodeAt(i);
        base64Str += BASE64_ENCODE_CHAR[v1 >>> 2] +
                     BASE64_ENCODE_CHAR[(v1 << 4) & 63] +
                     '==';
      } else if(remain == 2) {
        v1 = str.charCodeAt(i++);
        v2 = str.charCodeAt(i);
        base64Str += BASE64_ENCODE_CHAR[v1 >>> 2] +
                     BASE64_ENCODE_CHAR[(v1 << 4 | v2 >>> 4) & 63] +
                     BASE64_ENCODE_CHAR[(v2 << 2) & 63] +
                     '=';
      }
      return base64Str;
    };

    utf8Base64Encode = function(str) {
      var v1, v2, v3, base64Str = '', bytes = encodeAsBytes(str), length = bytes.length;
      for(var i = 0, count = parseInt(length / 3) * 3;i < count;) {
        v1 = bytes[i++];
        v2 = bytes[i++];
        v3 = bytes[i++];
        base64Str += BASE64_ENCODE_CHAR[v1 >>> 2] +
                     BASE64_ENCODE_CHAR[(v1 << 4 | v2 >>> 4) & 63] +
                     BASE64_ENCODE_CHAR[(v2 << 2 | v3 >>> 6) & 63] +
                     BASE64_ENCODE_CHAR[v3 & 63];
      }
      
      // remain char
      var remain = length - count;
      if(remain == 1) {
        v1 = bytes[i];
        base64Str += BASE64_ENCODE_CHAR[v1 >>> 2] +
                     BASE64_ENCODE_CHAR[(v1 << 4) & 63] +
                     '==';
      } else if(remain == 2) {
        v1 = bytes[i++];
        v2 = bytes[i];
        base64Str += BASE64_ENCODE_CHAR[v1 >>> 2] +
                     BASE64_ENCODE_CHAR[(v1 << 4 | v2 >>> 4) & 63] +
                     BASE64_ENCODE_CHAR[(v2 << 2) & 63] +
                     '=';
      }
      return base64Str;
    };

    atob = function(base64Str) {
      var v1, v2, v3, v4, str = '', length = base64Str.length;
      if(base64Str.charAt(length - 2) == '=') {
        length -= 2;
      } else if(base64Str.charAt(length - 1) == '=') {
        length -= 1;
      }

      // 4 char to 3 bytes
      for(var i = 0, count = length >> 2 << 2;i < count;) {
        v1 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
        v2 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
        v3 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
        v4 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
        str += String.fromCharCode((v1 << 2 | v2 >>> 4) & 255) +
               String.fromCharCode((v2 << 4 | v3 >>> 2) & 255) +
               String.fromCharCode((v3 << 6 | v4) & 255);
      }

      // remain bytes
      var remain = length - count;
      if(remain == 2) {
        v1 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
        v2 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
        str += String.fromCharCode((v1 << 2 | v2 >>> 4) & 255);
      } else if(remain == 3) {
        v1 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
        v2 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
        v3 = BASE64_DECODE_CHAR[base64Str.charAt(i++)];
        str += String.fromCharCode((v1 << 2 | v2 >>> 4) & 255) +
               String.fromCharCode((v2 << 4 | v3 >>> 2) & 255);
      }
      return str;
    };

    utf8Base64Decode = function(base64Str) {
      var str = '', bytes = decodeAsBytes(base64Str), length = bytes.length;
      var i = 0, followingChars = 0, b, c;
      while(i < length) {
        b = bytes[i++];
        if(b <= 0x7F) {
          str += String.fromCharCode(b);
          continue;
        } else if(b > 0xBF && b <= 0xDF) {
          c = b & 0x1F;
          followingChars = 1;
        } else if(b <= 0xEF) {
          c = b & 0x0F;
          followingChars = 2;
        } else if(b <= 0xF7) {
          c = b & 0x07;
          followingChars = 3;
        } else {
          throw 'not a UTF-8 string';
        }

        for(var j = 0;j < followingChars;++j) {
          b = bytes[i++];
          if (b < 0x80 || b > 0xBF) {
            throw 'not a UTF-8 string';
          }
          c <<= 6;
          c += b & 0x3F;
        }
        if (c >= 0xD800 && c <= 0xDFFF) {
          throw 'not a UTF-8 string';
        }
        if (c > 0x10FFFF) {
          throw 'not a UTF-8 string';
        }

        if (c <= 0xFFFF) {
          str += String.fromCharCode(c);
        } else {
          c -= 0x10000;
          str += String.fromCharCode((c >> 10) + 0xD800);
          str += String.fromCharCode((c & 0x3FF) + 0xDC00);
        }
      }
      return str;
    };
  } else {
    utf8Base64Encode = function(str) {
      var result = '';
      for (var i=0;i < str.length; i++) {
        var charcode = str.charCodeAt(i);
        if (charcode < 0x80) {
          result += String.fromCharCode(charcode);
        } else if (charcode < 0x800) {
          result += String.fromCharCode(0xc0 | (charcode >> 6)) +
                    String.fromCharCode(0x80 | (charcode & 0x3f));
        } else if (charcode < 0xd800 || charcode >= 0xe000) {
          result += String.fromCharCode(0xe0 | (charcode >> 12)) +
                    String.fromCharCode(0x80 | ((charcode >> 6) & 0x3f)) +
                    String.fromCharCode(0x80 | (charcode & 0x3f));
        } else {
          charcode = 0x10000 + (((charcode & 0x3ff) << 10) | (str.charCodeAt(++i) & 0x3ff));
          result += String.fromCharCode(0xf0 | (charcode >> 18)) +
                    String.fromCharCode(0x80 | ((charcode >> 12) & 0x3f)) +
                    String.fromCharCode(0x80 | ((charcode >> 6) & 0x3f)) +
                    String.fromCharCode(0x80 | (charcode & 0x3f));
        }
      }
      return btoa(result);
    };

    utf8Base64Decode = function(base64Str) {
      var tmpStr = atob(base64Str.trim('=').replace(/-/g, '+').replace(/_/g, '/'));
      if(!/[^\x00-\x7F]/.test(tmpStr)) {
        return tmpStr;
      }
      var str = '', i = 0, length = tmpStr.length, followingChars = 0, b, c;
      while(i < length) {
        b = tmpStr.charCodeAt(i++);
        if(b <= 0x7F) {
          str += String.fromCharCode(b);
          continue;
        } else if(b > 0xBF && b <= 0xDF) {
          c = b & 0x1F;
          followingChars = 1;
        } else if(b <= 0xEF) {
          c = b & 0x0F;
          followingChars = 2;
        } else if(b <= 0xF7) {
          c = b & 0x07;
          followingChars = 3;
        } else {
          throw 'not a UTF-8 string';
        }

        for(var j = 0;j < followingChars;++j) {
          b = tmpStr.charCodeAt(i++);
          if (b < 0x80 || b > 0xBF) {
            throw 'not a UTF-8 string';
          }
          c <<= 6;
          c += b & 0x3F;
        }
        if (c >= 0xD800 && c <= 0xDFFF) {
          throw 'not a UTF-8 string'; 
        }
        if (c > 0x10FFFF) {
          throw 'not a UTF-8 string';
        }

        if (c <= 0xFFFF) {
          str += String.fromCharCode(c);
        } else {
          c -= 0x10000;
          str += String.fromCharCode((c >> 10) + 0xD800);
          str += String.fromCharCode((c & 0x3FF) + 0xDC00);
        }
      }
      return str;
    };
  }
  
  var encode = function(str, asciiOnly) {
    if(!asciiOnly && /[^\x00-\x7F]/.test(str)) {
      return utf8Base64Encode(str);
    } else {
      return btoa(str);
    }
  };

  var decode = function(base64Str, asciiOnly) {
    return asciiOnly ? atob(base64Str) : utf8Base64Decode(base64Str);
  };

  var exports = {
    encode: encode,
    decode: decode,
    encodeAsBytes: encodeAsBytes,
    decodeAsBytes: decodeAsBytes,
    atob: atob,
    btoa: btoa
  };

  if(typeof(module) != 'undefined') {
    module.exports = exports;
  } else if(root) {
    root.base64 = exports;
  }
}(this));

}).call(this,typeof global !== "undefined" ? global : typeof self !== "undefined" ? self : typeof window !== "undefined" ? window : {})
},{"buffer":3}],30:[function(require,module,exports){
window.addEventListener("load", function() {
  var CodeMirror, base64, cjsxfy, codeStr, coffeeify, convertFunction, editorTextArea, langStr, resultFrame, run, runButton, scriptCodeMirror, scriptObject;
  console.log('ready for coder ?');

  /*
  			Import CodeMirror
   */
  CodeMirror = require('codemirror');
  base64 = require('hi-base64');

  /*
  			Install iframe
   */
  resultFrame = document.getElementById('result');
  console.log(["resultFrame is ", resultFrame]);
  console.log(resultFrame.contentDocument.head);

  /*
  			Install editor
   */
  editorTextArea = document.getElementById('editor');
  scriptObject = {
    lineNumbers: true,
    mode: "javascript"
  };
  scriptCodeMirror = CodeMirror.fromTextArea(editorTextArea, scriptObject);
  langStr = "js";
  convertFunction = null;
  if (langStr === "js") {
    codeStr = "//Debug\n";
    codeStr += "console.log('ready for js ?')\n";
    codeStr += "\n//Define\n";
    codeStr += "function myFunc(){return 100;};\n";
    codeStr += "\n//test require\n";
    codeStr += "lodash=require('lodash')\n";
    codeStr += "\n//return\n";
    codeStr += "myFunc()\n";
    convertFunction = eval;
  } else if (langStr === "coffee") {
    codeStr = "#Debug\n";
    codeStr += "console.log('ready for coffee ?')\n";
    codeStr += "\n#Define\n";
    codeStr += "myFunc= ()->return 100";
    codeStr += "\nreturn myFunc()";
    codeStr += "\n#test require\n";
    codeStr += "lodash = require 'lodash'\n";
    codeStr += "\n#Debug\n";
    codeStr += "console.log lodash\n";
    coffeeify = require('coffee-script');
    convertFunction = function(string, options) {
      var transformStr;
      console.log("convert coffee, string is " + string);
      transformStr = coffeeify.compile(string);
      console.log('transformStr is : \n' + transformStr);
      return eval(transformStr);
    };
  } else if (langStr === "cjsx") {
    cjsxfy = require('coffee-react-transform');
    coffeeify = require('coffee-script');
    console.log("cjsxfy is " + cjsxfy);
    convertFunction = function(string, options) {
      var transformStr;
      console.log("convert cjsx, string is " + string);
      transformStr = coffeeify.compile(cjsxfy(string, options));
      console.log('transformStr is : \n' + transformStr);
      return eval(transformStr);
    };

    /*
    			#require
    			#fs = require('browserify-fs')
    			fs = require('brfs')
    
    			#Debug
    			console.log "fs is "+fs
    			#console.log "fs.readFileSync is "+ fs.readFileSync
    
    			#read
    			codeStr = fs.readFileSync(
    							'../Reacter/src.cjsx'
    						)
     */
    codeStr = "#Debug\n";
    codeStr += "console.log(\"ready for coffee-react ?\")\n";
    codeStr += "\n#require #NB it is important to call it as Reat and not react\n";
    codeStr += "React = require('react')\n";
    codeStr += "\n#test\n";
    codeStr += "console.log React\n";
    codeStr += "\n#create";
    codeStr += "Hello = React.createClass\n ";
    codeStr += "\t render: -> <div>Hello {this.props.name}</div>\n";
    codeStr += "\n#test\n";
    codeStr += "console.log document.getElementById('example')\n";
    codeStr += "\n#render\n";
    codeStr += "React.render(<Hello name='John' />, document.getElementById('example'));\n";
  }
  scriptCodeMirror.setValue(codeStr);

  /*
  			Define submit
   */
  runButton = document.getElementById('run');
  run = function() {
    var scriptStr, sourceStr, stdOutStr;
    scriptCodeMirror.save();
    scriptStr = editorTextArea.value;
    console.log("convertFunction is " + convertFunction);
    stdOutStr = String(convertFunction(editorTextArea.value));
    console.log("stdOutStr is :\n' " + stdOutStr + "' ");
    sourceStr = base64.encode(stdOutStr);
    console.log(resultFrame.contentDocument.body);
    return resultFrame.contentDocument.body.innerHTML += "<br> >" + stdOutStr;
  };
  return runButton.addEventListener("click", run);
});


},{"codemirror":11,"coffee-react-transform":12,"coffee-script":20,"hi-base64":29}]},{},[1]);
