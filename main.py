import sys
import coverage
from sample.text_examples import TextExamples

if __name__ == "__main__":
    cov=coverage.Coverage()
    cov.start()
    args = sys.argv
    for i in args:
        l = TextExamples.quitarSigno(i)
        array = TextExamples.contar(l)
    cov.stop()
    cov.save()

    print("coverage report",cov.xml_report())
    print("data", cov.get_data().line_counts())



