fn main() {
    let data = vec![3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0];
    let want = vec![0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9];
    let got = selection_sort(&data);
    assert_eq!(want, got);
    let got = insertion_sort(&data);
    assert_eq!(want, got);
    let got = mergesort(&data);
    assert_eq!(want, got);
    let got = quicksort(&data);
    assert_eq!(want, got);
    let data: Vec<u32> = vec![3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0];
    let want: Vec<u32> = vec![0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9];
    let got = counting_sort(&data, 10);
    assert_eq!(want, got);
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
        d.swap(i, min_i);
    }
    return d;
}

fn insertion_sort(data: &[i32]) -> Vec<i32> {
    let mut d = Vec::from(data);
    for i in 1..d.len() {
        let mut j = i;
        while j > 0 && d[j] < d[j-1] {
            d.swap(j, j-1);
            j -= 1;
        }
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

fn quicksort(data: &[i32]) -> Vec<i32> {
    let mut d = Vec::from(data);
    _quicksort(&mut d, 0, (data.len()-1) as i32);
    return d;
}

fn _quicksort(d: &mut [i32], l: i32, h: i32) {
    if l >= h || l < 0 {
        return;
    }
    let p = _partition(d, l, h);
    _quicksort(d, l, p-1);
    _quicksort(d, p+1, h);
}

fn _partition(d: &mut [i32], l: i32, h: i32) -> i32 {
    let pivot = d[h as usize];
    let mut i = l-1;
    for j in l..h {
        if d[j as usize] <= pivot {
            i += 1;
            d.swap(i as usize, j as usize);
        }
    }
    i += 1;
    d.swap(i as usize, h as usize);
    return i
}

fn counting_sort(data: &[u32], radix: u32) -> Vec<u32> {
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