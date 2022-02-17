
RGraph=window.RGraph||{isrgraph:true,isRGraph:true,rgraph:true};RGraph.Segmented=function(conf)
{var id=conf.id,canvas=document.getElementById(id),min=conf.min,max=conf.max,value=conf.value;this.id=id;this.canvas=canvas;this.context=this.canvas.getContext?this.canvas.getContext("2d",{alpha:(typeof id==='object'&&id.alpha===false)?false:true}):null;this.canvas.__object__=this;this.type='segmented';this.min=RGraph.stringsToNumbers(min);this.max=RGraph.stringsToNumbers(max);this.value=RGraph.stringsToNumbers(value);this.centerx=null;this.centery=null;this.radius=null;this.isRGraph=true;this.isrgraph=true;this.rgraph=true;this.currentValue=null;this.uid=RGraph.createUID();this.canvas.uid=this.canvas.uid?this.canvas.uid:RGraph.createUID();this.colorsParsed=false;this.coordsText=[];this.original_colors=[];this.firstDraw=true;if(this.value<=0.0000001){this.value=0.0000001;}
this.properties={radius:null,centerx:null,centery:null,width:null,marginLeft:15,marginRight:15,marginTop:15,marginBottom:15,backgroundColor:'black',colors:['red','#ddd'],textFont:'Arial, Verdana, sans-serif',textSize:null,textColor:'gray',textBold:false,textItalic:false,textAccessible:true,textAccessibleOverflow:'visible',textAccessiblePointerevents:false,labelsCenterFont:null,labelsCenterSize:null,labelsCenterColor:null,labelsCenterBold:null,labelsCenterItalic:null,labelsCenterUnitsPre:'',labelsCenterUnitsPost:'',labelsCenterDecimals:0,labelsCenterPoint:'.',labelsCenterThousand:',',labelsCenterSpecific:'',labelsCenterSpecificFormattedDecimals:0,labelsCenterSpecificFormattedPoint:'.',labelsCenterSpecificFormattedThousand:',',labelsCenterSpecificFormattedUnitsPre:'',labelsCenterSpecificFormattedUnitsPost:'',labelsCenterOffsetx:0,labelsCenterOffsety:0,radialsCount:36,contextmenu:null,annotatable:false,annotatableColor:'black',adjustable:false,effectRoundrobinMultiplier:1,clearto:'rgba(0,0,0,0)'}
if(!this.canvas){alert('[SDONUT] No canvas support');return;}
var properties=this.properties;this.path=RGraph.pathObjectFunction;if(RGraph.Effects&&typeof RGraph.Effects.decorate==='function'){RGraph.Effects.decorate(this);}
this.responsive=RGraph.responsive;this.set=function(name)
{var value=typeof arguments[1]==='undefined'?null:arguments[1];if(arguments.length===1&&typeof arguments[0]==='object'){for(i in arguments[0]){if(typeof i==='string'){this.set(i,arguments[0][i]);}}
return this;}
properties[name]=value;return this;};this.get=function(name)
{return properties[name];};this.draw=function()
{RGraph.fireCustomEvent(this,'onbeforedraw');if(!this.canvas.__rgraph_aa_translated__){this.context.translate(0.5,0.5);this.canvas.__rgraph_aa_translated__=true;}
if(this.value>this.max)this.value=this.max;if(this.value<this.min)this.value=this.min;this.currentValue=this.value;this.marginLeft=properties.marginLeft;this.marginRight=properties.marginRight;this.marginTop=properties.marginTop;this.marginBottom=properties.marginBottom;this.centerx=((this.canvas.width-this.marginLeft-this.marginRight)/2)+this.marginLeft;this.centery=((this.canvas.height-this.marginBottom-this.marginTop)/2)+this.marginTop;this.radius=Math.min((this.canvas.width-this.marginLeft-this.marginRight)/2,(this.canvas.height-this.marginTop-this.marginBottom)/2);this.coordsText=[];if(typeof properties.centerx==='number')this.centerx=properties.centerx;if(typeof properties.centery==='number')this.centery=properties.centery;if(typeof properties.radius==='number')this.radius=properties.radius;if(!this.colorsParsed){this.parseColors();this.colorsParsed=true;}
this.drawMeter();this.drawLabel();if(properties.contextmenu){RGraph.showContext(this);}
RGraph.installEventListeners(this);if(this.firstDraw){this.firstDraw=false;RGraph.fireCustomEvent(this,'onfirstdraw');this.firstDrawFunc();}
RGraph.fireCustomEvent(this,'ondraw');return this;};this.exec=function(func)
{func(this);return this;};this.drawMeter=function()
{var width=typeof properties.width==='number'?properties.width:this.radius/2;if(typeof properties.width==='string'){width+=Number(properties.width);}
if(properties.backgroundColor){this.path('fs % fr -5 -5 % %',properties.backgroundColor,this.canvas.width+10,this.canvas.height+10);}
var degrees=360/properties.radialsCount;degrees/=2,colored=Math.round(((this.value-this.min)/(this.max-this.min))*(properties.radialsCount*2));for(var i=1;i<(properties.radialsCount*2);i+=2){var start=(RGraph.toRadians((i*degrees)-(degrees/2))*properties.effectRoundrobinMultiplier)-RGraph.HALFPI,end=(RGraph.toRadians((i*degrees)+(degrees/2))*properties.effectRoundrobinMultiplier)-RGraph.HALFPI;this.path('b a % % % % % false a % % % % % true f % ',this.centerx,this.centery,this.radius,start,end,this.centerx,this.centery,this.radius-width,end,start,i>=colored?properties.colors[1]:properties.colors[0]);}
this.context.lineWidth=1;};this.drawLabel=function()
{if(RGraph.isNull(properties.textSize)){properties.textSize=this.radius/2.5;}
var textConf=RGraph.getTextConf({object:this,prefix:'labelsCenter'});if(properties.labelsCenterSpecific&&properties.labelsCenterSpecific.length){properties.labelsCenterSpecific=RGraph.labelSubstitution({object:this,text:properties.labelsCenterSpecific,index:0,value:this.value,decimals:properties.labelsCenterSpecificFormattedDecimals||0,unitsPre:properties.labelsCenterSpecificFormattedUnitsPre||'',unitsPost:properties.labelsCenterSpecificFormattedUnitsPost||'',thousand:properties.labelsCenterSpecificFormattedThousand||',',point:properties.labelsCenterSpecificFormattedPoint||'.'});}
RGraph.text({object:this,font:textConf.font,italic:textConf.italic,bold:textConf.bold,size:textConf.size,color:textConf.color,x:this.centerx+properties.labelsCenterOffsetx,y:this.centery+properties.labelsCenterOffsety,text:properties.labelsCenterSpecific?properties.labelsCenterSpecific:RGraph.numberFormat({object:this,number:(this.value*properties.effectRoundrobinMultiplier).toFixed(properties.labelsCenterDecimals),unitspre:properties.labelsCenterUnitsPre,unitspost:properties.labelsCenterUnitsPost,point:properties.labelsCenterPoint,thousand:properties.labelsCenterThousand}),halign:'center',valign:'center',accessible:properties.textAccessible});};this.getShape=function(e){};this.getValue=function(e)
{if(typeof e==='number'){angle=e;}else{var mouseXY=RGraph.getMouseXY(e);var angle=RGraph.getAngleByXY(this.centerx,this.centery,mouseXY[0],mouseXY[1]);}
angle+=RGraph.HALFPI;if(angle>RGraph.TWOPI){angle-=RGraph.TWOPI;}
var value=((angle/RGraph.TWOPI)*(this.max-this.min))+this.min;value=Math.max(value,this.min);value=Math.min(value,this.max);return value;};this.getObjectByXY=function(e)
{var mouseXY=RGraph.getMouseXY(e),width=properties.width;var radius=RGraph.getHypLength(this.centerx,this.centery,mouseXY[0],mouseXY[1]);if(typeof width==='string'){width=(this.radius/2)+parseFloat(width);}else if(RGraph.isNull(width)){width=this.radius/2;}
if(radius>this.radius||radius<(this.radius-width)){return null;}
return this;};this.adjusting_mousemove=function(e)
{if(properties.adjustable&&RGraph.Registry.get('adjusting')&&RGraph.Registry.get('adjusting').uid==this.uid){this.value=this.getValue(e);RGraph.clear(this.canvas);RGraph.redrawCanvas(this.canvas);RGraph.fireCustomEvent(this,'onadjust');}};this.getAngle=function(value)
{if(typeof value==='number'){if(value>this.max||value<this.min){return null;}
var angle=(((value-this.min)/(this.max-this.min))*RGraph.TWOPI)-RGraph.HALFPI;if(value===this.max)angle-=0.00001;if(value===this.min)angle+=0.00001;}else{var mouseX=value.offsetX,mouseY=value.offsetY;var angle=RGraph.getAngleByXY({cx:this.centerx,cy:this.centery,x:mouseX,y:mouseY});if(angle>(RGraph.PI+RGraph.HALFPI)){angle-=RGraph.TWOPI;}}
return angle;};this.parseColors=function()
{if(this.original_colors.length===0){this.original_colors.backgroundColor=RGraph.arrayClone(properties.backgroundColor);this.original_colors.colors=RGraph.arrayClone(properties.colors);}
properties.backgroundColor=this.parseSingleColorForGradient(properties.backgroundColor);var colors=properties.colors;if(colors&&colors.length){for(var i=0;i<colors.length;++i){colors[i]=this.parseSingleColorForGradient(colors[i]);}}};this.reset=function()
{};this.parseSingleColorForGradient=function(color)
{if(!color||typeof color!='string'){return color;}
if(color.match(/^gradient\((.*)\)$/i)){if(color.match(/^gradient\(({.*})\)$/i)){return RGraph.parseJSONGradient({object:this,def:RegExp.$1,radial:true});}
var parts=RegExp.$1.split(':');var grad=this.context.createLinearGradient(properties.marginLeft,0,this.canvas.width-properties.marginLeft-properties.marginRight,0);var diff=1/(parts.length-1);grad.addColorStop(0,RGraph.trim(parts[0]));for(var j=1,len=parts.length;j<len;++j){grad.addColorStop(j*diff,RGraph.trim(parts[j]));}}
return grad?grad:color;};this.on=function(type,func)
{if(type.substr(0,2)!=='on'){type='on'+type;}
if(typeof this[type]!=='function'){this[type]=func;}else{RGraph.addCustomEventListener(this,type,func);}
return this;};this.firstDrawFunc=function()
{};this.grow=function()
{var obj=this;obj.currentValue=obj.currentValue||obj.min;var opt=arguments[0]||{},frames=opt.frames||30,frame=0,diff=obj.value-obj.currentValue,step=diff/frames,callback=arguments[1]||function(){},initial=obj.currentValue
function iterator()
{obj.value=initial+(frame++ *step);RGraph.clear(obj.canvas);RGraph.redrawCanvas(obj.canvas);if(frame<=frames){RGraph.Effects.updateCanvas(iterator);}else{callback(obj);}}
iterator();return this;};this.roundrobin=this.roundRobin=function()
{var obj=this,opt=arguments[0]||{},callback=arguments[1]||function(){},frame=0,frames=opt.frames||30,radius=this.radius;var iterator=function()
{obj.set({effectRoundrobinMultiplier:RGraph.Effects.getEasingMultiplier(frames,frame)});RGraph.redrawCanvas(obj.canvas);if(frame<frames){RGraph.Effects.updateCanvas(iterator);frame++;}else{RGraph.redrawCanvas(obj.canvas);callback(obj);}};iterator();return this;};RGraph.register(this);RGraph.parseObjectStyleConfig(this,conf.options);};