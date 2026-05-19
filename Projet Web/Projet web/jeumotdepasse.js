function Click() {

    let mdp = document.getElementById("mdp").value;

    let conditions = [

        mdp.length >= 8,

        /[!#$%&*+,\-./:;<=>?@\\^_{}~()]/.test(mdp),

        /[A-Z]/.test(mdp),

        sommeChiffres(mdp) % 5 == 0 && mdp.length > 0,

        mdp.includes("grancher"),

        mdp.includes("FOOOOOORT"),

        mdp.includes("1214"),

        mdp.includes("@gmail.com")
    ];

    /* RESET */

    for (let i = 1; i <= 8; i++) {

        let condition = document.getElementById("condition" + i);

        condition.style.display = "none";
    }

    document.getElementById("lienSecret").style.display = "none";

    /* AFFICHAGE UNE PAR UNE */

    for (let i = 0; i < conditions.length; i++) {

        let condition = document.getElementById("condition" + (i + 1));

        condition.style.display = "block";

        if (conditions[i]) {

            condition.style.color = "lightgreen";

        } else {

            condition.style.color = "red";

            break;
        }
    }

    /* SI TOUT EST BON */

    let toutBon = true;

    for (let i = 0; i < conditions.length; i++) {

        if (!conditions[i]) {

            toutBon = false;
        }
    }

    if (toutBon) {

        document.getElementById("lienSecret").style.display = "block";
    }
}

/* SOMME DES CHIFFRES */

function sommeChiffres(mdp) {

    let somme = 0;

    for (let i = 0; i < mdp.length; i++) {

        if (!isNaN(mdp[i]) && mdp[i] != " ") {

            somme += Number(mdp[i]);
        }
    }

    return somme;
}