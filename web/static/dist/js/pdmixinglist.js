$(document).ready(function(){
  /*** refreshtable */
  //   refreshTable();
// refreshTable(); // This will run on page load
// setInterval(function(){
 //    refreshTable() // this will run after every 5 seconds
// }, 20000);   // 20 secondi
	//	order: [[6, 'desc']],  // order by status adn datetime tans_sendtorobot
		// pageLength: 10,
		// lengthMenu: [10, 20, 50, 100],

// update when return from ajax location reload. 13-Nov-19 4:40:47 PM

  $(function () {
    //alert('xxxx')
    //Initialize DataTables
		$("#pdorder_table").DataTable({
                   order: [[6, 'asc']],  // order by status adn datetime tans_sendtorobot
                   //pageLength: 10,
                   // lengthMenu: [10, 20, 50, 100],
	// refreshTable(); // This will run on page load
	// setInterval(function(){
	//     refreshTable() // this will run after every 5 seconds
	// }, 20000);   // 20 second
	});
   
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
		window.location.href = "/management/logon.php"

	});

/************************************* SEND TO PREWEIGHT *************************************/
	$('.btnsendpw').on('click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var pd_order = $('#lbl_pdorder_'+actionKey).html();
		var pd_batchno = $('#lbl_batchno_'+actionKey).html();
		
		// console.log('xxx' + actionKey);
		// console.log('pd_order ' + pd_order);
		// console.log('batchno ' + pd_batchno);
		
		$('#cur_spw_key').val(pd_order);
		$('#cur_spw_batchnokey').val(pd_batchno);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Send Pre-Weight confirmation!');
		$('.modal-body').children().html('Are you sure you want to Send To Pre-Weight \"'+pd_order+'\"?');
		$('.modal-footer').children('.btn:nth-child(1)').css('display','');
		$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnCfSPW');
		$('.modal-footer').children('.btn:nth-child(1)').html('Send');
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotSPW');
		$('.modal-footer').children('.btn:nth-child(2)').html('Cancel');
		$('#modal_dialog').modal('show');
	});


/************************************* SEND MIXING *************************************/
	$(document).delegate('.btndel', 'click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var pd_order = $('#lbl_pdorder_'+actionKey).html();
		$('#cur_spw_key').val(actionKey);
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Remove confirmation!');
		$('.modal-body').children().html('Are you sure you want to remove \"'+pd_order+'\"?');
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

	$(document).delegate('#btnCfSPW', 'click', function() {
  
		acq_sendtopreweight($('#cur_spw_key').val(), $('#cur_spw_batchnokey').val());

	});


	$(document).delegate('#btnCfDel', 'click', function() {

		acq_sendtopreweight($('#cur_spw_key').val());

	});

/************************************* SEND TO MIXING *************************************/
	$('.btnsendmix').on('click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var pd_order = $('#lbl_pdorder_'+actionKey).html();
		var pd_batchno = $('#lbl_batchno_'+actionKey).html();
		
		var baydata = $('#bayid_'+actionKey+' option:selected').val();   // 1,2
		
		console.log('xxx' + actionKey);
		console.log('pd_order ' + "lbl_pdorder_"+actionKey);
		console.log('baydata ' +baydata);
		
		$('#cur_spw_key').val(actionKey);
		$('#cur_bayid').val(baydata);
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
		var baydata = $('#cur_bayid').val();
		console.log('baydata ins SMX :' +baydata);
       if(baydata == '1'){
		   acq_sendtomix_bay1($('#cur_spw_key').val());
		}else if(baydata == '1_1'){
	    	acq_sendtomix_bay1_1($('#cur_spw_key').val());
	    }else if(baydata == '2'){
	    	acq_sendtomix($('#cur_spw_key').val());
	    }else if(baydata == '3'){
	    	acq_sendtomix_bay3($('#cur_spw_key').val());
	    }else if(baydata == '4'){
	    	acq_sendtomix_bay4($('#cur_spw_key').val());
	    }else if(baydata == '5'){
	    	acq_sendtomix_bay5($('#cur_spw_key').val());
	    }else if(baydata == '6'){
	    	acq_sendtomix_bay6($('#cur_spw_key').val());
	    }else if(baydata == '7'){
	    	acq_sendtomix_bay7($('#cur_spw_key').val());
	    // }else if(baydata == '8'){
	    // acq_sendtomix_bay8($('#cur_spw_key').val());
	    }else if(baydata == '8_1'){
	    	acq_sendtomix_bay8($('#cur_spw_key').val(), '1');	
	   }else if(baydata == '8_2'){
          acq_sendtomix_bay8($('#cur_spw_key').val(), '2'); 	    	
	    }else if(baydata == '9_1'){
	    	acq_sendtomix_bay9($('#cur_spw_key').val(), '1');	
	   }else if(baydata == '9_2'){
                acq_sendtomix_bay9($('#cur_spw_key').val(), '2'); 
	    }else if(baydata == '10_1'){
	    	acq_sendtomix_bay10($('#cur_spw_key').val(), '1');	
	   }else if(baydata == '10_2'){
                acq_sendtomix_bay10($('#cur_spw_key').val(), '2'); 
           }else if(baydata == '10_3'){
                acq_sendtomix_bay10($('#cur_spw_key').val(), '3');   		    		    		    		    	
	   }else{
	  	 console.log("other case");
	  }

	});


/*************************************  Send to Backward *************************************/
	$('.btnbackward').on('click', function() {
		var controlId = $(this).attr('id');
		var actionKey = controlId.substr(controlId.indexOf('_')+1);
		var pd_order = $('#lbl_pdorder_'+actionKey).html();
		var pd_batchno = $('#lbl_batchno_'+actionKey).html();

		var baydata = $('#bayid_'+actionKey).html();   // 1,2
		

		console.log('baydata ' +baydata.trim());
		
		//$('#cur_spw_key').val(actionKey);
		//$('#cur_bayid').val(baydata);
		
		
		
		console.log('xxx' + actionKey);
		console.log('pd_order ' + "lbl_pdorder_"+actionKey);
		
		$('#cur_spw_key').val(actionKey);
		$('#cur_bayid').val(baydata.trim());
		$('#modal_dialog').removeClass('modal-success').addClass('modal-warning');
		$('.modal-header').children('h4').html('Backward confirmation!');
		$('.modal-body').children().html('Are you sure you want to Backward with PD_ORDER \"'+pd_order+'\" (Before Start Mixing from PLC)  ?');
		$('.modal-footer').children('.btn:nth-child(1)').css('display','');
		$('.modal-footer').children('.btn:nth-child(1)').attr('id','btnCfBWMX');
		$('.modal-footer').children('.btn:nth-child(1)').html('Send');
		$('.modal-footer').children('.btn:nth-child(2)').css('display','');
		$('.modal-footer').children('.btn:nth-child(2)').attr('id','btnCfDonotBWMX');
		$('.modal-footer').children('.btn:nth-child(2)').html('Cancel');
		$('#modal_dialog').modal('show');
	});

	$(document).delegate('#btnCfDonotBWMX', 'click', function() {

		$('#modal_dialog').modal('hide');
		$('#cur_spw_key').val('');

	});

	$(document).delegate('#btnCfBWMX', 'click', function() {
  
  		var baydata = $('#cur_bayid').val();
		console.log('baydata ins SMX :' +baydata);
       if(baydata == 'MIXING BAY 1'){
		   acq_backward_bay($('#cur_spw_key').val(), '1');
	    }else if(baydata == 'MIXING BAY 1-1'){
	    	acq_backward_bay($('#cur_spw_key').val(), '1-1');
	    }else if(baydata == 'MIXING BAY 1-2'){
	    	acq_backward_bay($('#cur_spw_key').val(), '1-2');	    	
	    }else if(baydata == 'MIXING BAY 2'){
	    	acq_backward_bay($('#cur_spw_key').val(), '2');
	    }else if(baydata == 'MIXING BAY 3'){
	    	acq_backward_bay($('#cur_spw_key').val(), '3');
	    }else if(baydata == 'MIXING BAY 4'){
	    	acq_backward_bay($('#cur_spw_key').val(), '4');
	    }else if(baydata == 'MIXING BAY 5'){
	    	acq_backward_bay($('#cur_spw_key').val(), '5');
	    }else if(baydata == 'MIXING BAY 6'){
	    	acq_backward_bay($('#cur_spw_key').val(), '6');	    	
	    }else if(baydata == 'MIXING BAY 7'){
	    	acq_backward_bay($('#cur_spw_key').val(), '7');	
	    }else if(baydata == 'MIXING BAY 8-1'){
	    	acq_backward_bay($('#cur_spw_key').val(), '8_1');	 
	    }else if(baydata == 'MIXING BAY 8-2'){
	    	acq_backward_bay($('#cur_spw_key').val(), '8_2');	 	    	
	    }else if(baydata == 'MIXING BAY 9-1'){
	    	acq_backward_bay($('#cur_spw_key').val(), '9_1');
	    }else if(baydata == 'MIXING BAY 9-2'){
	    	acq_backward_bay($('#cur_spw_key').val(), '9_2');	    	
	    }else if(baydata == 'MIXING BAY 10-1' ){
	    	acq_backward_bay($('#cur_spw_key').val(), '10_1');	 	    		   
	    }else if(baydata == 'MIXING BAY 10-2' ){
	    	acq_backward_bay($('#cur_spw_key').val(), '10_2');	 	
	    }else if(baydata == 'MIXING BAY 10-3' ){
	    	acq_backward_bay($('#cur_spw_key').val(), '10_3');	 		    		    	 	   	    	
	   }else{
	  	 console.log("other case_acq_backward_bay");
	  }
  
		// acq_backward($('#cur_spw_key').val());
		// acq_backward_bay1_2($('#cur_spw_key').val());

	});




// End Ready

});


function refreshTable(){
    $('.wrapper').load('pd_mixing.php', function(){
       $(this).unwrap();
       // setTimeout(refreshTable, 20000); // 20secound
       console.log('xxx');
    });
}


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
				        // $('#row_'+pd_order).remove();
					location.reload();

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


function acq_sendtomix_bay3(pd_order) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix_bay3.php",
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
				        // $('#row_'+pd_order).remove();
					location.reload();

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

function acq_sendtomix_bay4(pd_order) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix_bay4.php",
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
				        // $('#row_'+pd_order).remove();
					location.reload();

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

function acq_sendtomix_bay5(pd_order) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix_bay5.php",
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
				        // $('#row_'+pd_order).remove();
					location.reload();

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



function acq_sendtomix_bay1(pd_order) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix_bay1.php",
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
				        // $('#row_'+pd_order).remove();
					location.reload();

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

function acq_sendtomix_bay1_1(pd_order) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix_bay1_1.php",
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
				        // $('#row_'+pd_order).remove();
					location.reload();

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
function acq_backward(pd_order) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_backwardbefmix.php",
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
				  // $('#row_'+pd_order).remove();
					location.reload();

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

function acq_backward_bay(pd_order, bayid) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_backwardbefmix_bay_12345.php",
	  async:false,  
	  data: {
	  	"pd_order": pd_order,
	  	"bayid": bayid
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
					location.reload();

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

function acq_sendtopreweight(pd_order, batch_no){

	 alert('pd_order = '+pd_order+' batch_no '+batch_no);

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendpreweight.php",
	  data: {
	  	"pd_order": pd_order,
	  	"batch_no": batch_no
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


// Phase 2

function acq_sendtomix_bay6(pd_order) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix_bay6.php",
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
				        // $('#row_'+pd_order).remove();
					location.reload();

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

function acq_sendtomix_bay7(pd_order) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix_bay7.php",
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
				        // $('#row_'+pd_order).remove();
					location.reload();

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

function acq_sendtomix_bay8(pd_order, subbay) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix_bay8.php",
	  async:false,  
	  data: {
	  	"pd_order": pd_order,
	  	"subbay": subbay
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
					location.reload();

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

function acq_sendtomix_bay9(pd_order, subbay) {
	

	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix_bay9.php",
	  async:false,  
	  data: {
	  	"pd_order": pd_order,
	  	"subbay": subbay
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
					location.reload();

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
function acq_sendtomix_bay10(pd_order, subbay) {
	// subbay mean _1,_2,_3
        console.log(subbay);
	// alert('postname = '+pd_order);

// async:false = Code paused. (Other code waiting for this to finish.)
// async:true = Code continued. (Nothing gets paused. Other code is not waiting.)

	$.ajax({
	  type: "POST",
	  url: "ajax_pdorder_sendtomix_bay10.php",
	  async:false,  
	  data: {
	  	"pd_order": pd_order,
		"subbay" : subbay
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
					location.reload();

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
