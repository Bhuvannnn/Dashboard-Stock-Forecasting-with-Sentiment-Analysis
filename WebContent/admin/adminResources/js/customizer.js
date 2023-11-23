$('#myDropdown .dropdown-menu').on({
	"click":function(e){
      e.stopPropagation();
    }
});
$('.closer').on('click', function () {
    $('.btn-group').removeClass('open');
});