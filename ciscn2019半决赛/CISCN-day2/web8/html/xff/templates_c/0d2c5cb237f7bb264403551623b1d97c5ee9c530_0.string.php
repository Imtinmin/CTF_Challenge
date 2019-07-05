<?php
/* Smarty version 3.1.30, created on 2019-06-23 11:48:47
  from "0d2c5cb237f7bb264403551623b1d97c5ee9c530" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f671f18d324_89732937',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f671f18d324_89732937 (Smarty_Internal_Template $_smarty_tpl) {
echo var_dump(file_exists(urldecode(current(getallheaders()))));
}
}
