(function(g){g.fn.gracket=function(q){g.fn.gracket.defaults={gracketClass:"g_gracket",gameClass:"g_game",roundClass:"g_round",roundLabelClass:"g_round_label",teamClass:"g_team",winnerClass:"g_winner",spacerClass:"g_spacer",currentClass:"g_current",seedClass:"g_seed",cornerRadius:15,canvasId:"g_canvas",canvasClass:"g_canvas",canvasLineColor:"#eee",canvasLineCap:"round",canvasLineWidth:2,canvasLineGap:15,roundLabels:[],src:[]};var j=this,k="undefined"===typeof j.data("gracket")?[]:JSON.parse(j.data("gracket")),
r,y,z,u=[];g.fn.gracket.settings={};var A={init:function(a){this.gracket.settings=g.extend({},this.gracket.defaults,a);this.gracket.settings.src.length&&(k=this.gracket.settings.src);this.gracket.settings.canvasId=this.gracket.settings.canvasId+"_"+(new Date).getTime();a=document.createElement("canvas");a.id=this.gracket.settings.canvasId;a.className=this.gracket.settings.canvasClass;a.style.position="absolute";a.style.left=0;a.style.top=0;a.style.right="auto";j.addClass(this.gracket.settings.gracketClass).prepend(a);
y=k.length;for(a=0;a<y;a++){var d=m.build.round(this.gracket.settings);j.append(d);z=k[a].length;for(var b=0;b<z;b++){var c=m.build.game(this.gracket.settings),f=j.find("."+this.gracket.settings.gameClass).outerHeight(!0),f=m.build.spacer(this.gracket.settings,f,a,0!==a&&0===b?!0:!1);0==b%1&&0!==a&&d.append(f);d.append(c);r=k[a][b].length;for(f=0;f<r;f++){var h=m.build.team(k[a][b][f],this.gracket.settings);c.append(h);h=h.outerWidth(!0);if(void 0===u[a]||u[a]<h)u[a]=h;1===r&&(c.prev().remove(),m.align.winner(c,
this.gracket.settings,c.parent().prev().children().eq(0).height()),m.listeners(this.gracket.settings,k,c.parent().prev().children().eq(1)))}}}}},m={build:{team:function(a,d){var b=["<h3"+("undefined"===typeof a.score?"":' title="Score: '+a.score+'"')+">",'<span class="'+d.seedClass+'">',"undefined"===typeof a.displaySeed?a.seed:a.displaySeed,"</span>","&nbsp;"+a.name+"&nbsp;","<small>","undefined"===typeof a.score?"":a.score,"</small></h3>"].join("");return team=g("<div />",{html:b,"class":d.teamClass+
" "+(a.id||"id_null")})},game:function(a){return game=g("<div />",{"class":a.gameClass})},round:function(a){return round=g("<div />",{"class":a.roundClass})},spacer:function(a,d,b,c){return spacer=g("<div />",{"class":a.spacerClass}).css({height:c?(Math.pow(2,b)-1)*(d/2):(Math.pow(2,b)-1)*d})},labels:function(a,d){var b,c=a.length,f,h=0;for(b=0;b<c;b++)f=0===b?d.padding+h:d.padding+h+d.right*b,g("<h5 />",{html:d.labels.length?d.labels[b]:"Round "+(b+1),"class":d["class"]}).css({position:"absolute",
left:f,width:d.width}).prependTo(j),h+=u[b]},canvas:{resize:function(a){a=document.getElementById(a.canvasId);a.height=j.innerHeight();a.width=j.innerWidth();g(a).css({height:j.innerHeight(),width:j.innerWidth(),zIndex:1,pointerEvents:"none"})},draw:function(a,d,b){var c=document.getElementById(a.canvasId);"undefined"!=typeof G_vmlCanvasManager&&G_vmlCanvasManager.initElement(c);var c=c.getContext("2d"),f=u[0],h=b.outerHeight(!0),k=parseInt(j.css("paddingLeft"))||0,q=parseInt(j.css("paddingTop"))||
0;parseInt(b.css("marginBottom"));var r=f+k,s=parseInt(j.find("> div").css("marginRight"))||0,e=a.cornerRadius,v=a.canvasLineGap,A=b.height()-2*b.find("> div").eq(1).height();_playerHt=b.find("> div").eq(1).height();_totalItemWidth=0;"undefined"!==typeof console&&console.info("Padding Left: "+k+"px","Player/Name Width: "+f+"px","Container padding left: "+r+"px");e>h/3&&(e=h/3);e>s/2&&(e=s/2-2);0>=e&&(e=1);v>s/3&&(v=s/3);c.strokeStyle=a.canvasLineColor;c.lineCap=a.canvasLineCap;c.lineWidth=a.canvasLineWidth;
c.beginPath();b=Math.pow(2,d.length-2);var n=0,B,y=0.5,C=0===n&&1===b?!0:!1;if(C)var D=g("."+a.gameClass),f=D.eq(D.length-1),h=f.outerHeight(!0),f=f.outerWidth(!0);for(;1<=b;){for(B=0;B<b;B++){1==b&&(y=1);var p=C?f+k:r+_totalItemWidth+n*s,w=y*s,l=((Math.pow(2,n-1)-0.5)*(n&&1)+B*Math.pow(2,n))*h+q+(C?D.find("> div").eq(1).height():_playerHt)+A/2;1<b?(c.moveTo(p+v,l),c.lineTo(p+w-e,l)):(c.moveTo(p+v,l),c.lineTo(p+3*v,l));if(1<b&&0==B%2){var z=l+e,E=l+Math.pow(2,n)*h-e;c.moveTo(p+w,z);c.lineTo(p+w,E);
var x=p+w-e,t=l+e;c.moveTo(x,t-e);c.arcTo(x+e,t-e,x+e,t,e);t=l+Math.pow(2,n)*h-e;c.moveTo(x+e,t-e);c.arcTo(x+e,t+e,x,t+e,e);l=(z+E)/2;c.moveTo(p+w,l);c.lineTo(p+w+v,l)}}n++;f=u[n];_totalItemWidth+=f;b/=2}c.stroke();m.build.labels(d,{padding:k,left:r,right:s,labels:a.roundLabels,"class":a.roundLabelClass})}}},align:{winner:function(a,d,b){b=1===a.parent().siblings().not("canvas").length?b-(a.height()+a.height()/2):b+a.height()/2;return a.addClass(d.winnerClass).css({"margin-top":b})}},listeners:function(a,
d,b){g.each(g("."+a.teamClass+" > h3"),function(){var b="."+g(this).parent().attr("class").split(" ")[1];void 0!==b&&g(b).hover(function(){g(b).addClass(a.currentClass)},function(){g(b).removeClass(a.currentClass)})});m.build.canvas.resize(a);m.build.canvas.draw(a,d,b)}};if(A[q])return A[q].apply(this,Array.prototype.slice.call(arguments,1));if("object"===typeof q||!q)return A.init.apply(this,arguments);g.error('Method "'+q+'" does not exist in gracket!')}})(jQuery);