<?php

/* config/form_display/fieldset_bottom.twig */
class __TwigTemplate_11a12c69b05726eb7f4d898a8329cd929096bbbf79156f4271500c5b805aa89c extends Twig_Template
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
        $context["colspan"] = 2;
        // line 2
        if ((isset($context["is_setup"]) ? $context["is_setup"] : null)) {
            // line 3
            echo "    ";
            $context["colspan"] = ((isset($context["colspan"]) ? $context["colspan"] : null) + 1);
        }
        // line 5
        if ((isset($context["show_buttons"]) ? $context["show_buttons"] : null)) {
            // line 6
            echo "    <tr>
        <td colspan=\"";
            // line 7
            echo twig_escape_filter($this->env, (isset($context["colspan"]) ? $context["colspan"] : null), "html", null, true);
            echo "\" class=\"lastrow\">
            <input type=\"submit\" name=\"submit_save\" value=\"";
            // line 8
            echo _gettext("Apply");
            echo "\" class=\"green\" />
            <input type=\"button\" name=\"submit_reset\" value=\"";
            // line 9
            echo _gettext("Reset");
            echo "\" />
        </td>
    </tr>
";
        }
        // line 13
        echo "</table>
</fieldset>
";
    }

    public function getTemplateName()
    {
        return "config/form_display/fieldset_bottom.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  47 => 13,  40 => 9,  36 => 8,  32 => 7,  29 => 6,  27 => 5,  23 => 3,  21 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "config/form_display/fieldset_bottom.twig", "E:\\phpstudy\\PHPTutorial\\WWW\\ciscn\\phpmyadmin\\templates\\config\\form_display\\fieldset_bottom.twig");
    }
}
