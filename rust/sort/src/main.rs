fn main() {
    let data = vec![3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0];
    let want = vec![0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9];
    let got = insertion_sort(&data);
    assert_eq!(want, got);
    let got = selection_sort(&data);
    assert_eq!(want, got);
    let got = mergesort(&data);
    assert_eq!(want, got);
    let data: Vec<u32> = vec![3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0];
    let want: Vec<u32> = vec![0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9];
    let got = count_sort(&data, 10);
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

fn selection_sort(data: &[i32]) -> Vec<i32> {
    let mut d = Vec::from(data);
    for i in 0..d.len() {
        let mut min_i = i;
        for j in i+1..d.len() {
            if d[j] < d[min_i] {
                min_i = j;
            }
        }
        (d[min_i], d[i]) = (d[i], d[min_i])
    }
    return d;
}

fn mergesort(data: &[i32]) -> Vec<i32> {
    let n = data.len();
    if n < 2 {
        return Vec::from(data);
    };
    let k = n / 2 ;
    let a = mergesort(&data[..k]);
    let b = mergesort(&data[k..]);
    return _merge(&a, &b);
}

fn _merge(a: &[i32], b: &[i32]) -> Vec<i32> {
    let n = a.len() + b.len();
    let mut aux = vec![0; n];
    let (mut i, mut j, mut k) = (0, 0, 0);
    while k < n  && i < a.len() && j < b.len() {
        if a[i] <= b[j] {
            aux[k] = a[i];
            i += 1;
        } else {
            aux[k] = b[j];
            j += 1;
        }
        k += 1;
    }
    while i < a.len() {
        aux[k] = a[i];
        i += 1;
        k += 1;
    }
    while j < b.len() {
        aux[k] =  b[j];
        j += 1;
        k += 1;
    }
    return aux;
}

fn count_sort(data: &[u32], radix: u32) -> Vec<u32> {
    let mut count = vec![0; (radix+1) as usize];
    for v in data {
        count[(v+1) as usize] += 1;
    }
    for i in 0..count.len()-1 {
        count[i+1] += count[i];
    }
    let mut result = vec![0; data.len()];
    for v in data {
        result[count[*v as usize]] = *v;
        count[*v as usize] += 1;
    }
    return result;
}