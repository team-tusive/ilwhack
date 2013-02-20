<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head><title>
	Twitter
</title><link href="/WebResource.axd?d=c-dc1HPwtJCJGLUHocuMYfTJCa9WL8mBKjMnD3hVD2juh1YpTbVkmYtUQz9rbqLdikVzDJoSO_UCPPLHpX6u7rF-v7cpW7TAF816s4VmNJU1&amp;t=634807193449531250" type="text/css" rel="stylesheet" /><meta http-equiv="Content-Style-Type" content="text/css" /><meta http-equiv="content-script-type" content="text/javascript" /><link href="../../../../../templates/default/css/system/default.css" rel="stylesheet" type="text/css" /><link href="../../../../../templates/default/css/standard.css" type="text/css" rel="stylesheet" />
<script type="text/javascript" src="/jquery/jquery-1.7.1.min.js"></script>




<meta name="GENERATOR" content="Immediacy .NET CMS - Licensed To : Lothian &amp; Borders Police Board" /><meta name="keywords" content="LBP, Twitter, Lothian and Borders Police" /><meta name="description" content="Twitter, Lothian and Borders Police" /></head>
<body>






<div id="wrapper">

<script type="text/javascript" src="http://code.jquery.com/jquery-latest.js"></script>
<noscript><div>Browser does not support script.</div></noscript>
 

<div id = "cookies" style="background-color:#333333; color:#ffffff;font-weight:bold; display:none;">
<table>
<tr>
    <td style="width:200px">Cookies on the LBP website.</td>
    <td>We use cookies to enable us to improve the experience that you receive from visiting the Lothian and Borders Police website. If you continue to use the website, we will assume that you are happy to receive cookies from our site. <a id="ContinueOn" href="#" style="color:#c8c8c8; text-decoration: underline;" >Continue</a></td>

</tr>
</table>
</div>
<script type="text/javascript">

 DisplayCookie();
 
 function DisplayCookie(){
   if (readCookie("LBP.Cookie") === "Accepted")
   {
     $("#cookies").hide();
     //eraseCookie("LBP.Cookie")
     createCookie("LBP.Cookie", "Accepted", 7);  
   }
   else
   {
    $("#cookies").show();
   }
 }
 
  $("a#ContinueOn")
    .bind('click', function(event) {
        var src = event.type == 'mouseenter' ? $('p#return').css('cursor', 'pointer') : $('p#return').css('cursor', 'auto');
        var srcclick = event.type == 'click' ? true : false;
        if (srcclick) {     
         createCookie ("LBP.Cookie","Accepted",7)        
         $("#cookies").hide();
       }
    });

function createCookie(name,value,days) {
	if (days) {
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = "; expires="+date.toGMTString();
	}
	else var expires = "";
	document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}

function eraseCookie(name) {
	createCookie(name,"",-1);
}


</script>
<noscript><div>Browser does not support script.</div></noscript>
 
    

<div id="header">
    <div>
        <span id="tagLine">Non-Emergency Number<span class="bold">0131 311 3131</span></span>
        <div id="search">
            <form action="/search.aspx" method="get">
                <fieldset>
                    <input name="terms" title="search terms" type="text" size="24" />
                    <input id="btnSearch" title="submit" type="submit" value="" />
                </fieldset>
            </form>
       </div>
    </div>
    <div id="headerImage">
        <img id="Template_ctl02_imgHeader" src="../../../../../images/cbo_floors%20castle_final.jpg" alt="Floors Castle Scottish Borders"  />
    </div>

	
				<ul>
    				<li class="first"><a href="../../../../../default.aspx">Homepage</a></li>
		<li><a href="/my_neighbourhood.aspx" title="My Neighbourhood" class="L0nc">My Neighbourhood</a></li>
<li><a href="/crime_prevention.aspx" title="Crime Prevention" class="L0nc">Crime Prevention</a></li>
<li><a href="/information.aspx" title="Information" class="L0nc">Information</a></li>
<li><a href="/about_us.aspx" title="About us" class="L0nc">About us</a></li>
<li><a href="/contact_us.aspx" title="Contact Us" class="L0nc">Contact Us</a></li>

			</ul>
		

    <div style="clear:left;height:0;"><!-- empty div--></div>
</div>   

    <form name="aspnetForm" method="post" action="twitter.aspx" id="aspnetForm">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUENTM4MQ9kFgJmD2QWBgIBD2QWAgIGDxYCHgRocmVmBSR+L3RlbXBsYXRlcy9kZWZhdWx0L2Nzcy9zdGFuZGFyZC5jc3NkAgkPZBYCZg8PFgQeCEltYWdlVXJsBSR+L2ltYWdlcy9jYm9fZmxvb3JzIGNhc3RsZV9maW5hbC5qcGceDUFsdGVybmF0ZVRleHQFHkZsb29ycyBDYXN0bGUgU2NvdHRpc2ggQm9yZGVyc2RkAgsPZBYGAgcPZBYEZg8WAh4HVmlzaWJsZWdkAgIPFgIfA2hkAg0PZBYOAgEPDxYCHgRUZXh0BQpDYXRlZ29yaWVzZGQCAw8PFgIfA2hkZAIFDw8WAh8DaGQWBAIBDxYCHgljdXJQYWdlTm8CARYIAgEPZBYCZg8VAgxJTElOS3w0NzgzLHwsTWFkZSBmcm9tIENyaW1lPyBjYW1wYWlnbiAtIFNjb3R0aXNoIEJvcmRlcnNkAgIPZBYCZg8VAgxJTElOS3w0NzQ3LHwPZHJ1Z3Mgb3BlcmF0aW9uZAIDD2QWAmYPFQIMSUxJTkt8NDc5NCx8HFdpdG5lc3MgYXBwZWFsLCBXZXN0IExvdGhpYW5kAgQPZBYCZg8VAgxJTElOS3w0NzkzLHwmQnJlYWstaW4gYW5kIGhpZ2ggdmFsdWUgdGhlZnQsIEJvcmRlcnNkAgMPDxYCHwNoZGQCBw8PFgIfA2hkZAIJDw8WAh8DaGQWAgIBDxYCHwUCARYQAgEPZBYCZg8VAwxJTElOS3w0NzgzLHwsTWFkZSBmcm9tIENyaW1lPyBjYW1wYWlnbiAtIFNjb3R0aXNoIEJvcmRlcnMsTWFkZSBmcm9tIENyaW1lPyBjYW1wYWlnbiAtIFNjb3R0aXNoIEJvcmRlcnNkAgIPZBYCZg8VAwxJTElOS3w0NzQ3LHwPZHJ1Z3Mgb3BlcmF0aW9uD2RydWdzIG9wZXJhdGlvbmQCAw9kFgJmDxUDDElMSU5LfDQ3OTQsfBxXaXRuZXNzIGFwcGVhbCwgV2VzdCBMb3RoaWFuHFdpdG5lc3MgYXBwZWFsLCBXZXN0IExvdGhpYW5kAgQPZBYCZg8VAwxJTElOS3w0NzkzLHwmQnJlYWstaW4gYW5kIGhpZ2ggdmFsdWUgdGhlZnQsIEJvcmRlcnMmQnJlYWstaW4gYW5kIGhpZ2ggdmFsdWUgdGhlZnQsIEJvcmRlcnNkAgUPZBYCZg8VAwxJTElOS3w0NzkyLHwZTWFuIGNoYXJnZWQsIEVhc3QgTG90aGlhbhlNYW4gY2hhcmdlZCwgRWFzdCBMb3RoaWFuZAIGD2QWAmYPFQMMSUxJTkt8NDc5Myx8JkJyZWFrLWluIGFuZCBoaWdoIHZhbHVlIHRoZWZ0LCBCb3JkZXJzJkJyZWFrLWluIGFuZCBoaWdoIHZhbHVlIHRoZWZ0LCBCb3JkZXJzZAIHD2QWAmYPFQMMSUxJTkt8NDc5Mix8GU1hbiBjaGFyZ2VkLCBFYXN0IExvdGhpYW4ZTWFuIGNoYXJnZWQsIEVhc3QgTG90aGlhbmQCCA9kFgJmDxUDDElMSU5LfDQ3ODMsfCxNYWRlIGZyb20gQ3JpbWU/IGNhbXBhaWduIC0gU2NvdHRpc2ggQm9yZGVycyxNYWRlIGZyb20gQ3JpbWU/IGNhbXBhaWduIC0gU2NvdHRpc2ggQm9yZGVyc2QCCw8PFgIfA2hkFgQCAQ8PFgIfA2hkZAIFDw8WAh8DaGRkAg0PDxYCHwNnZGQCDw9kFgICAQ8WAh8EBRFGZWF0dXJlZCBTZXJ2aWNlc2Rkht5m00nVbCr61ZlIqGs5iLzB+lU=" />


<script type="text/javascript">
//<![CDATA[
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-7208266-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
  //]]>
</script>
<noscript><div>Browser does not support script.</div></noscript>


<script src="/ScriptResource.axd?d=8-bP4NkZ9QXvt8FwQHibsf6t824Gsph2oRGOXODMfH8uQnYJLpQ54T481OnvmI1WGu9anjXAxomEzdeyrnHoDhapsna01mvb-xqH7VPS1LY1&amp;t=fcd28e4" type="text/javascript"></script>
<noscript><div>Browser does not support script.</div></noscript>

        <div id="mainContent">

            

            
        <div id="breadcrumb">
            <span>You are here : </span>
	    	<ul>
	
			<li class="arrow"><a href="/default.aspx">Home Page</a> </li>
	

			<li class="arrow"><a href="/information.aspx">Information</a> </li>
	

			<li class="arrow"><a href="/information/news.aspx">Latest News</a> </li>
	

			<li class="arrow"><a href="/information/latest_news/news_archives.aspx">News Archives</a> </li>
	

			<li class="arrow"><a href="/information/latest_news/news_archives/2011.aspx">2011</a> </li>
	

			<li class="arrow"><a href="/information/latest_news/news_archives/2011/october_2011.aspx">October 2011</a> </li>
	

			<li>Twitter</li>
	

		    </ul>
	    </div>
	
        
            <div id="main">
                <div class="cell724">
	                <h1>
    	                <span id="Template_NewsDate1_lblDate" style="float:right"></span>

	                    Twitter


	                    <span id="Template_ctl08_lblMessage"><font color="Red"></font></span>

	                </h1>
                	
<p><a onclick="window.open(this.href, '_blank'); return false;" href="http://twitter.com/LBP_Police" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}"><img width="306" alt="Twitter icon on computer screen" class="ImmControlAlign_Right" title="Twitter icon on computer screen" src="/images/istocktwittericon360.jpg" height="204"/></a>Did you know that&nbsp;nearly&nbsp;6000 people follow
us on Twitter.?</p>
<p><br />
Our tweets keep the public informed on the latest LBP news and
offers advice on how to deal with current local issues, such as
adverse weather conditions.<br />
<br />
We'll also be keeping the public informed on details of forthcoming
Community Safety Meetings<br />
<br />
Why not&nbsp;follow&nbsp;us&nbsp;and receive daily updates direct
to your computer or phone?</p>
<p>&nbsp;</p>
<table summary="Box">
<tbody>
<tr>
<td><img width="21" alt="Link" title="Link" src="/images/link_icon.jpg" height="21"/></td>
<td><a onclick="window.open(this.href, '_blank'); return false;" href="http://twitter.com/LBP_Police" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}">LBP Twitter feed</a></td>
</tr>
</tbody>
</table>
&nbsp;
                </div>
                <div class="cell250">
                    

<h2>
    <span id="Template_RightMenu1_lblHeading">Categories</span>
</h2>













<table id="Template_RightMenu1_pnlPageList" cellpadding="0" cellspacing="0" border="0" width="100%"><tr><td>
	


    
            <div id="rightPageList">
                <ul>
        
	        <li>
	            <a href="/information/how_to_contact_us.aspx" title="How to contact us" class=''>
	                <span>How to contact us</span>
	            </a>
	            </li>

	        <li>
	            <a href="/information/accessibility.aspx" title="Accessibility" class=''>
	                <span>Accessibility</span>
	            </a>
	            </li>

	        <li>
	            <a href="/information/appeals.aspx" title="Appeals" class=''>
	                <span>Appeals</span>
	            </a>
	            </li>

	        <li>
	            <a href="/information/community_guidance.aspx" title="Community Guidance" class=''>
	                <span>Community Guidance</span>
	            </a>
	            </li>

	        <li>
	            <a href="/information/events.aspx" title="Public Information" class=''>
	                <span>Public Information</span>
	            </a>
	            </li>

	        <li>
	            <a href="/information/freedom_of_information.aspx" title="Freedom of Information" class=''>
	                <span>Freedom of Information</span>
	            </a>
	            </li>

	        <li>
	            <a href="/information/frequently_asked_questions.aspx" title="Frequently asked questions" class=''>
	                <span>Frequently asked questions</span>
	            </a>
	            </li>

	        <li>
	            <a href="/information/news.aspx" title="Latest News" class=''>
	                <span>Latest News</span>
	            </a>
	            
<ul>
	        <li>
	            <a href="/information/latest_news/news_archives.aspx" title="News Archives" class=''>
	                <span>News Archives</span>
	            </a>
	            
<ul>
	        <li>
	            <a href="/information/latest_news/news_archives/2011.aspx" title="2011" class="selected">
	                <span>2011</span>
	            </a>
	            

	        <li>
	            <a href="/information/latest_news/news_archives/2012.aspx" title="2012" class=''>
	                <span>2012</span>
	            </a>
	            

	        <li>
	            <a href="/information/latest_news/news_archives/2013.aspx" title="2013" class=''>
	                <span>2013</span>
	            </a>
	            
</ul></li>
	        <li>
	            <a href="/information/links.aspx" title="Useful links" class=''>
	                <span>Useful links</span>
	            </a>
	            

	        <li>
	            <a href="/information/meritorious_award_ceremony.aspx" title="Meritorious Award Ceremony" class=''>
	                <span>Meritorious Award Ceremony</span>
	            </a>
	            

	        <li>
	            <a href="/information/restorative_justice.aspx" title="Restorative Justice for Hate Crime" class=''>
	                <span>Restorative Justice for Hate Crime</span>
	            </a>
	            

	        <li>
	            <a href="/information/service_information.aspx" title="Service Information" class=''>
	                <span>Service Information</span>
	            </a>
	            

	        <li>
	            <a href="/information/station_information.aspx" title="Station information" class=''>
	                <span>Station information</span>
	            </a>
	            

	        <li>
	            <a href="/information/strategic_co-ordinating_group.aspx" title="Strategic Co-ordinating Group" class=''>
	                <span>Strategic Co-ordinating Group</span>
	            </a>
	            

	        <li>
	            <a href="/information/operation_accessible.aspx" title="Operation Accessible" class=''>
	                <span>Operation Accessible</span>
	            </a>
	            

	        <li>
	            <a href="/information/lbp_twitter_policy.aspx" title="LBP Twitter Policy" class=''>
	                <span>LBP Twitter Policy</span>
	            </a>
	            

	        <li>
	            <a href="/information/police%20reform.aspx" title="Police reform" class=''>
	                <span>Police reform</span>
	            </a>
	            

            </ul>
        </div>
    



</td></tr></table>
                </div>
                
                <div style="clear:left;"></div>
            </div>

            <div>
                <div class="footer724"></div>
                <div class="footer250"></div>
            </div>
        
            <div>

                <div class="cell724 footer724 height145">
                   

<h2>
    Featured Services
</h2>

<div id="featuredServices">

<ul><li><a class="bottomRightArrow" href="/system_pages/featured_services/freedom_of_information.aspx">Freedom of Information</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/jobs.aspx">Jobs</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/make_a_complaint.aspx">Make a complaint</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/crimestoppers.aspx" onclick="window.open(this.href, '_blank'); return false;" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}">Crimestoppers</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/foreign_national_registration.aspx">Foreign national registration</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/ceop.aspx" onclick="window.open(this.href, '_blank'); return false;" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}">CEOP</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/firearms_faq.aspx">Firearm Certificates (FAQs)</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/victim_support_scotland.aspx" onclick="window.open(this.href, '_blank'); return false;" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}">Victim Support Scotland</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/internet_watch_foundation.aspx" onclick="window.open(this.href, '_blank'); return false;" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}">Internet Watch Foundation</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/victims_of_crime_in_scotland.aspx" onclick="window.open(this.href, '_blank'); return false;" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}">Victims of Crime in Scotland</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/traffic_scotland.aspx" onclick="window.open(this.href, '_blank'); return false;" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}">Traffic Scotland</a></li>
<li><a class="bottomRightArrow" href="/system_pages/featured_services/crime_statistics.aspx">Crime Statistics</a></li>
</ul>

</div>
                </div>

                <div class="cell250 footer250 height145" id="ContactArea">
                    
<h2><a href="/contact_us.aspx">Contact</a></h2>
<p>Lothian and Borders Police<br />
Force Headquarters<br />
Fettes Avenue&nbsp;<br />
Edinburgh EH4 1RB<br /></p>
<div style="HEIGHT: 6px"></div>
<table summary="table summary">
<tbody>
<tr>
<td style="WIDTH: 40%" class="ImmTextAlign_Left">EMERGENCY<br />
<strong>999</strong></td>
<td style="WIDTH: 140px" class="ImmTextAlign_Left">
NON-EMERGENCY<br />
<strong>0131 311 3131</strong></td>
</tr>
</tbody>
</table>
                
                </div>
            </div>

            <div id="web2">
                
<table style="WIDTH: 100%" summary="box">
<tbody>
<tr>
<th class="ImmTextAlign_Left" style="WIDTH: 3%">&nbsp;</th>
<td class="ImmTextAlign_Left"><img width="34" alt="Email Lothian Borders Police" class="ImmControlAlign_Left" title="email us" src="/images/email_ic.png" height="35"/>&nbsp;<a title="Email: Enquiries at Lothian and Borders Police" href="/email%20redirect.aspx">E-mail</a><br />
&nbsp;Get in touch with us</td>
<td style="WIDTH: 3%" class="ImmTextAlign_Left"><img width="34" alt="Wordpress" title="Wordpress" src="/images/wordpress_logo_35px.jpg" style="MARGIN-RIGHT: 5px" height="35"/></td>
<td class="ImmTextAlign_Left">
<p><a onclick="window.open(this.href, '_blank'); return false;" href="http://lbpolice.wordpress.com/" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}">Blog</a></p>
<p>Updates and information</p>
</td>
<td style="WIDTH: 2%" class="ImmTextAlign_Left"><img width="34" alt="Follow us on Twitter" title="Twitter" src="/images/twitter.png" height="35"/></td>
<td class="ImmTextAlign_Left">&nbsp; <a onclick="window.open(this.href, '_blank'); return false;" href="http://twitter.com/LBP_Police" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}">Twitter</a><br />
&nbsp;&nbsp; Get the latest force tweets</td>
<td style="WIDTH: 3%" class="ImmTextAlign_Left">&nbsp;<img width="35" alt="View our You Tube channel" title="You Tube" src="/images/youtube.png" height="35"/></td>
<td class="ImmTextAlign_Left">&nbsp; <a onclick="window.open(this.href, '_blank'); return false;" href="http://www.youtube.com/user/LBPolicemedia" onkeypress="if (event.keyCode==13) {window.open(this.href, '_blank'); return false;}">You
Tube&nbsp;</a><br />
&nbsp;&nbsp;Watch and listen to our videos</td>
</tr>
</tbody>
</table>

            </div>

        </div>
        
        

<div id="footer">
    <div>
	    <a href="/system_pages/useful_links/site_map.aspx">Site Map</a>
 | <a href="/system_pages/useful_links/faq.aspx">FAQ</a>
 | <a href="/system_pages/useful_links/accessibility.aspx">Accessibility</a>

    </div>

    &copy; 2010 Lothian and Borders Police | Force Headquarters | Fettes Avenue | Edinburgh EH4 1RB 

</div>





<script type="text/javascript">
//<![CDATA[
Sys.Application.initialize();
//]]>
</script>
<noscript><div>Browser does not support script.</div></noscript>

</form>
</div>
</body>
</html>
