use std::i32::{MAX, MIN};
use bisection::bisect_right;

fn main() {
    let seq = vec![0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15];
    let want = 6;
    let got = lis(&seq);
    assert_eq!(want, got);
}

fn lis(seq: &[i32]) -> usize {
    let mut s = vec![MAX; seq.len()+1];
    s[0] = MIN;
    for i in 0..seq.len() {
        let v = &seq[i];
        let j = bisect_right(&s, v);
        if &s[j-1] < v && v < &s[j] {
            s[j] = *v;
        }
    };
    let mut result = 1;
    for i in (0..seq.len()).rev() {
        if s[i] < MAX {
            result = i;
            break;
        }
    };
    return result;
}
