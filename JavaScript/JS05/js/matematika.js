function osszead() {
    var szam1 = parseInt(document.getElementById("szam1").value)
    var szam2 = parseInt(document.getElementById("szam2").value)
    var osszeg = szam1 + szam2
    document.getElementById("osszeg").value = osszeg
}
