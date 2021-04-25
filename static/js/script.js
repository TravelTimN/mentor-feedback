document.addEventListener("DOMContentLoaded", function () {
    let datepicker = document.querySelectorAll(".datepicker");
    M.Datepicker.init(datepicker, {format: "dd/mm/yyyy"});
});
