# PRIMMDebug Evaluation Study Repository

A repository containing the study materials and analysis code for the *PRIMMDebug: A Debugging Teaching Aid For Secondary Students* research paper (currently in review). For more information on PRIMMDebug, [visit the website](https://primmdebug.web.app/) or [view the source code](https://github.com/LaurieGale10/primmdebug).

The evaluation study collected data from several classes of secondary school students (aged 11-16) who used PRIMMDebug over a number of lessons. The main data collected was:
- **Survey responses** related to students' perspectives on PRIMMDebug (analysed in R).
- **Log data** from students using the PRIMMDebug tool (analysed in Python).

## Viewing the Study Materials
The following materials used in the evaluation study are available to view in the `study_materials` folder:
- The schedule for the initial teacher calls, where teachers were introduced to PRIMMDebug and invited to give initial feedback (`.pdf`).
- The student survey structure that students completed in their final lesson of using PRIMMDebug (`filename`).
- The schedule for the teacher interviews that took place after teachers had taught with PRIMMDebug to some of their secondary school students (`.pdf`).

## Viewing the Analysis
You can view the analysis that is reported in the paper in the following two jupyter notebooks:
- For the **survey responses**: `survey_analysis.pdf`
- For the **log data analysis**: `log_data_analysis.pdf`.
These notebooks document and visualise all of the results that are reported in the paper, as well as the code used to obtain them.

## Running the Analysis
Students' actual survey responses and log data are not currently public. As a result, the actual jupyter notebooks used for analysis cannot be run locally.

The student data will be added to this repository by the end of 2025, at which point you'll be able to use the run all of the analysis yourself. Once posted, more information on running will be provided here. In the meantime, view the two pdfs named above.

## Further Information
For more detail on the logging in the PRIMMDebug tool, view the [`logging.service.ts`](https://github.com/LaurieGale10/primmdebug/blob/main/src/app/services/logging.service.ts) file in the [PRIMMDebug GitHub repository](https://github.com/LaurieGale10/primmdebug).

### Versions
Python: 3.13 \
R: 4.5.1 (*Great Square Root*) \
Docker Desktop 4.28.0 was used for running tests on student programs