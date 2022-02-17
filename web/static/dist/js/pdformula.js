$(document).ready(function(){

  $(function () {
    //alert('xxxx')
    //Initialize DataTables
		$("#pdrequest_table").DataTable();

  });

	$('.acqname').blur(function() {

		$(this).val($(this).val().toUpperCase());

	});

	$('.btnedit').on('click', function() {

		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var editStatus = $('#edit_status').val();
		//alert(actionKey);

		if(editStatus == '0'){

			//Insert active status
			$('#edit_status').val('1');
			$('#cur_active_key').val(actionKey);

			//Enable control
			$('#acqname_'+actionKey).css('display','');
			$('#acqdesc_'+actionKey).css('display','');
			$('#save_'+actionKey).css('display','');

			//Disable control
			$('#lbl_pdorder_'+actionKey).css('display','none');
			$('#lbl_acqdesc_'+actionKey).css('display','none');
			$('#edit_'+actionKey).css('display','none');
			$('#del_'+actionKey).css('display','none');

		}
		else{
			$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
			$('.modal-header').children('h4').html('Warning!');
			$('.modal-body').children().html('');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');
			$('#modal_dialog').modal('show');
			return false;
		}

	});

	$('.btnInsert').on('click', function() {

			$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
			$('.modal-header').children('h4').html('Warning!');
			$('.modal-body').children().html('Acquirer cannot be null value. Please, enter acquirer name.'+$('#pd_order').val());
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnFocusAcqName');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('OK');
			$('#modal_dialog').modal('show');
			return false;


		if($('#pd_order').val() != ''){

			pdorder_topw($('#pd_order').val(), $('textarea[name=acq_desc]').val());

		}
		else{
			$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
			$('.modal-header').children('h4').html('Warning!');
			$('.modal-body').children().html('Acquirer cannot be null value. Please, enter acquirer name.');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnFocusAcqName');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('OK');
			$('#modal_dialog').modal('show');
			return false;
		}

	});

	$(document).delegate('#btnFocusAcqName', 'click', function() {

		$('#modal_dialog').modal('hide');
		$('#pd_order').focus();

	});

	$(document).delegate('#btnGotoLogin', 'click', function() {

		$('#modal_dialog').modal('hide');
		window.location.href = "/neo/logon.php"

	});





/********************* SEND TO MASTER TEMPLATE **********************/


	$(document).delegate('.btndtotemplate', 'click', function() {
		
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var pd_order = $('#lbl_pdorder_'+actionKey).html();
		//var pd_batchno = $('#lbl_batchno_'+actionKey).html();

		console.log('controlId ' + controlId);
		console.log('actionKey' + actionKey);
		console.log('pd_order ' + pd_order);
		
		$('#cur_spw_key').val(actionKey);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Set To Template confirmation!');
		$('.modal-body').children().html('Are you sure you want to Assign  \"'+pd_order+'\" to Template?');
		$('.modal-footer').children('.btn:nth-child(1)').css('display','');
		$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnCfSTP');
		$('.modal-footer').children('.btn:nth-child(1)').html('Assign');
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotSTP');
		$('.modal-footer').children('.btn:nth-child(2)').html('Cancel');
		$('#modal_dialog').modal('show');
	});

	$(document).delegate('#btnCfDonotSTP', 'click', function() {

		$('#modal_dialog').modal('hide');
		$('#cur_spw_key').val('');

	});

	$(document).delegate('#btnCfSTP', 'click', function() {

		acq_sendtotemplate($('#cur_spw_key').val());

	});



/************************************* Remove *************************************/
	
	$(document).delegate('.btremove', 'click', function() {
		
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var pd_order = $('#lbl_pdorder_'+actionKey).html();
		//var pd_batchno = $('#lbl_batchno_'+actionKey).html();

		console.log('controlId ' + controlId);
		console.log('actionKey' + actionKey);
		console.log('pd_order ' + pd_order);
		
		$('#cur_spw_key').val(actionKey);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Remove Template confirmation!');
		$('.modal-body').children().html('Are you sure you want Remove  \"'+pd_order+'\" ?');
		$('.modal-footer').children('.btn:nth-child(1)').css('display','');
		$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnCfETP');
		$('.modal-footer').children('.btn:nth-child(1)').html('Assign');
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotETP');
		$('.modal-footer').children('.btn:nth-child(2)').html('Cancel');
		$('#modal_dialog').modal('show');
	});

	$(document).delegate('#btnCfDonotETP', 'click', function() {

		$('#modal_dialog').modal('hide');
		$('#cur_spw_key').val('');

	});

	$(document).delegate('#btnCfETP', 'click', function() {
		acq_removetemplate($('#cur_spw_key').val());
    // $( 'a[href^="http://"]' ).attr("href", "http://www.google.com/").attr( 'target','_blank' );
    // $('#edittmp_8').attr('href', 'http://172.30.1.1:8080/');
    // $('#edittmp_8').attr('target', '_blank');
 //   $("#edittmp_8").click(function(){
 //      $(this).hide(200);
 //      return false;
 //   });
 
//   $('#modal_dialog').modal('hide');
//  $('#cur_spw_key').val('');
//  
//  $("a#edittmp_8").attr({
//  "href": "http://172.30.1.1:8080",
//  "target": "_blank",
//  });
//   $("#edittmp_8").click(function( event ){
//      event.preventDefault();
//        console.log("xxxx");
//      // $(this).click();
//      return false;
//   });     

//	$('a[id^="edittmp_"]').attr({
//		"href" : "http://172.30.1.1:8080", 
//	});

// $("#edittmp_8").attr("href", "http://172.30.1.1");
//	$('#edittmp_8"]').attr(
//		"href" : "http://172.30.1.1:8080", 
//	});

//	$('a[id^="edittmp_"]').click(function(){
//		event.preventDefault();
//		return false;
//	});

    // $("#edittmp_8").attr({
    //     "href" : "http://172.30.1.1:8080",            // setting multiple attributes
    //     "title" : "Template Editor"
    // });
    // });

    // $('a').attr("href", "http://172.30.1.1:8080/").attr( 'target','_blank' );
    // 
    // .attr( 'target','_blank' );
    //$('a[rel="external"]').attr('target', '_blank');
		// acq_modifytemplate($('#cur_spw_key').val());

	});





/************************************* SEND TO PREWEIGHT *************************************/
	$('.btnsendplan').on('click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var pd_order = $('#lbl_pdorder_'+actionKey).html();
		//var pd_batchno = $('#lbl_batchno_'+actionKey).html();

		// console.log('xxx' + actionKey);
		// console.log('pd_order ' + pd_order);
		// console.log('batchno ' + pd_batchno);

		$('#cur_spw_key').val(pd_order);
		// $('#cur_spw_batchnokey').val(pd_batchno);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Send to Plan confirmation!');
		$('.modal-body').children().html('Are you sure you want to Send To Plan \"'+pd_order+'\"?');
		$('.modal-footer').children('.btn:nth-child(1)').css('display','');
		$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnCfSPW');
		$('.modal-footer').children('.btn:nth-child(1)').html('Send');
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotSPW');
		$('.modal-footer').children('.btn:nth-child(2)').html('Cancel');
		$('#modal_dialog').modal('show');
	});


	$('.btndetailreq').on('click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var pd_order = $('#lbl_pdorder_'+actionKey).html();
		var pd_orderlist = $('#lbl_orderlist_'+actionKey).html();
		//var pd_batchno = $('#lbl_batchno_'+actionKey).html();

		// console.log('xxx' + actionKey);
		// console.log('pd_order ' + pd_order);
		// console.log('batchno ' + pd_batchno);

		$('#cur_spw_key').val(pd_order);
		// $('#cur_spw_batchnokey').val(pd_batchno);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Detail for '+pd_order);
		$('.modal-body').children().html('include PD ORDER : '+pd_orderlist);
		$('.modal-footer').children('.btn:nth-child(1)').css('display','none');  // undispaly savechange
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotSPW');
		$('.modal-footer').children('.btn:nth-child(2)').html('Close');
		$('#modal_dialog').modal('show');
		
	});


	$(document).delegate('.btndel', 'click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var useraccid = $('#lbl_orderlist_'+actionKey).html();
		$('#cur_spw_key').val(actionKey);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Remove confirmation!');
		$('.modal-body').children().html('Are you sure you want to remove Account \"'+useraccid+'\"?');
		$('.modal-footer').children('.btn:nth-child(1)').css('display','');
		$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnCfDel');
		$('.modal-footer').children('.btn:nth-child(1)').html('Remove');
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotSPW');
		$('.modal-footer').children('.btn:nth-child(2)').html('Cancel');
		$('#modal_dialog').modal('show');
	});

	$(document).delegate('#btnCfDonotSPW', 'click', function() {

		$('#modal_dialog').modal('hide');
		$('#cur_spw_key').val('');

	});

	$(document).delegate('#btnCfDel', 'click', function() {

		acq_delaccount($('#cur_spw_key').val());

	});

/***************** inactive *****************/
	$(document).delegate('.btninactive', 'click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var useraccid = $('#lbl_orderlist_'+actionKey).html();
		$('#cur_spw_key').val(actionKey);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Inactive Account confirmation!');
		$('.modal-body').children().html('Are you sure you want to Inacive Account \"'+useraccid+'\"?');
		$('.modal-footer').children('.btn:nth-child(1)').css('display','');
		$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnCfInAct');
		$('.modal-footer').children('.btn:nth-child(1)').html('InActive');
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotIAC');
		$('.modal-footer').children('.btn:nth-child(2)').html('Cancel');
		$('#modal_dialog').modal('show');
	});

	$(document).delegate('#btnCfDonotIAC', 'click', function() {

		$('#modal_dialog').modal('hide');
		$('#cur_spw_key').val('');

	});

	$(document).delegate('#btnCfInAct', 'click', function() {

	  acq_inactiveaccount($('#cur_spw_key').val());

	});


/***************** active *****************/
	$(document).delegate('.btnactive', 'click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var useraccid = $('#lbl_orderlist_'+actionKey).html();
		$('#cur_spw_key').val(actionKey);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Active Account confirmation!');
		$('.modal-body').children().html('Are you sure you want to Active Account \"'+useraccid+'\"?');
		$('.modal-footer').children('.btn:nth-child(1)').css('display','');
		$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnCfAct');
		$('.modal-footer').children('.btn:nth-child(1)').html('Active');
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotAC');
		$('.modal-footer').children('.btn:nth-child(2)').html('Cancel');
		$('#modal_dialog').modal('show');
	});

	$(document).delegate('#btnCfDonotAC', 'click', function() {

		$('#modal_dialog').modal('hide');
		$('#cur_spw_key').val('');

	});

	$(document).delegate('#btnCfAct', 'click', function() {

	  acq_activeaccount($('#cur_spw_key').val());

	});

/******** clear logon invalid count *************/
	$(document).delegate('.btnclelgcnt', 'click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var useraccid = $('#lbl_orderlist_'+actionKey).html();
		$('#cur_spw_key').val(actionKey);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Clear Logon Invalid Count confirmation!');
		$('.modal-body').children().html('Are you sure you want to Clear Logon Invalid Count  \"'+useraccid+'\"?');
		$('.modal-footer').children('.btn:nth-child(1)').css('display','');
		$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnCfClearCnt');
		$('.modal-footer').children('.btn:nth-child(1)').html('Clear');
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotClearCnt');
		$('.modal-footer').children('.btn:nth-child(2)').html('Cancel');
		$('#modal_dialog').modal('show');
	});

	$(document).delegate('#btnCfDonotClearCnt', 'click', function() {

		$('#modal_dialog').modal('hide');
		$('#cur_spw_key').val('');

	});

	$(document).delegate('#btnCfClearCnt', 'click', function() {

	  acq_clearlogoncount($('#cur_spw_key').val());

	});




/************************************* SEND TO MIXING *************************************/
	$('.btnsendmix').on('click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var pd_order = $('#lbl_pdorder_'+actionKey).html();
		var pd_batchno = $('#lbl_batchno_'+actionKey).html();

		console.log('xxx' + actionKey);
		console.log('pd_order ' + "lbl_pdorder_"+actionKey);

		$('#cur_spw_key').val(actionKey);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Send Mixing confirmation!');
		$('.modal-body').children().html('Are you sure you want to Send To Mixing with PD_ORDER \"'+pd_order+'\"?');
		$('.modal-footer').children('.btn:nth-child(1)').css('display','');
		$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnCfSMX');
		$('.modal-footer').children('.btn:nth-child(1)').html('Send');
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotSMX');
		$('.modal-footer').children('.btn:nth-child(2)').html('Cancel');
		$('#modal_dialog').modal('show');
	});

	$(document).delegate('#btnCfDonotSMX', 'click', function() {

		$('#modal_dialog').modal('hide');
		$('#cur_spw_key').val('');

	});

	$(document).delegate('#btnCfSMX', 'click', function() {

		acq_sendtomix($('#cur_spw_key').val());

	});


});





function acq_sendtotemplate(fm_id) {


	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_fw_sendtotemplate.php",
	  async:false,
	  data: {
	  	"fm_id": fm_id
//	  	"acq_desc": acq_desc
		},
	  cache: false,
	  beforeSend: function() {
	  	$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	  	$('.modal-header').children('h4').html('On process');
			$('.modal-body').children().html('<div class="overlay" style="background: rgba(238, 238, 238, 0);"><i class="fa fa-spinner fa-pulse fa-3x fa-fw" style="margin-left: 15%;"></i><h4 style="margin-top: -5%; text-align:center;">Do not close this box. Please wait...</h4></div>');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
			$('#modal_dialog').modal('show');
	  },
	  success: function(result) {
	  	// alert(result);

	  	if(result.match(/logonrequest/)){
      	//Case not logon : go to logon page
      	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
      	$('.modal-header').children('h4').html('An error occurred!');
      	$('.modal-body').children().html('You\'re not login or your session has expired! Please, login again.');
      	$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnGotoLogin');
				$('.modal-footer').children('.btn:nth-child(1)').css('display','');
				$('.modal-footer').children('.btn:nth-child(1)').html('Goto Login');
				$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
      }
			else if(result.match(/denied/)){
      	//Case access denied : show error
      	$('#modal_dialog').modal('hide');
      	$('#mainbox_body').html(result+'<br/><br/><br/><br/><br/><br/>');
			}
      else{
      	//Normal case : show search result
      	//Normal case : show search result
      	var result_arr = result.split('|');
         // alert(result_arr[0]);
      	if(result_arr[0] == '1'){
      		//Inform success to user
					$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');

					// Remove from pd_order table
				  // $('#row_'+pd_order).remove();
				  // 					// Remove from pd_order table
				  $('a[id^="settmp_"]').removeClass('bg-yellow').addClass('bg-green');
				  $('#settmp_'+fm_id).removeClass('bg-green').addClass('bg-yellow');
				  $('#edittmp_8').removeClass('bg-yellow').addClass('bg-blue');
				  

      	}
      	else{
      		//Inform error to user
					$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');
      	}

      	// alert(result);
				//$('#mainbox').parent().replaceWith(result);
      	// $('#mainbox').parent().parent().replaceWith(result);
      }
	  },
		error: function(jqXHR, exception) {
	  	var errorStr = '';
	  	//alert(jqXHR.status);

			if(jqXHR.status === 0){
				errorStr = 'Can not connect. Please verify network</p></div>';
			}
			else if(jqXHR.status == 404){
				errorStr = 'Requested page not found [404]</p></div>';
			}
			else if(jqXHR.status == 500){
				errorStr = 'Internal server error [500]</p></div>';
			}
			else if(exception === 'parsererror'){
				errorStr = 'Requested JSON parse failed</p></div>';
			}
			else if(exception === 'timeout'){
				errorStr = 'Time out error</p></div>';
			}
			else if(exception === 'abort'){
				errorStr = 'Ajax request aborted</p></div>';
			}
			else{
				errorStr = 'Uncaught Error : ' + jqXHR.responseText + '</p></div>';
			}

    	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
    	$('.modal-header').children('h4').html('Some problems have occured!');
    	$('.modal-body').children().html(errorStr);
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');

	  }
	});


}




function acq_removetemplate(fm_id) {


	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_fw_removetemplate.php",
	  async:false,
	  data: {
	  	"fm_id": fm_id
//	  	"acq_desc": acq_desc
		},
	  cache: false,
	  beforeSend: function() {
	  	$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	  	$('.modal-header').children('h4').html('On process');
			$('.modal-body').children().html('<div class="overlay" style="background: rgba(238, 238, 238, 0);"><i class="fa fa-spinner fa-pulse fa-3x fa-fw" style="margin-left: 15%;"></i><h4 style="margin-top: -5%; text-align:center;">Do not close this box. Please wait...</h4></div>');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
			$('#modal_dialog').modal('show');
	  },
	  success: function(result) {
	  	// alert(result);

	  	if(result.match(/logonrequest/)){
      	//Case not logon : go to logon page
      	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
      	$('.modal-header').children('h4').html('An error occurred!');
      	$('.modal-body').children().html('You\'re not login or your session has expired! Please, login again.');
      	$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnGotoLogin');
				$('.modal-footer').children('.btn:nth-child(1)').css('display','');
				$('.modal-footer').children('.btn:nth-child(1)').html('Goto Login');
				$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
      }
			else if(result.match(/denied/)){
      	//Case access denied : show error
      	$('#modal_dialog').modal('hide');
      	$('#mainbox_body').html(result+'<br/><br/><br/><br/><br/><br/>');
			}
      else{
      	//Normal case : show search result
      	//Normal case : show search result
      	var result_arr = result.split('|');
         // alert(result_arr[0]);
      	if(result_arr[0] == '1'){
      		//Inform success to user
					$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');

					// Remove from pd_order table
				    $('#row_'+fm_id).remove();
				  // 					// Remove from pd_order table
				  //$('a[id^="settmp_"]').removeClass('bg-yellow').addClass('bg-green');
				  //$('#settmp_'+fm_id).removeClass('bg-green').addClass('bg-yellow');
				  //$('#edittmp_8').removeClass('bg-yellow').addClass('bg-blue');
				  

      	}
      	else{
      		//Inform error to user
					$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');
      	}

      	// alert(result);
				//$('#mainbox').parent().replaceWith(result);
      	// $('#mainbox').parent().parent().replaceWith(result);
      }
	  },
		error: function(jqXHR, exception) {
	  	var errorStr = '';
	  	//alert(jqXHR.status);

			if(jqXHR.status === 0){
				errorStr = 'Can not connect. Please verify network</p></div>';
			}
			else if(jqXHR.status == 404){
				errorStr = 'Requested page not found [404]</p></div>';
			}
			else if(jqXHR.status == 500){
				errorStr = 'Internal server error [500]</p></div>';
			}
			else if(exception === 'parsererror'){
				errorStr = 'Requested JSON parse failed</p></div>';
			}
			else if(exception === 'timeout'){
				errorStr = 'Time out error</p></div>';
			}
			else if(exception === 'abort'){
				errorStr = 'Ajax request aborted</p></div>';
			}
			else{
				errorStr = 'Uncaught Error : ' + jqXHR.responseText + '</p></div>';
			}

    	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
    	$('.modal-header').children('h4').html('Some problems have occured!');
    	$('.modal-body').children().html(errorStr);
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');

	  }
	});


}

function acq_modifytemplate(fm_id) {


	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)



	$.ajax({
	  type: "POST",
	  url: "ajax_fw_modifytemplate.php",
	  async:false,
	  data: {
	  	"fm_id": fm_id
//	  	"acq_desc": acq_desc
		},
	  cache: false,
	  beforeSend: function() {
	  	$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	  	$('.modal-header').children('h4').html('On process');
			$('.modal-body').children().html('<div class="overlay" style="background: rgba(238, 238, 238, 0);"><i class="fa fa-spinner fa-pulse fa-3x fa-fw" style="margin-left: 15%;"></i><h4 style="margin-top: -5%; text-align:center;">Do not close this box. Please wait...</h4></div>');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
			$('#modal_dialog').modal('show');
	  },
	  success: function(result) {
	  	// alert(result);

	  	if(result.match(/logonrequest/)){
      	//Case not logon : go to logon page
      	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
      	$('.modal-header').children('h4').html('An error occurred!');
      	$('.modal-body').children().html('You\'re not login or your session has expired! Please, login again.');
      	$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnGotoLogin');
				$('.modal-footer').children('.btn:nth-child(1)').css('display','');
				$('.modal-footer').children('.btn:nth-child(1)').html('Goto Login');
				$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
      }
			else if(result.match(/denied/)){
      	//Case access denied : show error
      	$('#modal_dialog').modal('hide');
      	$('#mainbox_body').html(result+'<br/><br/><br/><br/><br/><br/>');
			}
      else{
      	//Normal case : show search result
      	//Normal case : show search result
      	var result_arr = result.split('|');
         // alert(result_arr[0]);
      	if(result_arr[0] == '1'){
      		//Inform success to user
					$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');

					// Remove from pd_order table
				  // $('#row_'+pd_order).remove();
				  // 					// Remove from pd_order table
				  $('a[id^="settmp_"]').removeClass('bg-yellow').addClass('bg-green');
				  $('#settmp_'+fm_id).removeClass('bg-green').addClass('bg-yellow');
				  $('#edittmp_8').removeClass('bg-yellow').addClass('bg-blue');
				  

      	}
      	else{
      		//Inform error to user
					$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');
      	}

      	// alert(result);
				//$('#mainbox').parent().replaceWith(result);
      	// $('#mainbox').parent().parent().replaceWith(result);
      }
	  },
		error: function(jqXHR, exception) {
	  	var errorStr = '';
	  	//alert(jqXHR.status);

			if(jqXHR.status === 0){
				errorStr = 'Can not connect. Please verify network</p></div>';
			}
			else if(jqXHR.status == 404){
				errorStr = 'Requested page not found [404]</p></div>';
			}
			else if(jqXHR.status == 500){
				errorStr = 'Internal server error [500]</p></div>';
			}
			else if(exception === 'parsererror'){
				errorStr = 'Requested JSON parse failed</p></div>';
			}
			else if(exception === 'timeout'){
				errorStr = 'Time out error</p></div>';
			}
			else if(exception === 'abort'){
				errorStr = 'Ajax request aborted</p></div>';
			}
			else{
				errorStr = 'Uncaught Error : ' + jqXHR.responseText + '</p></div>';
			}

    	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
    	$('.modal-header').children('h4').html('Some problems have occured!');
    	$('.modal-body').children().html(errorStr);
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');

	  }
	});


}




/***** out scropt ****/







function acq_sendtomix(pd_order) {


	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix.php",
	  async:false,
	  data: {
	  	"pd_order": pd_order
//	  	"acq_desc": acq_desc
		},
	  cache: false,
	  beforeSend: function() {
	  	$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	  	$('.modal-header').children('h4').html('On process');
			$('.modal-body').children().html('<div class="overlay" style="background: rgba(238, 238, 238, 0);"><i class="fa fa-spinner fa-pulse fa-3x fa-fw" style="margin-left: 15%;"></i><h4 style="margin-top: -5%; text-align:center;">Do not close this box. Please wait...</h4></div>');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
			$('#modal_dialog').modal('show');
	  },
	  success: function(result) {
	  	// alert(result);

	  	if(result.match(/logonrequest/)){
      	//Case not logon : go to logon page
      	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
      	$('.modal-header').children('h4').html('An error occurred!');
      	$('.modal-body').children().html('You\'re not login or your session has expired! Please, login again.');
      	$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnGotoLogin');
				$('.modal-footer').children('.btn:nth-child(1)').css('display','');
				$('.modal-footer').children('.btn:nth-child(1)').html('Goto Login');
				$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
      }
			else if(result.match(/denied/)){
      	//Case access denied : show error
      	$('#modal_dialog').modal('hide');
      	$('#mainbox_body').html(result+'<br/><br/><br/><br/><br/><br/>');
			}
      else{
      	//Normal case : show search result
      	//Normal case : show search result
      	var result_arr = result.split('|');
         // alert(result_arr[0]);
      	if(result_arr[0] == '1'){
      		//Inform success to user
					$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');

					// Remove from pd_order table
				  $('#row_'+pd_order).remove();

      	}
      	else{
      		//Inform error to user
					$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');
      	}

      	// alert(result);
				//$('#mainbox').parent().replaceWith(result);
      	// $('#mainbox').parent().parent().replaceWith(result);
      }
	  },
		error: function(jqXHR, exception) {
	  	var errorStr = '';
	  	//alert(jqXHR.status);

			if(jqXHR.status === 0){
				errorStr = 'Can not connect. Please verify network</p></div>';
			}
			else if(jqXHR.status == 404){
				errorStr = 'Requested page not found [404]</p></div>';
			}
			else if(jqXHR.status == 500){
				errorStr = 'Internal server error [500]</p></div>';
			}
			else if(exception === 'parsererror'){
				errorStr = 'Requested JSON parse failed</p></div>';
			}
			else if(exception === 'timeout'){
				errorStr = 'Time out error</p></div>';
			}
			else if(exception === 'abort'){
				errorStr = 'Ajax request aborted</p></div>';
			}
			else{
				errorStr = 'Uncaught Error : ' + jqXHR.responseText + '</p></div>';
			}

    	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
    	$('.modal-header').children('h4').html('Some problems have occured!');
    	$('.modal-body').children().html(errorStr);
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');

	  }
	});


}

function acq_sendtoplan(pd_order){

	// alert('pd_order = '+pd_order);

	$.ajax({
	  type: "POST",
	  url: "ajax_pdrequest_sendtoplan.php",
	  data: {
	  	"pd_order": pd_order
	  	// ,"batch_no": batch_no
//	  	"acq_desc": acq_desc
		},
	  cache: false,
	  beforeSend: function() {
	  	$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	  	$('.modal-header').children('h4').html('On process');
			$('.modal-body').children().html('<div class="overlay" style="background: rgba(238, 238, 238, 0);"><i class="fa fa-spinner fa-pulse fa-3x fa-fw" style="margin-left: 15%;"></i><h4 style="margin-top: -5%; text-align:center;">Do not close this box. Please wait...</h4></div>');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
			$('#modal_dialog').modal('show');
	  },
	  success: function(result) {
	  	// alert(result);

	  	if(result.match(/logonrequest/)){
      	//Case not logon : go to logon page
      	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
      	$('.modal-header').children('h4').html('An error occurred!');
      	$('.modal-body').children().html('You\'re not login or your session has expired! Please, login again.');
      	$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnGotoLogin');
				$('.modal-footer').children('.btn:nth-child(1)').css('display','');
				$('.modal-footer').children('.btn:nth-child(1)').html('Goto Login');
				$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
      }
			else if(result.match(/denied/)){
      	//Case access denied : show error
      	$('#modal_dialog').modal('hide');
      	$('#mainbox_body').html(result+'<br/><br/><br/><br/><br/><br/>');
			}
      else{
      	//Normal case : show search result
      	//Normal case : show search result
      	var result_arr = result.split('|');
         // alert(result_arr[0]);
      	if(result_arr[0] == '1'){
      		//Inform success to user
					$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');

					// Remove from pd_order table
				  $('#row_'+pd_order).remove();

      	}
      	else{
      		//Inform error to user
					$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');
      	}

      	// alert(result);
				//$('#mainbox').parent().replaceWith(result);
      	// $('#mainbox').parent().parent().replaceWith(result);
      }
	  },
		error: function(jqXHR, exception) {
	  	var errorStr = '';
	  	//alert(jqXHR.status);

			if(jqXHR.status === 0){
				errorStr = 'Can not connect. Please verify network</p></div>';
			}
			else if(jqXHR.status == 404){
				errorStr = 'Requested page not found [404]</p></div>';
			}
			else if(jqXHR.status == 500){
				errorStr = 'Internal server error [500]</p></div>';
			}
			else if(exception === 'parsererror'){
				errorStr = 'Requested JSON parse failed</p></div>';
			}
			else if(exception === 'timeout'){
				errorStr = 'Time out error</p></div>';
			}
			else if(exception === 'abort'){
				errorStr = 'Ajax request aborted</p></div>';
			}
			else{
				errorStr = 'Uncaught Error : ' + jqXHR.responseText + '</p></div>';
			}

    	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
    	$('.modal-header').children('h4').html('Some problems have occured!');
    	$('.modal-body').children().html(errorStr);
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');

	  }
	});

}


function acq_delaccount(userid){

	// alert('userid = '+userid);

	$.ajax({
	  type: "POST",
	  url: "ajax_delete_accno.php",
	  data: {
	  	"userid": userid
	  	// ,"batch_no": batch_no
     //	 "acq_desc": acq_desc
		},
	  cache: false,
	  beforeSend: function() {
	  	$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	  	$('.modal-header').children('h4').html('On process');
			$('.modal-body').children().html('<div class="overlay" style="background: rgba(238, 238, 238, 0);"><i class="fa fa-spinner fa-pulse fa-3x fa-fw" style="margin-left: 15%;"></i><h4 style="margin-top: -5%; text-align:center;">Do not close this box. Please wait...</h4></div>');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
			$('#modal_dialog').modal('show');
	  },
	  success: function(result) {
	  	// alert(result);

	  	if(result.match(/logonrequest/)){
      	//Case not logon : go to logon page
      	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
      	$('.modal-header').children('h4').html('An error occurred!');
      	$('.modal-body').children().html('You\'re not login or your session has expired! Please, login again.');
      	$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnGotoLogin');
				$('.modal-footer').children('.btn:nth-child(1)').css('display','');
				$('.modal-footer').children('.btn:nth-child(1)').html('Goto Login');
				$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
      }
			else if(result.match(/denied/)){
      	//Case access denied : show error
      	$('#modal_dialog').modal('hide');
      	$('#mainbox_body').html(result+'<br/><br/><br/><br/><br/><br/>');
			}
      else{
      	//Normal case : show search result
      	//Normal case : show search result
      	var result_arr = result.split('|');
         // alert(result_arr[0]);
      	if(result_arr[0] == '1'){
      		//Inform success to user
					$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');

					// Remove from pd_order table
				  $('#row_'+userid).remove();

      	}
      	else{
      		//Inform error to user
					$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');
      	}

      	// alert(result);
				//$('#mainbox').parent().replaceWith(result);
      	// $('#mainbox').parent().parent().replaceWith(result);
      }
	  },
		error: function(jqXHR, exception) {
	  	var errorStr = '';
	  	//alert(jqXHR.status);

			if(jqXHR.status === 0){
				errorStr = 'Can not connect. Please verify network</p></div>';
			}
			else if(jqXHR.status == 404){
				errorStr = 'Requested page not found [404]</p></div>';
			}
			else if(jqXHR.status == 500){
				errorStr = 'Internal server error [500]</p></div>';
			}
			else if(exception === 'parsererror'){
				errorStr = 'Requested JSON parse failed</p></div>';
			}
			else if(exception === 'timeout'){
				errorStr = 'Time out error</p></div>';
			}
			else if(exception === 'abort'){
				errorStr = 'Ajax request aborted</p></div>';
			}
			else{
				errorStr = 'Uncaught Error : ' + jqXHR.responseText + '</p></div>';
			}

    	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
    	$('.modal-header').children('h4').html('Some problems have occured!');
    	$('.modal-body').children().html(errorStr);
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');

	  }
	});

}

function acq_inactiveaccount(userid){

	// alert('userid = '+userid);

	$.ajax({
	  type: "POST",
	  url: "ajax_inactive_accno.php",
	  data: {
	  	"userid": userid
	  	// ,"batch_no": batch_no
     //	 "acq_desc": acq_desc
		},
	  cache: false,
	  beforeSend: function() {
	  	$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	  	$('.modal-header').children('h4').html('On process');
			$('.modal-body').children().html('<div class="overlay" style="background: rgba(238, 238, 238, 0);"><i class="fa fa-spinner fa-pulse fa-3x fa-fw" style="margin-left: 15%;"></i><h4 style="margin-top: -5%; text-align:center;">Do not close this box. Please wait...</h4></div>');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
			$('#modal_dialog').modal('show');
	  },
	  success: function(result) {
	  	// alert(result);

	  	if(result.match(/logonrequest/)){
      	//Case not logon : go to logon page
      	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
      	$('.modal-header').children('h4').html('An error occurred!');
      	$('.modal-body').children().html('You\'re not login or your session has expired! Please, login again.');
      	$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnGotoLogin');
				$('.modal-footer').children('.btn:nth-child(1)').css('display','');
				$('.modal-footer').children('.btn:nth-child(1)').html('Goto Login');
				$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
      }
			else if(result.match(/denied/)){
      	//Case access denied : show error
      	$('#modal_dialog').modal('hide');
      	$('#mainbox_body').html(result+'<br/><br/><br/><br/><br/><br/>');
			}
      else{
      	//Normal case : show search result
      	//Normal case : show search result
      	var result_arr = result.split('|');
         // alert(result_arr[0]);
      	if(result_arr[0] == '1'){
      		//Inform success to user
					$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');

					// Remove from pd_order table
				  $('#userstatus_'+userid).html('N');  // work

      	}
      	else{
      		//Inform error to user
					$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');
      	}

      	// alert(result);
				//$('#mainbox').parent().replaceWith(result);
      	// $('#mainbox').parent().parent().replaceWith(result);
      }
	  },
		error: function(jqXHR, exception) {
	  	var errorStr = '';
	  	//alert(jqXHR.status);

			if(jqXHR.status === 0){
				errorStr = 'Can not connect. Please verify network</p></div>';
			}
			else if(jqXHR.status == 404){
				errorStr = 'Requested page not found [404]</p></div>';
			}
			else if(jqXHR.status == 500){
				errorStr = 'Internal server error [500]</p></div>';
			}
			else if(exception === 'parsererror'){
				errorStr = 'Requested JSON parse failed</p></div>';
			}
			else if(exception === 'timeout'){
				errorStr = 'Time out error</p></div>';
			}
			else if(exception === 'abort'){
				errorStr = 'Ajax request aborted</p></div>';
			}
			else{
				errorStr = 'Uncaught Error : ' + jqXHR.responseText + '</p></div>';
			}

    	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
    	$('.modal-header').children('h4').html('Some problems have occured!');
    	$('.modal-body').children().html(errorStr);
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');

	  }
	});

}

function acq_activeaccount(userid){

	 //alert('userid = '+userid);

	$.ajax({
	  type: "POST",
	  url: "ajax_active_accno.php",
	  data: {
	  	"userid": userid
	  	// ,"batch_no": batch_no
     //	 "acq_desc": acq_desc
		},
	  cache: false,
	  beforeSend: function() {
	  	$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	  	$('.modal-header').children('h4').html('On process');
			$('.modal-body').children().html('<div class="overlay" style="background: rgba(238, 238, 238, 0);"><i class="fa fa-spinner fa-pulse fa-3x fa-fw" style="margin-left: 15%;"></i><h4 style="margin-top: -5%; text-align:center;">Do not close this box. Please wait...</h4></div>');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
			$('#modal_dialog').modal('show');
	  },
	  success: function(result) {
	  	// alert(result);

	  	if(result.match(/logonrequest/)){
      	//Case not logon : go to logon page
      	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
      	$('.modal-header').children('h4').html('An error occurred!');
      	$('.modal-body').children().html('You\'re not login or your session has expired! Please, login again.');
      	$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnGotoLogin');
				$('.modal-footer').children('.btn:nth-child(1)').css('display','');
				$('.modal-footer').children('.btn:nth-child(1)').html('Goto Login');
				$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
      }
			else if(result.match(/denied/)){
      	//Case access denied : show error
      	$('#modal_dialog').modal('hide');
      	$('#mainbox_body').html(result+'<br/><br/><br/><br/><br/><br/>');
			}
      else{
      	//Normal case : show search result
      	//Normal case : show search result
      	var result_arr = result.split('|');
         // alert(result_arr[0]);
      	if(result_arr[0] == '1'){
      		//Inform success to user
					$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');

					// Remove from pd_order table
				  $('#userstatus_'+userid).html('A');  // work

      	}
      	else{
      		//Inform error to user
					$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');
      	}

      	// alert(result);
				//$('#mainbox').parent().replaceWith(result);
      	// $('#mainbox').parent().parent().replaceWith(result);
      }
	  },
		error: function(jqXHR, exception) {
	  	var errorStr = '';
	  	//alert(jqXHR.status);

			if(jqXHR.status === 0){
				errorStr = 'Can not connect. Please verify network</p></div>';
			}
			else if(jqXHR.status == 404){
				errorStr = 'Requested page not found [404]</p></div>';
			}
			else if(jqXHR.status == 500){
				errorStr = 'Internal server error [500]</p></div>';
			}
			else if(exception === 'parsererror'){
				errorStr = 'Requested JSON parse failed</p></div>';
			}
			else if(exception === 'timeout'){
				errorStr = 'Time out error</p></div>';
			}
			else if(exception === 'abort'){
				errorStr = 'Ajax request aborted</p></div>';
			}
			else{
				errorStr = 'Uncaught Error : ' + jqXHR.responseText + '</p></div>';
			}

    	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
    	$('.modal-header').children('h4').html('Some problems have occured!');
    	$('.modal-body').children().html(errorStr);
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');

	  }
	});

}


function acq_clearlogoncount(userid){

	 //alert('userid = '+userid);

	$.ajax({
	  type: "POST",
	  url: "ajax_clearlogcnt_accno.php",
	  data: {
	  	"userid": userid
	  	// ,"batch_no": batch_no
     //	 "acq_desc": acq_desc
		},
	  cache: false,
	  beforeSend: function() {
	  	$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	  	$('.modal-header').children('h4').html('On process');
			$('.modal-body').children().html('<div class="overlay" style="background: rgba(238, 238, 238, 0);"><i class="fa fa-spinner fa-pulse fa-3x fa-fw" style="margin-left: 15%;"></i><h4 style="margin-top: -5%; text-align:center;">Do not close this box. Please wait...</h4></div>');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
			$('#modal_dialog').modal('show');
	  },
	  success: function(result) {
	  	// alert(result);

	  	if(result.match(/logonrequest/)){
      	//Case not logon : go to logon page
      	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
      	$('.modal-header').children('h4').html('An error occurred!');
      	$('.modal-body').children().html('You\'re not login or your session has expired! Please, login again.');
      	$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnGotoLogin');
				$('.modal-footer').children('.btn:nth-child(1)').css('display','');
				$('.modal-footer').children('.btn:nth-child(1)').html('Goto Login');
				$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
      }
			else if(result.match(/denied/)){
      	//Case access denied : show error
      	$('#modal_dialog').modal('hide');
      	$('#mainbox_body').html(result+'<br/><br/><br/><br/><br/><br/>');
			}
      else{
      	//Normal case : show search result
      	//Normal case : show search result
      	var result_arr = result.split('|');
         // alert(result_arr[0]);
      	if(result_arr[0] == '1'){
      		//Inform success to user
					$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');

					// Remove from pd_order table
				  // $('#userstatus_'+userid).html('N');  // work

      	}
      	else{
      		//Inform error to user
					$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');
      	}

      	// alert(result);
				//$('#mainbox').parent().replaceWith(result);
      	// $('#mainbox').parent().parent().replaceWith(result);
      }
	  },
		error: function(jqXHR, exception) {
	  	var errorStr = '';
	  	//alert(jqXHR.status);

			if(jqXHR.status === 0){
				errorStr = 'Can not connect. Please verify network</p></div>';
			}
			else if(jqXHR.status == 404){
				errorStr = 'Requested page not found [404]</p></div>';
			}
			else if(jqXHR.status == 500){
				errorStr = 'Internal server error [500]</p></div>';
			}
			else if(exception === 'parsererror'){
				errorStr = 'Requested JSON parse failed</p></div>';
			}
			else if(exception === 'timeout'){
				errorStr = 'Time out error</p></div>';
			}
			else if(exception === 'abort'){
				errorStr = 'Ajax request aborted</p></div>';
			}
			else{
				errorStr = 'Uncaught Error : ' + jqXHR.responseText + '</p></div>';
			}

    	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
    	$('.modal-header').children('h4').html('Some problems have occured!');
    	$('.modal-body').children().html(errorStr);
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');

	  }
	});

}

function acq_sysnctoplc(){

	 //alert('userid = '+userid);

	$.ajax({
	  type: "POST",
	  url: "ajax_syncusertoplc.php",
	  data: {
	  	// "userid": userid
	  	// ,"batch_no": batch_no
     //	 "acq_desc": acq_desc
		},
	  cache: false,
	  beforeSend: function() {
	  	$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	  	$('.modal-header').children('h4').html('On process');
			$('.modal-body').children().html('<div class="overlay" style="background: rgba(238, 238, 238, 0);"><i class="fa fa-spinner fa-pulse fa-3x fa-fw" style="margin-left: 15%;"></i><h4 style="margin-top: -5%; text-align:center;">Do not close this box. Please wait...</h4></div>');
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
			$('#modal_dialog').modal('show');
	  },
	  success: function(result) {
	  	// alert(result);

	  	if(result.match(/logonrequest/)){
      	//Case not logon : go to logon page
      	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
      	$('.modal-header').children('h4').html('An error occurred!');
      	$('.modal-body').children().html('You\'re not login or your session has expired! Please, login again.');
      	$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnGotoLogin');
				$('.modal-footer').children('.btn:nth-child(1)').css('display','');
				$('.modal-footer').children('.btn:nth-child(1)').html('Goto Login');
				$('.modal-footer').children('.btn:nth-child(2)').css('display','none');
      }
			else if(result.match(/denied/)){
      	//Case access denied : show error
      	$('#modal_dialog').modal('hide');
      	$('#mainbox_body').html(result+'<br/><br/><br/><br/><br/><br/>');
			}
      else{
      	//Normal case : show search result
      	//Normal case : show search result
      	var result_arr = result.split('|');
         // alert(result_arr[0]);
      	if(result_arr[0] == '1'){
      		//Inform success to user
					$('#modal_dialog').removeClass('modal-warning').addClass('modal-success');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');

					// Remove from pd_order table
				  $('#ret_sysntoplc').html('Sync All USER TO PLC Success');  

      	}
      	else{
      		//Inform error to user
					$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
	      	$('.modal-header').children('h4').html(result_arr[1]);
	      	$('.modal-body').children().html(result_arr[2]);
					$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
					$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnClose');
					$('.modal-footer').children('.btn:nth-child(2)').html('Close');
					$('.modal-footer').children('.btn:nth-child(2)').css('display','');
					$('#cur_del_key').val('');
      	}

      	// alert(result);
				//$('#mainbox').parent().replaceWith(result);
      	//$('#mainbox').parent().parent().replaceWith(result);
      }
	  },
		error: function(jqXHR, exception) {
	  	var errorStr = '';
	  	//alert(jqXHR.status);

			if(jqXHR.status === 0){
				errorStr = 'Can not connect. Please verify network</p></div>';
			}
			else if(jqXHR.status == 404){
				errorStr = 'Requested page not found [404]</p></div>';
			}
			else if(jqXHR.status == 500){
				errorStr = 'Internal server error [500]</p></div>';
			}
			else if(exception === 'parsererror'){
				errorStr = 'Requested JSON parse failed</p></div>';
			}
			else if(exception === 'timeout'){
				errorStr = 'Time out error</p></div>';
			}
			else if(exception === 'abort'){
				errorStr = 'Ajax request aborted</p></div>';
			}
			else{
				errorStr = 'Uncaught Error : ' + jqXHR.responseText + '</p></div>';
			}

    	$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
    	$('.modal-header').children('h4').html('Some problems have occured!');
    	$('.modal-body').children().html(errorStr);
			$('.modal-footer').children('.btn:nth-child(1)').css('display','none');
			$('.modal-footer').children('.btn:nth-child(2)').css('display','');
			$('.modal-footer').children('.btn:nth-child(2)').html('Close');

	  }
	});

}
// acq_sendtodel