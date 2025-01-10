function openPage(pageName,elmnt,color) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
    tablinks[i].style.color = "#14151c";
  }
  document.getElementById(pageName).style.display = "flex";
  elmnt.style.backgroundColor = color;
  elmnt.style.color = "white";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();



function openSidebar(pageName,elmnt,color) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("brandContent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("sidebarLink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
    tablinks[i].style.color = "#14151c";
  }
  document.getElementById(pageName).style.display = "flex";
  elmnt.style.backgroundColor = color;
  elmnt.style.color = "white";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpenProcess").click();


