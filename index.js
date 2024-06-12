console.log("Hare Krishna");

function openCategory(evt, category) {
    var i, tabcontent, pill, pillu;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    pill = document.getElementsByClassName("pill");
    for (i = 0; i < pill.length; i++) {
      pill[i].className = pill[i].className.replace(" pill-active", "");
    }
    pillu = document.getElementsByClassName("pillu");
    for (i = 0; i < pillu.length; i++) {
      pillu[i].className = pillu[i].className.replace(" pill-icon-active", "");
    }
    document.getElementById(category).style.display = "block";
    evt.currentTarget.className += " pill-active";
    console.log(evt.currentTarget.querySelector(".pillu"));
    evt.currentTarget.querySelector(".pillu").className += " pill-icon-active";
  }
  
  document.getElementById("defaultOpen").click();