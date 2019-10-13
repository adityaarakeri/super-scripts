public class ListAlphabetizer {

    public static void main(String[] args) {

        List<String> objects= new ArrayList<String>();

        objects.add("ball");
        objects.add("cat");
        objects.add("apple");
        objects.add("dog");
        //insert more items by writing "objects.add("object");"

        if(!objects.isEmpty()){

            for(String emp:objects){

                System.out.println(emp);
            }

            Collections.sort(objects);

            System.out.println(objects);
        }
    }
}
