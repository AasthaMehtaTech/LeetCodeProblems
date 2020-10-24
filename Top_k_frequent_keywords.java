// https://leetcode.com/discuss/interview-question/542597/

/*
Example :

Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.
*/



private static List<String> solve(int k, String[] keywords, String[] reviews) {
	List<String> res = new ArrayList<>();
	// Set<String> set = new HashSet<>(Arrays.asList(keywords)); if lowercase i/p only
  Set<String> set = new HashSet<>();
  for(String key : keywords) {
    set.add(key.toLowerCase());
  }
	Map<String, Integer> map = new HashMap<>();
	for(String r : reviews) {
		String[] strs = r.split("\\W");
		Set<String> added = new HashSet<>();
		for(String s : strs) {
			s = s.toLowerCase();
			if(set.contains(s) && !added.contains(s)) {
				map.put(s, map.getOrDefault(s, 0) + 1);
				added.add(s);
			}
		}
	}
	
  Queue<Map.Entry<String, Integer>> maxHeap = new PriorityQueue<>((a, b)->a.getValue() == b.getValue() ? a.getKey().compareTo(b.getKey()) : b.getValue() - a.getValue());
	maxHeap.addAll(map.entrySet());
	while(!maxHeap.isEmpty() && k-- > 0) {
		res.add(maxHeap.poll().getKey());
	}
  
	return res;
  
}


// Soln 2-  ArrayList| Easy Solution | No priority Queue -TC : O(N^2 + M) ,SC: O(N + M) 
// where N be the number of characters in the review string[] and M be the number of characters in the keywords list

     List<String> ls = new ArrayList<>(map.keySet()) ;
     Collections.sort(ls,(a,b)->(map.get(a)).equals(map.get(b))?a.compareTo(b):map.get(b)-map.get(a));
     return ls.subList(0,k) ;



public static void main(String[] args) {
	int k1 = 2;
	String[] keywords1 = { "anacell", "cetracular", "betacellular" };
	String[] reviews1 = { "Anacell provides the best services in the city", "betacellular has awesome services",
			"Best services provided by anacell, everyone should use anacell", };
	int k2 = 2;
	String[] keywords2 = { "anacell", "betacellular", "cetracular", "deltacellular", "eurocell" };
	String[] reviews2 = { "I love anacell Best services; Best services provided by anacell",
			"betacellular has great services", "deltacellular provides much better services than betacellular",
			"cetracular is worse than anacell", "Betacellular is better than deltacellular.", };
	System.out.println(solve(k1, keywords1, reviews1));
	System.out.println(solve(k2, keywords2, reviews2));
}


/* Python Soln

import re
from collections import Counter

class Element:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

def topKFrequent(k, keywords, reviews):
    '''
    k: int
    keywwords: list of string
    reviews: list of string
    '''
    data_value_dict = collections.Counter()
        key_value_dict = set(keywords)
        res = []

        for review in reviews:
            temp_list = review.lower().split(' ')

            for value in temp_list:
                value = re.sub('[^a-z]', '', value)

                if value in key_value_dict:
                    data_value_dict[value] += 1

        res = heapq.nsmallest(k, data_value_dict, key=lambda x: (-data_value_dict[x], x)) 
        # for getting max_count ele, comparator reversed based on value_count & then preference given to x: i.e.lexicographical order

        return res
    

print(topKFrequent(k, keywords, reviews))

*/
