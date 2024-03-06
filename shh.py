def label_encoding_with_reversal(
    df: pd.DataFrame,
    encoding_paths: dict,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Encode the labels categorical and then reverse the labels.
    
    Args:
        df: DataFrame with categorical labels.
        encoding_paths: paths for the encodings.
    
    Returns:
        DataFrame with labels encoded and then reversed.
    """
    reversed_df = df.copy()
    for col, path in encoding_paths.items():
        le = LabelEncoder()
        le.classes_ = np.load(path, allow_pickle=True)
        reversed_df[col] = le.transform(df[col])
        # Reverse the encoding
        max_label = reversed_df[col].max()
        reversed_df[col] = max_label - reversed_df[col]
    return reversed_df

def label_decoding_with_reversal(
    df: pd.DataFrame,
    encoding_paths: dict,
) -> pd.DataFrame:
    """
    Decode the labels that were previously encoded and reversed.
    
    Args:
        df: DataFrame with reversed categorical labels.
        encoding_paths: paths for the encodings.
    
    Returns:
        DataFrame with labels decoded from reversed encoding.
    """
    decoded_df = df.copy()
    for col, path in encoding_paths.items():
        le = LabelEncoder()
        le.classes_ = np.load(path, allow_pickle=True)
        # Reverse the encoding back to original encoding before decoding
        max_label = le.transform(le.classes_).max()
        decoded_df[col] = max_label - df[col]
        decoded_df[col] = le.inverse_transform(decoded_df[col])
    return decoded_df