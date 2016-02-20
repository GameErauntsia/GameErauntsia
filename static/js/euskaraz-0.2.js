 
	function itxi() {
		document.getElementById("bar_eu").style.visibility="hidden"; 
        // document.body.style.backgroundPosition = 'left 0';
	}
	
	var div = document.createElement('div');
    div.id = 'overlay';
    div.innerHTML = '<div id="bar_eu" style="position:absolute;z-index:200;top:50px;left:0;margin:0;padding:0;border:0;width:100%;height:58px;background:url(http://nabigatueuskaraz.com/img/fondoa.png) repeat-x;"><div style="position:relative;padding:8px 0 0 39px;float:left;"><img src="http://nabigatueuskaraz.com/img/b.png" style="position:absolute;top:6px;left:5px;"/><span style="margin:0;padding:0;border:none;font-family:Arial, Helvetica, sans-serif;font-size:18px;color:#000;font-weight:bold;">Ez zaude <span style="color:#cb0101;">euskaraz</span> nabigatzen.</span><span style="display:block;margin:3px 0 0 0;padding:0;border:none;font-family:Arial, Helvetica, sans-serif;font-size:13px;color:#000;">Interneten ere, lehen hitza euskaraz!</span></div><div style="float:left;position:relative;display:block;border-left:1px solid #eec44a;margin:1px 0 0 28px;height:54px;"><a href="http://nabigatueuskaraz.com/konfiguratu" style="display:block;font-size:14px;font-weight:bold;background:url(http://nabigatueuskaraz.com/img/fondoa.png) no-repeat right;margin-top:5px;margin-left:8px;font-family:Arial, Helvetica, sans-serif;color:#010000;text-decoration:none;padding:15px 20px 15px 10px;">Konfiguratu nabigatzailea <u style="color:#cb0101">euskaraz nabigatzeko</u>. Oso erraza: eskaini minutu bat euskarari. </a></div><div style="clear:both;">&nbsp;</div><div style="position:absolute;top:1px;right:0;width:200px;height:54px;border-left:1px solid #eec44a;"><span style="position:absolute;margin:0;padding:0;top:3px;left:10px;font-family:Arial, Helvetica, sans-serif;font-size:10px;color:#000;">Gehiago jakin nahi duzu?</span><a href="http://nabigatueuskaraz.com/" target="_blank"><img src="http://nabigatueuskaraz.com/img/nabigatu-euskaraz.png" alt="Nabigatu euskaraz" style="position:absolute;top:15px;left:20px;border:none;" /></a><a href="javascript:itxi();"><img src="http://nabigatueuskaraz.com/img/x.png" alt="itxi" style="position:absolute;top:0;right:5px;border:none;" /></a></div></div>';
    if (document.body.firstChild){
        document.body.insertBefore(div, document.body.firstChild);
    } else {
        document.body.appendChild(div);
    }
	
