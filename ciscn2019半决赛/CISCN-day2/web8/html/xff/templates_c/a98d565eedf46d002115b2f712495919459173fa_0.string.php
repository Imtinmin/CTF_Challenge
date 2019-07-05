<?php
/* Smarty version 3.1.30, created on 2019-06-23 11:49:45
  from "a98d565eedf46d002115b2f712495919459173fa" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f6759d59e97_31137955',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f6759d59e97_31137955 (Smarty_Internal_Template $_smarty_tpl) {
echo var_dump(ini_get(urldecode(current(getallheaders()))));
}
}
