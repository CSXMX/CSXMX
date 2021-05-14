package pro.Mapper;

import pro.Entity.User;
import java.util.*;
public interface UserMapper {
    public User getUser(String id);
    public List<User> getUser1(String id);

}
