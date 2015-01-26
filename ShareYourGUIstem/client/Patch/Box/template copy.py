<template name="Box">

	{{#if IsNoderBool}}
	    <rect 
	    		id="Box_{{_id}}" 
	    		class="Box" data-id="{{_id}}"
	    		x="{{x}}" y="{{y}}" 
	    		rx="20" ry="20"
	    		style="fill:red;stroke:black;stroke-width:5;opacity:0.5"
	            width="100" height="50" 
	    />
	    <foreignobject 
	    		x="{{x}}" y="{{y}}" 
	    		width="90" height="40"
	    		border="1"
	    >
	    	<body xmlns="http://www.w3.org/1999/xhtml">
	     		<div>
	     			<table>
	     				<tr>
	     					<td align="center">	
		      					{{NodeKeyStr}}
		      				</td>
		      			</tr>
		      		</table>
	      		</div>
	   		</body>
	    </foreignobject>
    {{/if}}

    {{#if IsOrderedDictBool}}
	    <circle 
	    		id="Box_{{_id}}" cx="{{x}}" cy="{{y}}" 
	            class="Box" data-id="{{_id}}"
	            r="10"
	    />
	    <foreignobject 
	    		x="{{x}}" y="{{y}}" 
	    		width="50" height="40"
	    		border="1"
	    >
	    	<body xmlns="http://www.w3.org/1999/xhtml">
	     		<div>
	     			<table>
		      			{{NodeCollectionStr}}
		      		</table>
	      		</div>
	   		</body>
	    </foreignobject>
    {{/if}}

</template>
