fn main() {
    let data = vec![3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0];
    let want = vec![0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9];
    let got = insertion_sort(&data);
    assert_eq!(want, got);
}

fn insertion_sort(data: &[i32]) -> Vec<i32> {
    let mut d = Vec::from(data);
    for i in 1..d.len() {
        let mut j = i;
        while j > 0 && d[j] < d[j-1] {
            (d[j], d[j-1]) = (d[j-1], d[j]);
            j -= 1;
        }
    }
    return d;
}