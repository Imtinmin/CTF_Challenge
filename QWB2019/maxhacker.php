
<?php
function system($a){
if ($a != " ") {
debug_print_backtrace();
}
}
function shell_exec($a){
if ($a != " ") {
debug_print_backtrace();
}
}
function assert($a){
if ($a != " ") {
debug_print_backtrace();
}
}
function preg_replace($a,$b){
if ($b != " ") {
debug_print_backtrace();
}
}