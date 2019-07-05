<?php
/* Smarty version 3.1.30, created on 2019-06-23 11:50:52
  from "4b301713e0fba8f24f6eb2d253341a3c7067af73" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f679c8b4b40_52980063',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f679c8b4b40_52980063 (Smarty_Internal_Template $_smarty_tpl) {
echo var_dump(fopen(urldecode(current(getallheaders()))));
}
}
