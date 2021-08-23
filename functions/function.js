function fun_one() {
    return fun_two();
}
function fun_two() {
    return "welcome";
}
document.write(fun_one + "<br>");
document.write(fun_one());
