function emergencyDrill() {
    let text_area = document.getElementById("send-message");
    text_area.value = "EMERGENCY PROCEDURES DRILL - Please gather your unit and assemble on the parade field.";
}

function classBColors() {
    let text_area = document.getElementById("send-message");
    text_area.value = "CLASS B COLORS - This evening, pleas,e have your unit wear class Bs to colors.";
}

function severeWeather() {
    let text_area = document.getElementById("send-message");
    text_area.value = "SEVERE WEATHER WARNING - Please assemble those around you and SEEK SAFE COVER IMMEDIATELY. ";
}

function campAssembly() {
    let text_area = document.getElementById("send-message");
    text_area.value = "URGENT: Please gather those around you and assemble with your unit on the parade field.";
}

function hide(id) {
    let element = document.getElementById(id);
    element.style.display = 'none';
}