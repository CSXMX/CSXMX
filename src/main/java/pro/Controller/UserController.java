package pro.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import pro.Mapper.UserMapper;
import pro.Entity.User;

import java.util.List;
import java.util.Map;

@RestController
public class UserController {
    @Autowired
    UserMapper myuser;
    @RequestMapping("/hello")
    public User getUser(){
        return myuser.getUser("1");
    }
    @RequestMapping("/2")
    public List<User> getUser1(){
        return myuser.getUser1("1");
    }


}
