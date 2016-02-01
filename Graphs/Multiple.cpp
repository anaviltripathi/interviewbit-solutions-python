string Solution::multiple(int n) {
    vector<int> flag, parent, val;
    flag.clear(), parent.clear(), val.clear();
    flag.resize(n), parent.resize(n), val.resize(n);
    int p;
    int q;
    int i;
    int tot = 0;
     
    //final string
    string ret = "";
 
    //queue for bfs
    queue <int> Q;
 
    //initial node
    int temp = 1%n;
    flag[temp] = 1;
    val[temp] = 1;
    Q.push(temp);
 
    while(true) {
         
        //pop from queue
        temp = Q.front();
        Q.pop();
        p = temp;
 
        //reached final state
        //build solution here
        if(p == 0) {
     
            p  =0;
            ret += (char)(val[p]+'0');
            p = parent[p];
            while(p != 0) {
 
                ret += (char)(val[p]+'0');
                p = parent[p];
            }
             
            reverse(ret.begin(), ret.end());
            return ret;
        }
         
        //visit two neighbors p*10 and p*10+1
        //if already not visited
        q = (p*10) % n;
         
        if(flag[q] == 0)
            Q.push(q), flag[q] = 1, parent[q] = p, val[q]=0; 
 
        q++;
         
        if(q >= n) q -= n;
         
        if(flag[q] == 0)
            Q.push(q), flag[q] = 1, parent[q] = p, val[q] = 1;
    }
}
 


