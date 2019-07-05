package hgame.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.*;
import java.util.Base64;

@Controller
public class MathController {

    @RequestMapping(value = "/index", method = RequestMethod.GET)
    public String index(ModelMap model, HttpSession session, HttpServletResponse response) throws IOException {
        Object step = session.getAttribute("step");
        if (step == null) {
            session.setAttribute("step", '1');
            response.sendRedirect("/index.php");
            return null;
        } else if (step.toString().equals("1")) {
            model.addAttribute("message", "Welcome to the world of mathematics.<br/>" +
                    "Let's warm up first.<br/>1+1=?");
        } else if (step.toString().equals("2")) {
            model.addAttribute("message", "It seems that you have learned it, let us do a difficult question.<br/>" +
                    "<img src=/img/cXVlc3Rpb24ucG5n.php><br/>Show me the smallest integer solutions.");
        }
        return "math";
    }

    @RequestMapping(value = "/index", method = RequestMethod.POST)
    public void pindex(@RequestParam(value = "answer") String answer, HttpSession session, HttpServletResponse response) throws IOException {
        Object step = session.getAttribute("step");
        if (step == null) {
            session.setAttribute("step", '1');
            response.sendRedirect("/index.php");
        } else if (step.toString().equals("1")) {
            if (answer.equals("2")) {
                session.setAttribute("step", "2");
                response.sendRedirect("/index.php");
            }
        }
    }

    @RequestMapping(value = "/img/{path}", method = RequestMethod.GET)
    public String image(@PathVariable("path") String path, HttpServletResponse response) {
        path = new String(Base64.getDecoder().decode(path));
        InputStream f = null;
        OutputStream out = null;

        try {
            f = new FileInputStream("/home/static/" + path);
            out = response.getOutputStream();
            int count = 0;
            byte[] buffer = new byte[1024 * 8];
            while ((count = f.read(buffer)) != -1) {
                out.write(buffer, 0, count);
                out.flush();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        try {
            f.close();
            out.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        return "ok";
    }

    @RequestMapping(value = "/flag", method = RequestMethod.GET)
    public String Flag(ModelMap model) {
        System.out.println("This is the last question.");
        System.out.println("123852^x % 612799081 = 6181254136845 % 612799081");
        System.out.println("The flag is hgame{x}.x is a decimal number.");
        model.addAttribute("flag", "Flag is not here.");
        return "flag";
    }
}
