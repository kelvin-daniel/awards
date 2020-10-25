$(document).ready(function() {
  $("#love").click(function(){
    $("#love").hide()
    $(".form").slideDown(2000)
      $(".form").show()

  })

  $("#click").click(function(){
    $("#search").show()
    $("#click").hide()
  })
})