---
title: DSA Module 1 — Arrays
type: dsa-notes
module: 1
started: 2026-09-28
tags: [dsa, dsa/arrays]
---

# DSA Module 1 — Arrays

> [!info] How this file works
> **Part 1** tells you how to practise. **Part 2** covers each pattern: the signal that tells you to use it, the core idea, and a template (folded so you don't see it until you want it). **Part 3** has one card per problem, which you fill in *in your own words* after you solve it. **Part 4** is the review tracker, and that's the part that stops you forgetting.

---

## Week 1 plan — Mon 28 Sep → Sun 4 Oct 2026

Goal: **all 12 problems solved and their cards filled in by Sunday.** (Source: 12-Week DSA Checklist, Week 1: Arrays.)
The order is by pattern, so each day builds on the day before. Start each evening with **10–15 min of
reviews** from any row in Part 4 whose date is due, *then* do the new problems.

| Day | Learn first (≈20 min) | New problems | Reviews due |
|---|---|---|---|
| Mon 28 | Tech Interview Handbook: Array | Contains Duplicate · Best Time to Buy/Sell | Two Sum (from blank) |
| Tue 29 | Wikipedia: Kadane | Maximum Subarray · Product Except Self | Mon's two (+1d) |
| Wed 30 | USACO: Prefix Sums | Subarray Sum Equals K · Container With Most Water | Tue's two (+1d) |
| Thu 1 | USACO: Two Pointers | 3Sum · Set Matrix Zeroes | Wed's (+1d), Mon's (+3d) |
| Fri 2 | TIH: Matrix | Spiral Matrix | Thu's (+1d), Tue's (+3d) |
| Sat 3 | Re-read Patterns 2 + 4 | Trapping Rain Water · First Missing Positive | Fri's (+1d), Wed's (+3d) |
| Sun 4 | none | **Buffer:** catch up on anything that slipped | Sat's (+1d), Thu's (+3d) |

> [!warning] Rules for the week
> - **A missed day doesn't cascade.** Push its problems onto Sunday's buffer rather than doubling up the next day.
> - **The two Hards (Saturday) are allowed to take 45 min each.** If one isn't solved at 45 min,
>   open both hints, write it with the hint, and mark it for a +1d re-solve. That still counts as done.
> - **Week 1 done** = all 12 solved + cards filled. The +7d and +21d reviews carry on into Weeks 2–3,
>   alongside Strings. That's normal, and it's what makes it stick.

---

## Part 1 — The protocol (every problem)

1. **5 min, understand.** Before you write any code, add a comment at the top of the file with the
   brute-force approach and its Big-O. That's your baseline.
2. **20–25 min, attempt.** Try it yourself. If you're stuck at 15 min, open **Hint 1** only. At 25
   min, open Hint 2. Getting stuck is fine. Staying stuck for an hour isn't a good use of time.
3. **Test the edges** before you submit: empty or single element, all negative, duplicates, and
   the answer sitting at index 0 or at the last index.
4. **Submit on LeetCode**, then send me the code for review.
5. **Fill in the card (Part 3) without looking at the solution.** Writing it in your own words is
   what actually stores it. A card copied from the solution is a wasted card.
6. **Re-solve from a blank file** at +1, +3, +7 and +21 days (Part 4), in 15 minutes or less. If
   you fail one, restart that problem's schedule from +1.

> [!important] Why this sticks
> Reading a solution feels like learning, but most of it is gone within a week. What stays is
> **retrieval**: pulling the idea out of your head from a blank page, repeated at longer and
> longer gaps. Step 6 is the part that stops you forgetting. Don't skip it.

---

## Part 2 — Patterns

### Family tree: how the problems connect

```
Two Sum (hashmap of "what I need")
 ├── Contains Duplicate ..... the simplest version: a set of "seen"
 ├── Subarray Sum = K ....... the same trick, applied to prefix sums
 └── 3Sum ................... fix one number, then two-pointer the rest

Best Time to Buy/Sell (running min)
 └── Maximum Subarray ....... Kadane: the running best, one step further

Product Except Self ......... prefix × suffix
 └── Trapping Rain Water .... prefix-max × suffix-max, then squeezed down with two pointers
Container With Most Water ... two pointers moving inwards

Set Matrix Zeroes ........... in place: the first row/col act as markers
First Missing Positive ...... in place: the array is its own hashmap
Spiral Matrix ............... four walls closing in
```

If you remember this tree, one problem's solution reminds you of the next one's.

> [!note] Learn it here
> - **Start with** [Tech Interview Handbook: Array](https://www.techinterviewhandbook.org/algorithms/array/),
>   one page covering every pattern (about 15 min).
> - **Watch after each problem (free):** search YouTube for `neetcode <problem name>`
>   (e.g. "neetcode best time to buy and sell stock"). The problem-solution videos are free on
>   his YouTube channel; only the courses on neetcode.io are paid. Every "NeetCode video" below
>   means the free YouTube one. Compare their approach with yours, not the other way round.
> - **Text backup (free):** the **Solutions** tab on each LeetCode problem, sorted by Most Votes.
>   The official *Editorial* tab is sometimes Premium, so skip it.
> - Each pattern below has its own "Learn" line. Learn one pattern, then solve its problem straight away.

---

### 1. Array traversal with a hashmap

**Learn:** [Tech Interview Handbook: Array](https://www.techinterviewhandbook.org/algorithms/array/)
and [Hash Table](https://www.techinterviewhandbook.org/algorithms/hash-table/), plus the NeetCode Two Sum video.

**Use it when:** you have "find a pair / a complement / something seen before" and you want to
avoid O(n²).
**Idea:** as you walk the array, store what you've already seen in a dict, so each lookup is O(1).
**Cost:** O(n) time, O(n) space.

> [!example]- Template
> ```python
> seen = {}
> for i, x in enumerate(nums):
>     need = target - x
>     if need in seen:
>         return [seen[need], i]
>     seen[x] = i          # store AFTER checking, so x can't pair with itself
> ```

**Trap:** if you insert before you check, an element can match itself (e.g. `[3]` with target 6).

---

### 2. Two pointers

**Learn:** [USACO Guide: Two Pointers](https://usaco.guide/silver/two-pointers) (Silver), plus the
NeetCode videos for Container With Most Water and 3Sum.

**Use it when:** the array is sorted (or you can afford to sort it), you're looking for a pair,
or the question is about the two ends of something.
**Idea:** start with `l = 0` and `r = n-1`. Each step, move one pointer based on a rule that you
can **prove** never skips the answer.
**Cost:** O(n) time, O(1) space. Add O(n log n) if you have to sort first.

> [!example]- Template
> ```python
> l, r = 0, len(nums) - 1
> while l < r:
>     s = nums[l] + nums[r]
>     if s == target: ...
>     elif s < target: l += 1
>     else: r -= 1
> ```

**The maths part (your strength):** every two-pointer solution rests on an *exchange argument*:
"moving the other pointer could never give a better answer, so it's safe to throw it away."
If you can state that argument, you understand the problem.

---

### 3. Sliding window

**Learn:** [USACO Guide: Sliding Window](https://usaco.guide/gold/sliding-window) (free), plus the
NeetCode video for Longest Substring Without Repeating Characters. Watch it properly in Module 2.

**Use it when:** "longest / shortest / count of **contiguous** subarrays (or substrings) that
satisfy X".
**Idea:** grow the window with `r`. While the window breaks the condition, shrink it from `l`.
**Cost:** O(n), because each index enters the window once and leaves once.

> [!example]- Template
> ```python
> l = 0
> for r in range(len(nums)):
>     # add nums[r] to the window state
>     while window_invalid():
>         # remove nums[l] from the window state
>         l += 1
>     best = max(best, r - l + 1)
> ```

**Note:** none of the 7 problems below is a pure sliding window. You'll get plenty of it in
Module 2 (Strings), e.g. Longest Substring Without Repeating Characters.

---

### 4. Prefix sums

**Learn:** [USACO Guide: Prefix Sums](https://usaco.guide/silver/prefix-sums) (Silver). This is the
most rigorous explanation around. Read it before Product Except Self.

**Use it when:** you need "sum of the range i..j" many times, or "count the subarrays whose
sum is K".
**Idea:** `P[0] = 0`, `P[i+1] = P[i] + nums[i]`. Then `sum(nums[i..j]) = P[j+1] - P[i]`.
**Cost:** O(n) to build, then O(1) for each range query.

**The key link:** "subarray sum = K" becomes "find pairs where `P[j] - P[i] = K`", and **that is
Two Sum** on the prefix array. The same idea works with products (prefix × suffix).

> [!example]- Template
> ```python
> P = [0]
> for x in nums:
>     P.append(P[-1] + x)
> # sum of nums[i:j] == P[j] - P[i]
> ```

**Trap:** off-by-one between `P[j+1]` and `P[j]`, the same family as your `range()` slip.
Write out `P` for a 3-element example by hand before you trust your indices.

---

### 5. Kadane's algorithm

**Learn:** [Wikipedia: Maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem).
It's written as a DP recurrence with a correctness argument, so it plays to your maths.

**Use it when:** "maximum sum of a contiguous subarray", or a variant of it.
**Idea (as a DP recurrence):** `best_ending_here[i] = max(nums[i], best_ending_here[i-1] + nums[i])`.
In words: either extend the previous subarray, or start again here. The answer is the max over all `i`.
**Cost:** O(n) time, O(1) space.

> [!example]- Template
> ```python
> cur = best = nums[0]
> for x in nums[1:]:
>     cur = max(x, cur + x)
>     best = max(best, cur)
> ```

**Trap:** starting with `best = 0` breaks when every number is negative. Start from `nums[0]`.

---

### 6. In-place modification

**Learn:** the NeetCode videos for Set Matrix Zeroes and First Missing Positive (when you reach the stretch problems).

**Use it when:** the problem says "O(1) extra space" or "modify the array in place".
**Idea:** use a write pointer (`w`) that trails a read pointer, or use the array itself as
storage (index as hash, sign flipping, first row and column as markers).
**Problems:** Set Matrix Zeroes and First Missing Positive in CHECKLIST.md.

---

### 7. Matrix traversal

**Learn:** [Tech Interview Handbook: Matrix](https://www.techinterviewhandbook.org/algorithms/matrix/),
plus the NeetCode Spiral Matrix video.

**Use it when:** you have a 2D grid.
**Idea:** `rows, cols = len(g), len(g[0])`. For boundary walks (spiral), keep four walls
(`top, bottom, left, right`) and shrink them after each side.
**Trap:** forgetting to check `top <= bottom` and `left <= right` again partway through a loop.
**Problems:** Spiral Matrix and Set Matrix Zeroes in CHECKLIST.md.

---

### 8. Intervals

**Learn:** [Tech Interview Handbook: Interval](https://www.techinterviewhandbook.org/algorithms/interval/),
plus the NeetCode Merge Intervals video.

**Use it when:** you have a list of `[start, end]` pairs and need to merge, insert, or count overlaps.
**Idea:** **sort by start first**. Then two intervals overlap exactly when `cur.start <= prev.end`.
**Problems:** Merge Intervals and Insert Interval, which are in Module 11 (Sorting) of CHECKLIST.md.

---

## Part 3 — Problem cards

Cards are numbered, but **the Week 1 plan at the top sets the order** (by pattern, not by difficulty).

### 0. Two Sum ✅
- **Pattern:** hashmap traversal
- **Key insight (your words):**
- **Complexity:** O(n) / O(n)
- **Mistake I made:**
- **Code:** `../two_sum_1.py`

### 1. Best Time to Buy and Sell Stock
[LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

> [!tip]- Hint 1
> For each day, *if you sold today*, which day would you have wanted to buy on?

> [!tip]- Hint 2
> Keep one running variable for "the cheapest price so far". One pass is enough.

- **Pattern:**
- **Brute force + Big-O:**
- **Key insight (1 sentence):**
- **Complexity:**
- **Mistake I made:**

### 2. Maximum Subarray
[LeetCode 53](https://leetcode.com/problems/maximum-subarray/)

> [!tip]- Hint 1
> At each index, the best subarray *ending here* either includes the one before it or starts fresh.

> [!tip]- Hint 2
> When is it better to throw away everything you've accumulated? (When it's pulling you down.)

- **Pattern:**
- **Brute force + Big-O:**
- **Key insight:**
- **How is this like Problem 1?**
- **Mistake I made:**

### 3. Product of Array Except Self
[LeetCode 238](https://leetcode.com/problems/product-of-array-except-self/)

> [!tip]- Hint 1
> `answer[i]` = (product of everything on the left) × (product of everything on the right).

> [!tip]- Hint 2
> Two passes: left→right for the prefix products, right→left for the suffix products. You're not allowed to use division.

- **Pattern:**
- **Key insight:**
- **Why not division?** (think about zeros)
- **Mistake I made:**

### 4. Subarray Sum Equals K
[LeetCode 560](https://leetcode.com/problems/subarray-sum-equals-k/)

> [!tip]- Hint 1
> Sliding window **doesn't work** here. Why not? (Negative numbers.)

> [!tip]- Hint 2
> Running prefix sum `s`. How many earlier prefixes equal `s - k`? Keep a dict of prefix-sum counts, starting with `{0: 1}`.

- **Pattern:**
- **Key insight:**
- **How is this like Two Sum?**
- **Why `{0: 1}`?**
- **Mistake I made:**

### 5. Container With Most Water
[LeetCode 11](https://leetcode.com/problems/container-with-most-water/)

> [!tip]- Hint 1
> Start with the widest container (`l=0`, `r=n-1`). Which wall is limiting the area?

> [!tip]- Hint 2
> Move the *shorter* wall inwards. Prove to yourself that moving the taller one can never help.

- **Pattern:**
- **Key insight:**
- **The proof (1–2 lines):**
- **Mistake I made:**

### 6. 3Sum
[LeetCode 15](https://leetcode.com/problems/3sum/)

> [!tip]- Hint 1
> Sort first. Fix `nums[i]`, then the rest is a two-pointer "two sum = -nums[i]" on the right side.

> [!tip]- Hint 2
> Duplicates: skip `i` if `nums[i] == nums[i-1]`. After finding a triple, move both pointers past any equal values.

- **Pattern:**
- **Key insight:**
- **How I handled duplicates:**
- **Mistake I made:**

### 7. Contains Duplicate
[LeetCode 217](https://leetcode.com/problems/contains-duplicate/)

> [!tip]- Hint 1
> What does Two Sum's `seen` dict become when you don't need an index?

> [!tip]- Hint 2
> A `set`. Also compare it with the one-liner `len(set(nums)) != len(nums)`. Which one can stop early?

- **Pattern:**
- **Key insight:**
- **Two solutions + trade-off:**
- **Mistake I made:**

### 8. Set Matrix Zeroes
[LeetCode 73](https://leetcode.com/problems/set-matrix-zeroes/)

> [!tip]- Hint 1
> Get it working first with O(m + n) space: record the zero rows and zero columns in two sets, then do a second pass.

> [!tip]- Hint 2
> For O(1) space, use row 0 and column 0 *as* those sets. They overlap at `[0][0]`, so keep one
> extra boolean for "column 0 needs zeroing", and zero the first row/column **last**.

- **Pattern:**
- **Key insight:**
- **Why the first row/col must be done last:**
- **Mistake I made:**

### 9. Spiral Matrix
[LeetCode 54](https://leetcode.com/problems/spiral-matrix/)

> [!tip]- Hint 1
> Keep four walls: `top, bottom, left, right`. Walk right along `top`, then `top += 1`. Walk down `right`, then `right -= 1`. And so on.

> [!tip]- Hint 2
> Try it on a 3×4 (non-square) matrix. Before walking left and before walking up, check again that `top <= bottom` and `left <= right`.

- **Pattern:**
- **Key insight:**
- **The edge case that broke me:**
- **Mistake I made:**

### 10. Trapping Rain Water
[LeetCode 42](https://leetcode.com/problems/trapping-rain-water/) (Hard, 45 min allowed)

> [!tip]- Hint 1
> Water above bar `i` = `min(tallest on the left, tallest on the right) - height[i]`. Build both
> "tallest so far" arrays, just like the prefix and suffix products in Problem 3.

> [!tip]- Hint 2
> For O(1) space, use two pointers. Whichever side has the smaller running max, that side's water is already
> decided (the other side is guaranteed to be at least as tall), so process it and move inwards.

- **Pattern:**
- **The formula:**
- **How is this like Problem 3 and Problem 5?**
- **Mistake I made:**

### 11. First Missing Positive
[LeetCode 41](https://leetcode.com/problems/first-missing-positive/) (Hard, 45 min allowed)

> [!tip]- Hint 1
> With `n` numbers, the answer is always in `1..n+1`. Anything ≤ 0 or > n is noise.

> [!tip]- Hint 2
> Use the array as its own hashmap: keep swapping each value `x` into index `x-1` until it's in place
> (or is noise, or is a duplicate). Then the first index `i` where `nums[i] != i+1` gives the answer `i+1`.

- **Pattern:**
- **Key insight:**
- **Why it's still O(n) despite the while-loop inside the for-loop:**
- **Mistake I made:**

---

## Part 4 — Review tracker

Re-solve from a **blank file**, in ≤15 min, without looking. Tick a box and write the date. If you
fail a review, write ✗ and restart that problem at +1.

| # | Problem | Solved | +1d | +3d | +7d | +21d |
|---|---|---|---|---|---|---|
| 0 | Two Sum | 2026-09-14 | 2026-09-28 ✓ (1 nudge) | | | |
| 1 | Best Time to Buy/Sell | 2026-09-28 (NeetCode-assisted) | | | | |
| 2 | Maximum Subarray | | | | | |
| 3 | Product Except Self | | | | | |
| 4 | Subarray Sum = K | | | | | |
| 5 | Container With Most Water | | | | | |
| 6 | 3Sum | | | | | |
| 7 | Contains Duplicate | 2026-09-28 (Hint 1 used) | | | | |
| 8 | Set Matrix Zeroes | | | | | |
| 9 | Spiral Matrix | | | | | |
| 10 | Trapping Rain Water | | | | | |
| 11 | First Missing Positive | | | | | |

> [!check] Module done when
> All 12 have passed their +21d review **and** you can write the 5 pattern templates from memory
> on a blank page: hashmap, two pointers, sliding window, prefix sum, Kadane.
