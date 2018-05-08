import java.util.ArrayList;

public class StringBuffer {
    private ArrayList<String> buff;

    public StringBuffer() {
        buff = new ArrayList<>();
    }

    public void append(String w) {
        buff.add(w);
    }

    public String toString() {
        return buff.toString();
    }
}
