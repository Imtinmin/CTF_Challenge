<?php

/* navigation/logo.twig */
class __TwigTemplate_408baec44992f7c81f44950a77ecafe81eb8941dbbb959abb5c6f18410d89fc7 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = [
        ];
    }

    protected function doDisplay(array $context, array $blocks = [])
    {
        // line 1
        if ((isset($context["display_logo"]) ? $context["display_logo"] : null)) {
            // line 2
            echo "    <div id=\"pmalogo\">
        ";
            // line 3
            if ((isset($context["use_logo_link"]) ? $context["use_logo_link"] : null)) {
                // line 4
                echo "            <a href=\"";
                echo (((isset($context["logo_link"]) || array_key_exists("logo_link", $context))) ? (_twig_default_filter((isset($context["logo_link"]) ? $context["logo_link"] : null), "#")) : ("#"));
                echo "\"";
                // line 5
                echo twig_escape_filter($this->env, (((isset($context["link_attribs"]) || array_key_exists("link_attribs", $context))) ? ((" " . (isset($context["link_attribs"]) ? $context["link_attribs"] : null))) : ("")), "html", null, true);
                echo ">
        ";
            }
            // line 7
            echo "        ";
            echo (isset($context["logo"]) ? $context["logo"] : null);
            echo "
        ";
            // line 8
            if ((isset($context["use_logo_link"]) ? $context["use_logo_link"] : null)) {
                // line 9
                echo "            </a>
        ";
            }
            // line 11
            echo "    </div>
";
        }
    }

    public function getTemplateName()
    {
        return "navigation/logo.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  46 => 11,  42 => 9,  40 => 8,  35 => 7,  30 => 5,  26 => 4,  24 => 3,  21 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "navigation/logo.twig", "E:\\phpstudy\\PHPTutorial\\WWW\\ciscn\\phpmyadmin\\templates\\navigation\\logo.twig");
    }
}
