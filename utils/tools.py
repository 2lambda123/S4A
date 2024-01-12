new line(s) to replace

        out['shadow_mask'] = shadows_cond

    if clouds:
        clouds_cond = (
                (bands['B03'] >= 0.319) & (bands['B05'] / bands['B11'] < 4.33) &
                (
                        ((bands['B11'] - bands['B10'] < 0.255) & (bands['B06'] - bands['B07'] < -0.016)) |
                        ((bands['B11'] - bands['B10'] >= 0.255) & (bands['B01'] >= 0.3))
                )
        )

        out['cloud_mask'] = clouds_cond

    if cirrus:
        cirrus_cond = (
            (
                (bands['B03'] < 0.319) & (bands['B8A'] >= 0.166) & (np.divide(bands['B02'], bands['B10']) < 14.689) &
                (np.divide(bands['B02'], bands['B09']) >= 0.788)
            ) |
            (
                (bands['B03'] >= 0.319) & (np.divide(bands['B05'], bands['B11']) < 4.33) &
                (bands['B11'] - bands['B10'] < 0.255) & (bands['B06'] - bands['B07'] >= -0.016)
            )
        )

        out['cirrus_mask'] = cirrus_cond

    if snow:
        snow_cond = (
                (bands['B03'] >= 0.319) & (np.divide(bands['B05'], bands['B11']) >= 4.33) & (bands['B03'] >= 0.525)
        )

        out['snow_mask'] = snow_cond

    # Logical OR between all masks is the final mask
    out = np.any(np.array(list(out.values())), axis=0)

    return out
