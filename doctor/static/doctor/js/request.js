window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function setEpertise(string) {
    document.getElementById("expertise").value = string;
    document.getElementById("expertiseDropdown").classList.remove("show");
}

function setCity(string) {
    document.getElementById("city").value = string;
    document.getElementById("cityDropdown").classList.remove("show");
}

function filterFunction(id, dropdown) {
    var input, filter, ul, li, a, i;
    input = document.getElementById(id);
    div = document.getElementById(dropdown);
    if (input.value.length >= 2) {
        filter = input.value.toUpperCase();
        div.classList.add("show");
        a = div.getElementsByClassName("op");
        for (i = 0; i < a.length; i++) {
            txtValue = a[i].textContent || a[i].innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                a[i].style.display = "";
            } else {
                a[i].style.display = "none";
            }
        }
    } else div.classList.remove("show");
}

function integer(id) {
    ipt = div.getElementById(id)

}

function rst() {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
        }
    }
}