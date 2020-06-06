static bool cmp(vector <int> a, vector <int> b)
{
      return abs(a[0] - a[1]) > abs(b[0] - b[1]);
}
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) 
    {
        sort(costs.begin(), costs.end(), cmp);   
        long long int i, a, b, n, sum=0;
        n=costs.size();
        a=b=(n/2);
        for(i=0;i<n;i++)
        {
            if((costs[i][0]<=costs[i][1] && b>0) || a==0)
            {    
                b--;
                sum+=costs[i][0];
            }
            else
            {
                a--;
                sum+=costs[i][1];
            }
        
        }
        return sum;
    }
};