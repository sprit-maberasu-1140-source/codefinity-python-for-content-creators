import matplotlib.pyplot as plt

def visualize_age_distribution(audience_ages):
    age_groups = ['<18', '18-24', '25-34', '35-44', '45-54', '55+']
    group_counts = [0] * len(age_groups)
    for age in audience_ages:
        if age < 18:
            group_counts[0] += 1
        elif 18 <= age <= 24:
            group_counts[1] += 1
        elif 25 <= age <= 34:
            group_counts[2] += 1
        elif 35 <= age <= 44:
            group_counts[3] += 1
        elif 45 <= age <= 54:
            group_counts[4] += 1
        else:
            group_counts[5] += 1

    plt.bar(age_groups, group_counts, color='skyblue')
    plt.xlabel('Age Groups')
    plt.ylabel('Number of Viewers')
    plt.title('Audience Age Distribution')
    plt.tight_layout()
    plt.show()

audience_ages = [15, 22, 27, 35, 19, 40, 54, 33, 29, 18, 17, 23, 45, 36, 60, 25, 31, 43, 52, 47]
visualize_age_distribution(audience_ages)