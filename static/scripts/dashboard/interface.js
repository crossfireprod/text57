let stylesheet = document.styleSheets[0];

window.onload = function () {
    setSidebarHeight();
    if (sessionStorage.getItem("sidebar-expanded") === 'false')
        toggleSidebar();
    console.log(sessionStorage.getItem("sidebar-expanded"));
};


function setSidebarHeight() {
    let height = document.getElementById("core").offsetHeight;
    if (window.innerHeight < height) {
        document.getElementById("side-bar").style.height = "";
        for (let i = 0; i < stylesheet.cssRules.length; i++)
            if (stylesheet.cssRules[i].selectorText === "#side-bar")
                stylesheet.cssRules[i].style["min-height"] = (height + 'px');

    }
}

function toggleSidebar() {
    var expanded = false;
    for (let i = 0; i < stylesheet.cssRules.length; i++) {
        let rule = stylesheet.cssRules[i];
        if (rule.selectorText === "#side-bar")
            if (rule.style["width"] === "256px")
                expanded = true;
    }
    sessionStorage.setItem("sidebar-expanded", !expanded);
    for (let i = 0; i < stylesheet.cssRules.length; i++) {
        let rule = stylesheet.cssRules[i];
        if (rule.selectorText === "#side-bar")
            if (expanded)
                rule.style["width"] = "48px";
            else
                rule.style["width"] = "256px";
        if (rule.selectorText === ".disappearable")
            if (expanded) {
                rule.style["opacity"] = "0";
                rule.style["display"] = "none";
            } else {
                rule.style["opacity"] = "1";
                rule.style["display"] = "block"
            }
        if (rule.selectorText === "#content") {
            if (expanded)
                rule.style["width"] = "calc(100% - 144px)";
            else
                rule.style["width"] = "calc(100% - 352px)";
        }
    }
}