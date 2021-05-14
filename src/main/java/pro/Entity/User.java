package pro.Entity;

public class User {
    private String id;
    private String sname;
    private String sex;
    public void setId(String id) {
        this.id = id;
    }
    public void setLastName(String sname) {
        this.sname = sname;
    }
    public void setGender(String sex) {
        this.sex = sex;
    }
    public String getid(){
        return id;
    }
    public String getsname(){
        return sname;
    }
    public String getsex(){
        return sex;
    }
}
