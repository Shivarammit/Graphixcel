import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os


def load_data(file_path):
    file_ext = os.path.splitext(file_path)[-1].lower()
    try:
        if file_ext == ".csv":
            data = pd.read_csv(file_path)
        elif file_ext in [".xls", ".xlsx"]:
            data = pd.read_excel(file_path, engine='openpyxl')
        else:
            raise ValueError("Unsupported file type. Only CSV or Excel files are allowed.")
        
        print("Data Loaded Successfully!")
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def clean_data(data):
    data.fillna(method='ffill', inplace=True)
    data.fillna(method='bfill', inplace=True)
    print("Missing values handled using forward and backward fill.")
    return data


def show_data_preview(data):
    print("\nAData Preview:")
    print(data.head())

def getDataList():
    file_path="media/file.xlsx"
    data = load_data(file_path)
    if data is None:
        return    
    data = clean_data(data)
    return data.columns.tolist()

def select_columns(data):
    print("\nAvailable Columns:")
    print(data.columns.tolist())
    
    while True:
        x_col = input("Select the column for X-axis: ")
        y_col = input("Select the column for Y-axis: ")
        if x_col in data.columns and y_col in data.columns:
            return x_col, y_col
        else:
            print("Invalid columns selected. Please try again.")


def plot_with_matplotlib(x_col, y_col):
    file_path="media/file.xlsx"
    data = load_data(file_path)
    if data is None:
        return    
    data = clean_data(data)
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_col], data[y_col], marker='o', color='b', linestyle='--')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col} (Matplotlib)")
    plt.grid()
    plt.savefig('media/output.png', format='png')  # Save as an image
    print(f"Matplotlib plot saved as output.png")
    plt.close()


def plot_with_plotly(data, x_col, y_col, output_file):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data[x_col], y=data[y_col], mode='lines+markers', name=f"{y_col} vs {x_col}"))
    fig.update_layout(
        title=f"{y_col} vs {x_col} (Plotly)",
        xaxis_title=x_col,
        yaxis_title=y_col,
        template='plotly_dark'
    )
    fig.write_image(output_file)  # Save as an image
    print(f"Plotly plot saved as {output_file}")


def generate_bar_chart(x_col, y_col):
    file_path="media/file.xlsx"
    data = load_data(file_path)
    if data is None:
        return    
    data = clean_data(data)
    plt.figure(figsize=(10, 6))
    plt.bar(data[x_col], data[y_col], color='skyblue')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col} (Bar Chart)")
    plt.savefig("media/output.png", format='png')  # Save as an image
    print(f"Bar chart saved as output.png")
    plt.close()


def generate_pie_chart(y_col):
    file_path="media/file.xlsx"
    data = load_data(file_path)
    if data is None:
        return    
    data = clean_data(data)
    plt.figure(figsize=(8, 8))
    data_counts = data[y_col].value_counts()
    plt.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
    plt.title(f"Pie Chart of {y_col}")
    plt.savefig("media/output.png", format='png')  # Save as an image
    print(f"Pie chart saved as output.png")
    plt.close()


def main():
    print("Welcome to Excel/CSV Graph Visualizer!")
    
    file_path = input("Enter the path of the Excel or CSV file: ")
    data = load_data(file_path)
    if data is None:
        return
    
    data = clean_data(data)
    show_data_preview(data)

    # Select Columns for Line and Bar Charts
    x_col, y_col = select_columns(data)

    # Save Matplotlib Line Plot
    matplotlib_output = "matplotlib_plot.png"
    print("\nGenerating and saving Matplotlib Line Plot...")
    plot_with_matplotlib(data, x_col, y_col, matplotlib_output)

    # Save Plotly Line Plot
    plotly_output = "plotly_plot.png"
    print("\nGenerating and saving Plotly Line Plot...")
    plot_with_plotly(data, x_col, y_col, plotly_output)

    # Save Bar Chart
    bar_chart_output = "bar_chart.png"
    print("\nGenerating and saving Bar Chart...")
    generate_bar_chart(data, x_col, y_col, bar_chart_output)

    # Generate and Save Pie Chart
    y_col_pie = input("Enter the column for the Pie Chart: ")
    if y_col_pie in data.columns:
        pie_chart_output = "pie_chart.png"
        print("\nGenerating and saving Pie Chart...")
        generate_pie_chart(data, y_col_pie, pie_chart_output)
    else:
        print("Invalid column for Pie Chart. Skipping Pie Chart generation.")


if __name__ == "__main__":
    main()
