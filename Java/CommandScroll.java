class CommandScroll {
    <unithype> CommandScroll(unithype creature, int stack) {
        
        unithype[] Lords = (unithype[]) new Object[stack];
        for(int h = 0; h < Lords.length; h++) {
            Lords[h] = creature;
        }
        
        unithype[] clones = Lords;
        for(unithype search : clones) {
            System.out.print(search);
        }System.out.print("\n");
        
        for(int e = 0; e < Lords.length; e++) {
            Lords[e] = null;
        }
        
        for(unithype right : clones) {
            System.out.print(right);
        }
    }
    
    public static void main(String[] args) {
        Object hat = new CommandScroll(6, 66);
    }
}
