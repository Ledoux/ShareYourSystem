/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

subscribe

*/

Router.route('/')

Router.map(function () {
  this.route('Interface');
});

Router.route('/View', function () {
  this.render('View');
});

Router.route('/Music', function () {
  this.render('Music');
});
