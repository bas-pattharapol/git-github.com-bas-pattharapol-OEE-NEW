<?php
ob_start();
session_start();
require_once("config_smarty.php");
include("utility.php");

if($_SESSION['GROUPS'] != ''){
	 // Logon done
//


//  $dataseries  =   file_get_contents('file_diary_data.json');
//  $databottombar = file_get_contents('file_diary_barmenu.json');

// Change Type of Preweight 11-Oct-19 11:34:42 AM
//  WHEN 'C' THEN 'Preweight Completed' to  WHEN 'F' THEN 'Preweight Completed'
//  WHEN 'F' THEN 'Finished'  to WHEN 'S' THEN 'Finished'
//
 

$sql = "SELECT PD_ORDER, CONVERT(VARCHAR(10), CONVERT(DATE, PD_PLAN_DT, 106), 105) AS PLAN_DATE,
				PD_FM_CODE, PD_FM_NAME, PD_BATCHNO,PD_TARGET_QTY, PD_TARGET_UNIT  ,
				CASE PD_STATUS
				    WHEN 'P' THEN 'Plan'
				    WHEN 'O' THEN 'Preweight ON PROCESS'
				    WHEN 'F' THEN 'Preweight Completed'
				    WHEN 'L' THEN 'Prepare Mix'				    
				    WHEN 'M' THEN 'Mixing'
				    WHEN 'Q' THEN 'QA'
				    WHEN 'S' THEN 'Finished'
				    WHEN 'T' THEN 'Filling'
				    WHEN 'E' THEN 'Error'
				    ELSE 'Unknown'
				END AS PD_STATUS_MSG ,
				PD_STATUS
				 FROM PD_ORDER_TAB WHERE PD_STATUS IN ('F','M')
				 ORDER BY PLAN_DATE DESC";

//  echo dirname(__FILE__);
	require_once dirname(__FILE__).'/../Logger/main/php/Logger.php';
	Logger::configure(dirname(__FILE__).'/../Logger/examples/resources/NEO_pdorder.properties');
	$today = date("m.d.y H:i:s");
	$logger = Logger::getLogger('Preweight_Complete');
	$logger->info('****************************************************');
	$logger->info('Ipaddress :: '.get_client_ip());

	// $logger->info('Actor :: '.$u_user);
	// $logger->info('Actions :: Update');
	// $logger->info('HOST_ID :: '.$acq_id);
	// $logger->info('Step :: Begin build history xml');

//	$sql = "SELECT PD_ORDER, CONVERT(VARCHAR(10), CONVERT(DATE, PD_PLAN_DT, 106), 105) AS PLAN_DATE,
//          PD_FM_CODE, PD_FM_NAME, PD_BATCHNO,PD_TARGET_QTY, PD_TARGET_UNIT
//          FROM PD_ORDER_TAB
//          WHERE PD_STATUS = 'P'
//          ORDER BY PLAN_DATE DESC";

	$db = db_connect();
	$rs = $db->Execute($sql,array());

if($rs->EOF){

		if($db->ErrorMsg() != ''){
			$error_msg = $db->ErrorMsg();
		}
		else{
			$error_msg = 'Preweight Complete '.$job_id.' not found on table [Preweight Complete]';
		}

  }
   	@db_disconnect($db);
		$smarty->display('head.tpl');
		
		$smarty->assign('username', $_SESSION['USERNAME']);
    $smarty->assign('group', $_SESSION['GROUPS']);

		$smarty->display('hbar_left_content.tpl');

		$head_title = " <h1>
						        Landing Page
						        <small>it all starts here</small>
						      </h1>";

		$head_nav = '<ol class="breadcrumb">
	    						  <li><a href="/neo/index.php"><i class="fa fa-home"></i> Home</a></li>
	    						  <li><a href="#">Preweight Completed</a></li>
	  					  </ol>';
	//			    					  		<li><a href="#">Examples</a></li>
	//			      						  <li class="active">Blank page</li>

	  $smarty->assign('head_title', $head_title);
	  $smarty->assign('head_nav', $head_nav);

	  $smarty->assign('content_title', 'Preweight On Process');

    $smarty->assign('rs', $rs);
		$smarty->display('pd_pw_completed_content.tpl');
		
		$smarty->display('footer.tpl');


}else{

   // First Lookup
		$smarty->display('head.tpl');
    $smarty->assign("logonmsg", '');
		$smarty->display('logon.tpl');
		$smarty->display('footer_unfooter.tpl');

}

?>
